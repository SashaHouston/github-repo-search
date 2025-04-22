import httpx
import logging
from typing import List, Dict
from app.core.settings import settings

logger = logging.getLogger(__name__)

class OctoFetchery:
    GITHUB_API = "https://api.github.com/search/repositories"

    def __init__(self, token: str):
        self.headers = {"Authorization": f"Bearer {token}"}

    async def dig_for_codegems(self, query: str, limit: int = 10) -> List[Dict]:
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": limit}
        async with httpx.AsyncClient() as client:
            try:
                res = await client.get(self.GITHUB_API, headers=self.headers, params=params, timeout=10)
                res.raise_for_status()
                gems = res.json().get("items", [])
                return [
                    {
                        "title": gem["full_name"],
                        "web": gem["html_url"],
                        "stars": gem["stargazers_count"]
                    } for gem in gems
                ]
            except httpx.RequestError as exc:
                logger.error(f"Connection error while fetching from GitHub: {exc}")
                raise
            except httpx.HTTPStatusError as exc:
                logger.error(f"GitHub returned an error: {exc.response.text}")
                raise
