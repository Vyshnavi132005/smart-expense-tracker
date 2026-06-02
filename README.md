# SMART EXPENSE TRACKER

SMART EXPENSE TRACKER is a beginner-friendly but professional Django web application for managing personal expenses.

## Features

- User registration, login, and logout
- Add expenses
- Edit expenses
- Delete expenses
- View only your own expenses
- Filter expenses by month
- Dashboard cards for spending summary
- Chart.js analytics
- Download expenses as CSV
- About page with profile links
- Admin panel support

## 📸 Project Screenshots

### Login Page
![Login Page](Smart%20expense%20tracker_ScreenShots/Login-Page.png)

### Registration Page
![Registration Page](Smart%20expense%20tracker_ScreenShots/Registration-Page.png)

### Dashboard
![Dashboard](Smart%20expense%20tracker_ScreenShots/Dashboard-Home-Page.png)

### Expense Analytics
![Expense Analytics](Smart%20expense%20tracker_ScreenShots/Expense-Charts.png)

### Edit Expense Feature
![Edit Expense Feature](Smart%20expense%20tracker_ScreenShots/Edit-Expense-Feature.png)

### About Page
![About Page](Smart%20expense%20tracker_ScreenShots/About-Page.png)
## Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS, Bootstrap
- Charts: Chart.js
- Database:
  - Local: SQLite or PostgreSQL/MySQL depending on setup
  - Deployment: PostgreSQL on Render

## Project Structure

```text
expense_tracker_project/
├── build.sh
├── manage.py
├── requirements.txt
├── README.md
├── expense_tracker/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── expenses/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        ├── about.html
        ├── base.html
        ├── edit.html
        ├── home.html
        ├── login.html
        └── register.html
