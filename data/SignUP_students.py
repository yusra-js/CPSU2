from flask import Flask, render_template,request,redirect,url_for
import psycopg2

app= Flask(__name__)

def connect_db():

    connect = psycopg2.connect(
        database="CPUS",
        host="localhost",
        port="5432",
        user="postgres",
        password="12345"
    )
    return connect


    def close_conn (connect, cursor):
        if cursor:
            cursor.close()
        if connect:
            connect.close()

            @app.route("/signup_1",methodes=["GET","POST"])
            def signup_1():
                if request.method == "POST":
                    Student_ID = request.form["Stu_ID"]
                    Student_name = request.form["Stu_name"]
                    Student_email = request.form["Stu_email"]
                    Student_password= request.form["pass_1"]
                    Student_password= request.form["pass_2"]

                   

                    connect=connect_db()
                    cursor=connect.cursor()

                    try:
                       cursor.execute("INSERT INTO students (university_name, university_email, university_pass, university_pass2) VALUES (%s, %s, %s, %s)", (Stu_ID, Stu_name, Stu_email, pass_1,pass_2))
                       connect.commit()
                       return redirect(url_for("signup_success"))
                    except psycopg2.Error as e :
                        print("Error inserting data",e)
                        connect.rollback()
                    finally:
                        close_conn(connect, cursor)
                return render_template("signup.html")

            @app.route("/signup1_success")
            def signup1_success():
                return "Signup successful!"

            if __name__== "__main__":
                app.run(debug=True)





                    



