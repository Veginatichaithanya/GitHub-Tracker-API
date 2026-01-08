from pydantic import BaseModel
from datetime import datetime

class GitHubImportRequest(BaseModel):
    username: str

class RepoCreate(BaseModel):
    repo_name: str
    github_url: str
    stars: int
    owner: str

class RepoUpdate(BaseModel):
    note: str

class RepoResponse(BaseModel):
    id: int
    repo_name: str
    github_url: str
    stars: int
    owner: str
    note: str | None
    created_at: datetime

    class Config:
        from_attributes = True
