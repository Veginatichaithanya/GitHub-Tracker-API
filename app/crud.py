from sqlalchemy.orm import Session
from . import models

def create_repo(db: Session, repo_name: str, github_url: str, stars: int, owner: str):
    repo = models.Repository(
        repo_name=repo_name,
        github_url=github_url,
        stars=stars,
        owner=owner,
    )
    db.add(repo)
    db.commit()
    db.refresh(repo)
    return repo

def get_repo(db: Session, repo_id: int):
    return db.query(models.Repository).filter(models.Repository.id == repo_id).first()

def get_all_repos(db: Session):
    return db.query(models.Repository).all()

def update_repo_note(db: Session, repo_id: int, note: str):
    repo = get_repo(db, repo_id)
    if not repo:
        return None
    repo.note = note
    db.commit()
    db.refresh(repo)
    return repo

def delete_repo(db: Session, repo_id: int):
    repo = get_repo(db, repo_id)
    if not repo:
        return False
    db.delete(repo)
    db.commit()
    return True
