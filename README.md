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

**Group Chat + Leaderboard**  


---

## 🛠 Tech Stack

- **Backend:** Django, Django Channels
- **Frontend:** Tailwind CSS, Bootstrap
- **Real-Time:** WebSockets, Daphne, Channels Redis
- **Database:** SQLite (default), can be changed to PostgreSQL/MySQL
- **APIs:** LeetCode stats API
<img width="1920" height="1020" alt="Screenshot 2025-08-03 203821" src="https://github.com/user-attachments/assets/df4f3650-1a9f-4aad-9054-f39ad564f3ec" />

---

## ⚙️ Installation

1. Clone the repository
   git clone https://github.com/albinea/LeetSquad.git
   cd LeetSquad
2.Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

2.Install dependencies
pip install -r requirements.txt

3.Run migrations
python manage.py migrate

4.Create a superuser
python manage.py createsuperuser

Run the development server with Daphne

daphne -p 8000 leetsquad.asgi:application


Project Structure

leetsquad/
├── core/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── consumers.py       # WebSocket handlers
│   ├── models.py          # Database models
│   ├── routing.py         # WebSocket routing
│   ├── urls.py            # Application URLs
│   ├── utils.py           # LeetCode scraping utility
│   └── views.py           # Application views
├── leetsquad/             # Project configuration
│   ├── asgi.py            # ASGI configuration
│   ├── settings.py        # Django settings
│   └── urls.py            # Project URLs
├── static/                # Static assets
└── manage.py              # Django management script

