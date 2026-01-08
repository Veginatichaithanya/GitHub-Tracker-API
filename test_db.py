from app.database import SessionLocal
from app import crud

db = SessionLocal()

repo = crud.create_repo(db, "test", "http://x.com", 5, "me")
print("Created:", repo.id)

fetched = crud.get_repo(db, repo.id)
print("Fetched:", fetched.repo_name)

updated = crud.update_repo_note(db, repo.id, "hello")
print("Updated note:", updated.note)

deleted = crud.delete_repo(db, repo.id)
print("Deleted:", deleted.id)
