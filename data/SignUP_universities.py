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

            @app.route("/signup",methodes=["GET","POST"])
            def signup():
                if request.method == "POST":
                    university_name = request.form["name"]
                    university_email = request.form["Email"]
                    university_pass = request.form["passs"]
                    university_pass2= request.form["passs2"]
                    # university_abstract = request.form["university_abstract"]
                    # gpa_male = request.form.get("gpa_male") or None
                    # qudurat_male = request.form["qudurat_male"]
                    # tahsili_male = request.form["tahsili_male"]
                    # gpa_female = request.form["gpa_female"]
                    # qudurat_female = request.form["qudurat_female"]
                    # tahsili_female = request.form["tahsili_female"]
                    # city = request.form["city"]

                    connect=connect_db()
                    cursor=connect.cursor()

                    try:
                       cursor.execute("INSERT INTO universites (university_name, university_email, university_pass, university_pass2) VALUES (%s, %s, %s, %s)", (university_name, university_email, university_pass, university_pass2))
                       connect.commit()
                       return redirect(url_for("signup_success"))
                    except psycopg2.Error as e :
                        print("Error inserting data",e)
                        connect.rollback()
                    finally:
                        close_conn(connect, cursor)
                return render_template("signup_uni.html")

            @app.route("/signup_success")
            def signup_success():
                return "Signup successful!"

            if __name__== "__main__":
                app.run(debug=True)





                    



