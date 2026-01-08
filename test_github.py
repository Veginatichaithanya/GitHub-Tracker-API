import asyncio
from app.api import fetch_user_repos

async def main():
    repos = await fetch_user_repos("torvalds")
    print("Repo count:", len(repos))
    print("First repo name:", repos[0]["name"])

asyncio.run(main())
