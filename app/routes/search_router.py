from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.logic.repo_engine import OctoFetchery
from app.core.settings import settings

router = APIRouter()

fetch_tool = OctoFetchery(token=settings.github_token)

@router.get("/search")
async def trigger_search(request: Request, keyword: str):
    try:
        data = await fetch_tool.dig_for_codegems(query=keyword)
        return JSONResponse(content={"status": "ok", "data": data})
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
