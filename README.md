# 🚀 GitHub Tracker API

A backend REST API built using FastAPI and PostgreSQL that allows users to import GitHub repositories, store them locally, manage them, add notes, and delete them.

This project was built as a take-home backend assessment to demonstrate:

- REST API design
- Database integration
- External API integration
- CRUD operations
- Validation and error handling
- Basic testing

---

# 📌 Problem Understanding

The goal is to build a backend service that:

- Talks to an external API (GitHub API)
- Stores processed data in a local PostgreSQL database
- Exposes exactly **4 core CRUD endpoints** (POST, GET, PUT, DELETE)
- Uses strict validation and proper status codes

---

# 🧠 Use Case

This project acts as a **GitHub Repository Tracker / Bookmarking System**.

It allows users to:

- Import repositories from GitHub
- Store them locally
- View saved repositories
- Add notes to them
- Delete them

⚠️ Important:

> This project **DOES NOT** create repositories on GitHub.  
> It only **reads data from GitHub** and stores it locally.

---

# 🧾 Assumptions

- Only **public repositories** are used
- GitHub token is valid and has no rate limit issues
- No authentication system is required
- Duplicate repositories are allowed (can be improved)
- Pagination from GitHub API is not handled (simplified for assignment)

---

# 🏗️ Tech Stack

- Backend: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Validation: Pydantic
- HTTP Client: httpx
- Environment Config: python-dotenv
- Testing: pytest + httpx

---

# 📂 Project Structure

```
github-tracker-api/
├── app/
│   ├── main.py        # FastAPI app & routes
│   ├── database.py    # Database connection config
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   ├── crud.py        # Database operations
│   ├── api.py         # GitHub API client
├── tests/
│   └── test_api.py    # Basic API tests
├── .env.example
├── requirements.txt
├── README.md
```

---

# 🗃️ Database Design

Single table: `repositories`

Fields:

- id (PK)
- repo_name
- github_url
- stars
- owner
- note
- created_at

---

# 🔁 Data Flow Example (POST)

POST `/repos/from-github`

1. Calls GitHub API
2. Fetches repository list
3. Takes first repo
4. Saves it in DB
5. Returns saved row

---

# 🚨 Error Handling

- Uses FastAPI `HTTPException`
- Returns:
  - 404 if repo not found
  - 400 if GitHub API fails
  - 422 for validation errors

---

# ⚙️ How To Run The Project

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pytest httpx python-dotenv
python.exe -m pip install --upgrade pip

```

---

## 3️⃣ Configure Environment Variables

Create `.env` file in root:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/github_tracker
GITHUB_TOKEN=your_github_personal_access_token
```

---

## 4️⃣ Create Database

```bash
psql -U postgres
CREATE DATABASE github_tracker;
\q
```

---

## 5️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

## 6️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```
<img width="1685" height="713" alt="image" src="https://github.com/user-attachments/assets/ab373c37-4e28-4746-ba49-5cc3ce927b7f" />

---


# 🔥 API Endpoints

### Import Repo from GitHub
POST `/repos/from-github`

```json
{ "username": "torvalds" }
```

```
```
<img width="1686" height="822" alt="image" src="https://github.com/user-attachments/assets/fffd6a5d-691a-4640-87e1-5dc5afb25b9b" />

---



### List All Repos
GET `/repos`

```
<img width="1660" height="668" alt="image" src="https://github.com/user-attachments/assets/f87cb5e9-5039-4093-b04e-1e73d370e5fe" />

---

```
<img width="1618" height="545" alt="image" src="https://github.com/user-attachments/assets/e2eec37f-e96d-4d02-a0bf-7fcfffce74f0" />


---



### Get One Repo
GET `/repos/{repo_id}`

---

### Update Repo Note
PUT `/repos/{repo_id}`

```json
{ "note": "Important project" }
```

---

### Delete Repo
DELETE `/repos/{repo_id}`

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🗄️ View Database Data

```bash
psql -U postgres -d github_tracker
SELECT * FROM repositories;
\q
```

---

# ✅ Conclusion

This project demonstrates:

- External API integration
- Database state management
- REST API design
- Validation & error handling
- Basic testing
