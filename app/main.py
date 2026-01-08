from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, crud, schemas
from .api import fetch_user_repos

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="GitHub Tracker API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------- ROOT --------------------
@app.get("/")
def root():
    return {"status": "ok"}

# -------------------- IMPORT FROM GITHUB --------------------
@app.post("/repos/from-github", response_model=schemas.RepoResponse)
async def import_repo(data: schemas.GitHubImportRequest, db: Session = Depends(get_db)):
    try:
        repos = await fetch_user_repos(data.username)
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to fetch from GitHub")

    if not repos:
        raise HTTPException(status_code=404, detail="No repositories found")

    repo = repos[0]  # take first repo

    saved = crud.create_repo(
        db,
        repo_name=repo["name"],
        github_url=repo["html_url"],
        stars=repo["stargazers_count"],
        owner=repo["owner"]["login"],
    )

    return saved

# -------------------- CREATE MANUALLY --------------------
@app.post("/repos", response_model=schemas.RepoResponse)
def create_repo(data: schemas.RepoCreate, db: Session = Depends(get_db)):
    return crud.create_repo(db, data.repo_name, data.github_url, data.stars, data.owner)

# -------------------- GET ONE --------------------
@app.get("/repos/{repo_id}", response_model=schemas.RepoResponse)
def get_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = crud.get_repo(db, repo_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repo not found")
    return repo

# -------------------- GET ALL --------------------
@app.get("/repos", response_model=list[schemas.RepoResponse])
def list_repos(db: Session = Depends(get_db)):
    return crud.get_all_repos(db)

# -------------------- UPDATE --------------------
@app.put("/repos/{repo_id}", response_model=schemas.RepoResponse)
def update_repo(repo_id: int, data: schemas.RepoUpdate, db: Session = Depends(get_db)):
    repo = crud.update_repo_note(db, repo_id, data.note)
    if not repo:
        raise HTTPException(status_code=404, detail="Repo not found")
    return repo

# -------------------- DELETE --------------------
@app.delete("/repos/{repo_id}")
def delete_repo(repo_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_repo(db, repo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Repo not found")
    return {"deleted": True}
