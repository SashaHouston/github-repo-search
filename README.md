# GitHub Repo Search (FastAPI + JS)

Простое веб-приложение для поиска самых популярных репозиториев по ключевому слову с использованием FastAPI и GitHub API.

# Установка

```bash


git clone https://github.com/yourname/github-repo-search
cd github-repo-search
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # добавьте свой GitHub токен
uvicorn app.main:app --reload