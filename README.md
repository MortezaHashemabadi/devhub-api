# 🚀 DevHub API — Developer Community Platform (Django + DRF)

DevHub API یک پلتفرم Open Source برای اشتراک‌گذاری پروژه‌های برنامه‌نویسیه،  
الهام گرفته از GitHub Explore و ProductHunt.  
کاربران می‌تونن پروژه‌هاشونو منتشر کنن، کامنت بذارن، Star بدن و پروژه‌های ترند هفته رو ببینن ⭐  

---

## ⚙️ Tech Stack

- **Backend:** Django 5, Django REST Framework  
- **Auth:** JWT (SimpleJWT)  
- **Database:** SQLite (dev) / PostgreSQL (prod)  
- **Testing:** pytest + pytest-django  
- **Filtering & Search:** django-filter  
- **CI/CD:** GitHub Actions (pytest + flake8)

---

## 🚀 Features

✅ Register / Login (JWT Authentication)  
✅ Developer Profiles (auto-created)  
✅ CRUD Projects  
✅ Like (Star) + View Count  
✅ Search / Filter / Pagination  
✅ Comments System  
✅ Trending Projects (based on views & stars in last 7 days)  
✅ Unit Tests with pytest  

---

## 🧩 Installation & Setup

```bash
git clone https://github.com/<your-username>/devhub-api.git
cd devhub-api

# create virtual env
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# install dependencies
pip install -r requirements.txt

# migrate db
python manage.py migrate

# run server
python manage.py runserver
```
---

##🔐 Authentication

Register → /api/auth/register/

Login → /api/token/
Returns:

{"access": "<JWT_ACCESS>", "refresh": "<JWT_REFRESH>"}