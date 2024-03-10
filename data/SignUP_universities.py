from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://username:password@localhost/databasename"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class University(db.Model):
    __tablename__ = "universites"

    university_id = db.Column(db.Integer, primary_key=True)
    university_name = db.Column(db.String(255), nullable=False)
    university_email = db.Column(db.String(255), nullable=False)
    university_pass = db.Column(db.String(255), nullable=False)
    university_abstract = db.Column(db.Text, nullable=False)
    gpa_male = db.Column(db.Integer)
    qudurat_male = db.Column(db.Integer, nullable=False)
    tahsili_male = db.Column(db.Integer, nullable=False)
    gpa_female = db.Column(db.Integer, nullable=False)
    qudurat_female = db.Column(db.Integer, nullable=False)
    tahsili_female = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(255))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        university_name = request.form["university_name"]
        university_email = request.form["university_email"]
        university_pass = request.form["university_pass"]
        university_abstract = request.form["university_abstract"]
        gpa_male = request.form.get("gpa_male") or None
        qudurat_male = request.form["qudurat_male"]
        tahsili_male = request.form["tahsili_male"]
        gpa_female = request.form["gpa_female"]
        qudurat_female = request.form["qudurat_female"]
        tahsili_female = request.form["tahsili_female"]
        city = request.form["city"]

        new_university = University(
            university_name=university_name,
            university_email=university_email,
            university_pass=university_pass,
            university_abstract=university_abstract,
            gpa_male=gpa_male,
            qudurat_male=qudurat_male,
            tahsili_male=tahsili_male,
            gpa_female=gpa_female,
            qudurat_female=qudurat_female,
            tahsili_female=tahsili_female,
            city=city,
        )
        db.session.add(new_university)
        db.session.commit()
        return redirect(url_for("signup_success"))
    return render_template("signup.html")


@app.route("/signup_success")
def signup_success():
    return render_template("signup_success.html")


if __name__ == "__main__":
    app.run(debug=True)
