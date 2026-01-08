# 🚀 GitHub Tracker API

A backend REST API built using **FastAPI** and **PostgreSQL** that allows users to import GitHub repositories, store them locally, manage them, add notes, and delete them.

This project demonstrates:

- ✅ FastAPI backend development
- ✅ PostgreSQL database integration
- ✅ SQLAlchemy ORM usage
- ✅ External API integration (GitHub API)
- ✅ Full CRUD operations
- ✅ Clean backend architecture

---

## 📌 What This Project Does

This project is a **GitHub Repository Tracker / Bookmarking System**.

It:

- Fetches repository data from **GitHub API**
- Stores repository metadata in a **local PostgreSQL database**
- Allows you to:
  - Import repositories from GitHub
  - List saved repositories
  - View a single repository
  - Add / update notes
  - Delete repositories

> ⚠️ Important:  
> This project does **NOT** create repositories on GitHub.  
> It only **reads data from GitHub** and stores it in your local database.

---

## 🏗️ Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **HTTP Client:** httpx
- **Environment Config:** python-dotenv

---

## 📂 Project Structure

github-tracker-api/
├── app/
│ ├── main.py # FastAPI app & routes
│ ├── database.py # DB connection setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # DB operations
│ ├── api.py # GitHub API integration
├── tests/
├── .env
├── requirements.txt
├── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv


Activate it:

venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure .env File

Create a .env file in root:

DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/github_tracker
GITHUB_TOKEN=your_github_personal_access_token


4️⃣ Create Database

Open PostgreSQL:

psql -U postgres


Create DB:

CREATE DATABASE github_tracker;


Exit:

\q

5️⃣ Run the Server
uvicorn app.main:app --reload

6️⃣ Open API Docs

Open in browser:

http://127.0.0.1:8000/docs

🔥 API Endpoints
✅ Import Repo from GitHub
POST /repos/from-github
{
  "username": "torvalds"
}

✅ List All Saved Repos
GET /repos

✅ Get One Repo
GET /repos/{repo_id}

✅ Update Repo Note
PUT /repos/{repo_id}
{
  "note": "Important project"
}

✅ Delete Repo
DELETE /repos/{repo_id}

🗄️ View Data in Database

Open PostgreSQL:

psql -U postgres -d github_tracker


Run:

SELECT * FROM repositories;


Exit:

\q