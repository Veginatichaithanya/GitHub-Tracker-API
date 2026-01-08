import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

async def fetch_user_repos(username: str):
    url = f"https://api.github.com/users/{username}/repos"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=HEADERS)

    if resp.status_code != 200:
        raise Exception("GitHub API error")

    return resp.json()
