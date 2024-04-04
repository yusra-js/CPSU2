# pip install psycopg2 flask  ------ in terminal


from flask import Flask, request, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    database="CPUS",
        host="localhost",
        port="5432",
        user="postgres",
        password="12345"
)
cur = conn.cursor()

@app.route('/LogIn_2', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur.execute("SELECT * FROM students WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            return "Login successful"
        else:
            return "Invalid credentials"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


