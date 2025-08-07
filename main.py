from flask import Flask,render_template,request,redirect,url_for,send_file #type:ignore
import mysql.connector #type:ignore
import csv
import io

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
   if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        feedback=request.form["feedback"]

        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback"
        )
        cursor=conn.cursor()

        try:
            cursor.execute("INSERT INTO feedbacks(name,email,feedback)VALUES(%s,%s,%s)",(name,email,feedback))
            conn.commit()
            message = "✅ Feedback submitted successfully!"
            print("values inserted succesfully!")
        except Exception as e:
            print(f"error occured:{e}")
        
        return render_template("index.html",message=message)
   else:
      return render_template("index.html")

@app.route("/admin_login",methods=["GET","POST"])
def admin():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]

        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback"
        )
        cursor=conn.cursor()

        cursor.execute("SELECT * from admin_login WHERE email=%s AND password=%s",(email,password))
        result = cursor.fetchone()
        message_success="logged in successfully!"
        message_failure = "Login failed. Please check your credentials and try again."

        if(result):
            return redirect(url_for('dashboard'))
        else:
            return render_template("admin_login.html",message_failure=message_failure)
    return render_template("admin_login.html")

@app.route("/admin_dashboard")
def dashboard():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="feedback"
    )
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM feedbacks")
    feedbacks=cursor.fetchall()

    conn.close()

    return render_template("admin_dashboard.html",feedbacks=feedbacks)

@app.route("/csv_file")
def csv_file():
    conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback"
    )
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM feedbacks")
    feedbacks=cursor.fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Id', 'Name', 'Email', 'Feedback', 'Submitted At'])
    for fb in feedbacks:
        writer.writerow([
            fb['id'],
            fb['name'],
            fb['email'],
            fb['feedback'],
            fb['submitted_at']
        ])
    output.seek(0)

    # Send CSV as a downloadable file
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='feedbacks.csv'
    )


@app.route("/change_pass", methods=["GET", "POST"])
def change_pass():
    message = None

    if request.method == "POST":
        email = request.form["email"]
        old_pass = request.form["old_pass"]
        new_pass = request.form["new_pass"]

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback"
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM admin_login WHERE email=%s AND password=%s", (email, old_pass))
        user = cursor.fetchone()

        if user:
            cursor.execute("UPDATE admin_login SET password=%s WHERE email=%s", (new_pass, email))
            conn.commit()
            message = "✅ Password updated successfully!"
        else:
            message = "❌ Incorrect email or old password!"

        conn.close()

    return render_template("change_pass.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
