# 📝 Feedback Management System with Admin Panel (Flask + MySQL)

## 🔍 Project Description

This is a **Flask-based web application** designed to collect, manage, and export user feedback. It features both a public feedback submission form and a secure admin panel for managing submissions.

Admins can:
- Log in securely
- View all submitted feedback
- Download feedback as a CSV file
- Change their password from the interface

The interface uses **Bootstrap 5** for a responsive and modern UI.

---

## ⚙️ Features

### 🌐 Public Feedback Form
Visitors can submit their **name**, **email**, and **feedback** through the homepage.

### 🔐 Admin Login
Secure login system for admins to access the dashboard.

### 📊 Admin Dashboard
View all submitted feedback in a clean, searchable table.

### 📥 Download CSV
Export all feedback entries into a CSV file with one click.

### 🔄 Change Password
Admins can securely change their login password from the UI.

### 💡 Bootstrap 5 UI
Clean, mobile-friendly layout using the latest Bootstrap version.

---

## 🛠️ Tech Stack

| Layer     | Technology           |
|-----------|----------------------|
| Frontend  | HTML, Bootstrap 5     |
| Backend   | Flask (Python)       |
| Database  | MySQL                |
| CSV Export| Python `csv` + `io`  |

---

## 🚀 Getting Started

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

### 🗄️ Set up your MySQL database
```CREATE DATABASE feedback;

USE feedback;

CREATE TABLE feedbacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    feedback TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE admin_login (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Add a sample admin user
INSERT INTO admin_login (email, password) VALUES ('admin@example.com', 'admin123');
```
### ▶️ Run the Flask App
```
python main.py
```

The app will be available at: http://127.0.0.1:5000/

### 📂 File Structure
```
├── main.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── change_pass.html

```
