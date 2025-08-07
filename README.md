📝 Feedback Management System with Admin Panel (Flask + MySQL)
🔍 Project Description
This is a Flask-based web application designed to collect, manage, and export user feedback. It features both a public feedback submission form and a secure admin panel for managing submissions. Admins can log in, view all feedback, download feedback as a CSV file, and change their password securely. The interface is built using Bootstrap 5 to ensure a responsive and user-friendly experience.

⚙️ Features
🌐 Public Feedback Form
Visitors can submit their name, email, and feedback through the homepage.

🔐 Admin Login
Secure login system for admins to access the dashboard.

📊 Admin Dashboard
View all submitted feedback in a tabular format.

📥 Download CSV
Export all feedback entries into a CSV file with one click.

🔄 Change Password
Admins can securely change their login password from the UI.

💡 Bootstrap 5 UI
Clean, mobile-friendly layout using the latest Bootstrap version.

🛠️ Tech Stack
Layer	Technology
Frontend	HTML, Bootstrap 5
Backend	Flask (Python)
Database	MySQL
CSV Exporting	Python csv + io

## install dependencies from requirements.txt, use:
pip install -r requirements.txt

Set up your MySQL database:

sql
Copy
Edit
CREATE DATABASE feedback;

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
Run the Flask app

📂 File Structure
pgsql
Copy
Edit
├── app.py
├── templates/
│   ├── index.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── change_pass.html
📌 Optional Enhancements (Ideas)
Add password hashing for security.

Add pagination to feedback dashboard.

Add email notifications on new feedback.

Create admin session management.
