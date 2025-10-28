![Tests](https://github.com/MortezaHashemabadi/devhub-api/actions/workflows/ci.yml/badge.svg)

# 🚀 DevHub API — Open Source Developer Community (Django + DRF)

**DevHub API** is an open-source platform for developers to share projects, get feedback, and explore trending projects weekly.  
Built with **Django REST Framework**, it features JWT authentication, automated tests, Docker, and CI/CD via GitHub Actions.

---

## ⚙️ Tech Stack

| Component               | Technology                         |
|------------------|---------------------------------|
| Backend          | Django 5, Django REST Framework |
| Auth             | JWT (SimpleJWT)                 |
| Database         | SQLite (Dev & CI)               |
| Testing          | pytest + pytest-django          |
| CI/CD            | GitHub Actions (Dockerized)     |
| Containerization | Docker & Docker Compose         |

---

## ✨ Features

✅ Register / Login (JWT Authentication)  
✅ Developer Profiles (auto-created on registration)  
✅ CRUD Projects (Create, Read, Update, Delete)  
✅ Like (Star) + View Count  
✅ Comments System  
✅ Trending Projects (based on stars & views in the last 7 days)  
✅ Unit Tests with pytest
✅ CI/CD with GitHub Actions   
✅ Dockerized Setup

---

## 🧠 Project Description

DevHub is a modern, community-driven API for developers.  
It aims to provide an experience similar to **GitHub Explore** or **ProductHunt** for developer projects.  
Users can publish their projects, star others’ projects, leave comments, and view trending projects weekly.

> 🧩 Designed with clean architecture, testability, and fast Docker deployment in mind.

---

---

## 🧩 Installation & Setup

```bash
git clone https://github.com/MortezaHashemabadi/devhub-api.git
cd devhub-api
```

🔹 Local (manual)
python -m venv .venv
source .venv/bin/activate # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 🔹 With Docker

docker-compose up --build

Access the API at http://localhost:8000.

### 🔐 Authentication

| Endpoint               | Description                         |
|------------------|---------------------------------|
| POST /api/auth/register/          | Register a new user |
| POST /api/token/           | Login (JWT Access & Refresh Tokens)                |
| POST /api/token/refresh/       | Refresh JWT Access Token            |
	

Example Login Response:

{
"access": "<JWT_ACCESS>",
"refresh": "<JWT_REFRESH>"
}

### 🧱 Core API Endpoints

| Method   | Endpoint                          | Description              |
| -------- | --------------------------------- | ------------------------ |
| GET      | `/api/projects/`                  | List all projects        |
| POST     | `/api/projects/`                  | Create a new project     |
| GET      | `/api/projects/{id}/`             | Retrieve project details |
| POST     | `/api/projects/{id}/toggle_star/` | Star or unstar a project |
| POST     | `/api/projects/{id}/add_view/`    | Increment view count     |
| GET      | `/api/projects/trending/`         | List trending projects   |
| GET/POST | `/api/comments/`                  | List or create comments  |

## 🧪 Run Tests
- Locally : pytest -v
- Inside Docker : docker run --rm devhub-api pytest -v

Example output:

==========================
3 passed in 2.10s
==========================

___

## 🐳 Docker Compose Configuration

This project is fully Dockerized using SQLite.
Directory structure:

devhub-api/
│
├── core/
├── developers/
├── users/
├── db_data/
│   └── db.sqlite3
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md


- Run with:

docker-compose up --build

---

## ⚙️ CI/CD via GitHub Actions

On each push to main, GitHub Actions:

Builds the Docker image

Runs automated tests

Displays test results as a badge

---
## 📈 Example: Trending Endpoint
GET /api/projects/trending/

Response:

[
{
"title": "AI Portfolio Builder",
"stars_count": 30,
"views": 120
},
{
"title": "FastAPI Scraper",
"stars_count": 18,
"views": 80
}
]

___

## 🧩 Contributing

Pull Requests and Issues are welcome 💬
If you have ideas for new features (e.g., notifications, tagging system), feel free to submit a PR.

--- 

## 🧾 License

MIT License © 2025 Morteza Hashemabadi