LeetSquad

LeetSquad is a Django-based web application that allows users to create and join groups, chat in real time, and view live **LeetCode statistics** for group members.  
It is designed for competitive programmers to collaborate, share progress, and track rankings.

---

🚀 Features

- **User Authentication** (Register/Login/Logout)
- **Create & Join Groups**
- **Real-Time Chat** using Django Channels & WebSockets
- **LeetCode Stats Integration** (problems solved, easy/medium/hard breakdown)
- **Group Leaderboard** sorted by total problems solved
- **Responsive UI** using Tailwind CSS & Bootstrap

---
📸 Screenshots

Dashboard View  

<img width="1920" height="1020" alt="Screenshot 2025-08-03 203700" src="https://github.com/user-attachments/assets/cc7d53f1-3aa4-4482-8a12-386c15488193" />



---

## 🛠 Tech Stack

- **Backend:** Django, Django Channels
- **Frontend:** Tailwind CSS, Bootstrap
- **Real-Time:** WebSockets, Daphne, Channels Redis
- **Database:** SQLite (default), can be changed to PostgreSQL/MySQL
- **APIs:** LeetCode stats API
- 
- **Group Chat + Leaderboard**  
<img width="1920" height="1020" alt="Screenshot 2025-08-03 203821" src="https://github.com/user-attachments/assets/df4f3650-1a9f-4aad-9054-f39ad564f3ec" />

---

## ⚙️ Installation

1. Clone the repository
   ```
   git clone https://github.com/albinea/LeetSquad.git
   cd LeetSquad
   ```
2.Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
2.Install dependencies
```
pip install -r requirements.txt
```
3.Run migrations
```
python manage.py migrate
```
4.Create a superuser
```
python manage.py createsuperuser
```
Run the development server with Daphne
```
daphne -p 8000 leetsquad.asgi:application
```
File tree
```
Project_leetsquad
├─ README.md
├─ core
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ consumers.py
│  ├─ forms.py
│  ├─ management
│  │  ├─ __init__.py
│  │  └─ commands
│  │     ├─ __init__.py
│  │     ├─ update_leetcode_stats.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ routing.py
│  ├─ services.py
│  ├─ urls.py
│  └─ views.py
├─ leetsquad
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ manage.py
├─ requirements.txt
└─ templates
   ├─ base.html
   ├─ core
   │  ├─ create_group.html
   │  ├─ dashboard.html
   │  ├─ group_detail.html
   │  └─ join_group.html
   └─ registration
      ├─ login.html
      └─ register.html

```
👥 Contributors
Nijoy P Jose
https://github.com/NIJOY-P-JOSE

