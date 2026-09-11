# CPSU — A Shared Platform for Saudi Universities & Students

**CPSU** ("منصة مشتركة للجامعات والطلاب" — *a shared platform for universities and students*) is a graduation project that connects Saudi high‑school graduates with Saudi universities in one place: browsing available universities and specialties, calculating admission scores, getting specialty suggestions, ranking specialty preferences, and tracking each university's registration timetable — all from a single platform.

**Author:** Yusra Salamah

## ✨ Key Features

- **Two account types** — separate sign‑up/login flows for **Students** (`singup_student.html`, `login_student.html`) and **Universities** (`signup_uni.html`, `login_uni.html`).
- **Browse universities** — a searchable directory of Saudi universities (`all_unis1.html`, `all_unis2.html`, `all_unis3.html`) with a dedicated profile page per university (e.g. `uni-single-tu.html` for Taibah University, `uni-single-saud.html`, `uni-singel-kfupm.html`, `uni-singel-uqu.html`, `uni-single-uka.html`).
- **University admin panel** (`uni-info.html`) — universities can add their colleges, specialties, seat counts, and required weighted‑score percentages.
- **Weighted score (النسبة الموزونة) calculator** — computes each student's admission score from three components, matching the real Saudi university admission formula:
  - High school average — 40%
  - Qudrat (cognitive/aptitude test) — 30%
  - Tahsili (achievement test) — 30%
- **Smart specialty suggestions** — a decision‑tree classifier (ID3/C4.5‑style, using entropy and information gain — `data/c45.py`) plus a simpler threshold‑based suggestion function (`data/specificationsSugg.py`) recommend specialties the student is likely to qualify for based on their weighted score.
- **Specialty preference ranking** (`Order_Specialties.html`, `specialties.html`) — a two‑list "move item from List 1 to List 2" interface letting students order their desired specialties by priority, similar to the real Saudi admission preference system.
- **Student dashboard** (`main-studentPage.html`, `student-info.html`) — view/edit personal and academic information (national ID, nationality, ID expiry, grades, etc.).
- **Registration timetable** (`Time_Table.html`) — a shared calendar showing each university's registration dates (Hijri & Gregorian) and direct registration links.
- **Statistics page** (`statistics.html`) — a dashboard for aggregate platform data.

## 🛠️ Tech Stack

**Frontend**
- HTML5, CSS3 (custom `style.css` + Bootstrap)
- JavaScript / jQuery (`jquery.min.js`, `bootstrap.js`, `carousel.js`, `parallax.js`, `animate.js`, `prettyPhoto`, `videobg.js`, `map.js`)

**Backend**
- Python 3 with **Flask** (routes for sign‑up/login)
- **PostgreSQL** via `psycopg2` for data storage
- `flask_sqlalchemy` used in an early prototype (`tast.py`)

**Algorithms**
- Custom decision‑tree implementation (entropy / information gain) for specialty recommendation
- Weighted‑average formula for admission score calculation

**Testing**
- Python `unittest` with `unittest.mock` for database‑connection tests

## 📂 Project Structure

```
CPSU2/
├── index.html                  # Landing page
├── login_student.html / singup_student.html      # Student auth
├── login_uni.html / signup_uni.html               # University auth
├── main-studentPage.html                          # Student dashboard
├── student-info.html                              # Student profile / academic info
├── specialties.html / Order_Specialties.html      # Specialty browsing & preference ranking
├── all_unis1.html / all_unis2.html / all_unis3.html   # University directory (paginated)
├── uni-info.html                                  # University admin panel
├── uni-single-*.html / uni-singel-*.html          # Individual university profile pages
├── Time_Table.html                                # Cross-university registration timetable
├── statistics.html                                # Statistics dashboard
├── style.css
├── css/                        # Bootstrap & Font Awesome
├── js/                         # jQuery, Bootstrap, carousel, parallax, animation scripts
├── icon/                       # UI icons
├── images/
│   ├── uni/                    # University logos/photos (set 1)
│   └── uni2/                   # University logos/photos (set 2)
└── data/                       # Python / Flask backend
    ├── DB.py                          # Database connection example
    ├── SignUP_students.py             # Student sign-up route (Flask)
    ├── SignUP_universities.py         # University sign-up route (Flask)
    ├── LogIn_students.py              # Student login route (Flask)
    ├── LogIn_universities.py          # University login route (Flask)
    ├── CalculateGPA.py                # Weighted score calculator (CLI)
    ├── specificationsSugg.py          # Weighted score + specialty suggestion (CLI)
    ├── c45.py                         # Decision-tree specialty classifier
    ├── uni-info.py                    # CLI script to insert university/college data
    ├── tast.py                        # Early Flask + SQLAlchemy prototype
    └── Unit_Tests.py/
        └── DBconnectTest.py           # Unit tests for the DB connection
```

## ▶️ How to Run

### Frontend only (UI preview)
Since the pages are static HTML/CSS/JS, you can preview the interface without any backend:
1. Open `index.html` directly in a browser, **or**
2. Serve the folder locally for correct relative paths, e.g.:
   ```bash
   python -m http.server 8000
   ```
   then visit `http://localhost:8000`.

### Full stack (with backend + database)
1. Install PostgreSQL and create a database (the scripts currently expect one named `CPSU`/`CPUS`).
2. Install the Python dependencies:
   ```bash
   pip install flask psycopg2 flask_sqlalchemy pandas numpy
   ```
3. Update the database credentials (`host`, `port`, `database`, `user`, `password`) in `data/DB.py`, `data/LogIn_students.py`, `data/LogIn_universities.py`, `data/SignUP_students.py`, `data/SignUP_universities.py`, and `data/c45.py` to match your local setup.
4. Run the relevant Flask script, e.g.:
   ```bash
   python data/LogIn_students.py
   ```
5. Run the unit tests:
   ```bash
   python -m unittest "data/Unit_Tests.py/DBconnectTest.py"
   ```

## ⚠️ Known Limitations / Work in Progress

This is an active graduation project, and a few backend pieces are still incomplete or inconsistent — worth knowing before a demo or before continuing development:
- In `SignUP_students.py` and `SignUP_universities.py`, the Flask `@app.route` functions are currently nested *inside* `close_conn()`, so they aren't registered as routes. They need to be moved out to the top level of the file (indented at module level, alongside `connect_db()`), and the `INSERT` statements' variable names need to match the form field variables actually captured (e.g. `Student_ID` vs. `Stu_ID`).
- `LogIn_universities.py` references `uni_name` in the SQL query before it's actually assigned from `request.form['uni_name']` — this needs a small fix (assign it to a variable first).
- Database table/column names differ slightly between scripts (`CPSU` vs `CPUS`, `username`/`password` vs `university_name`/`university_pass`) and should be unified against your actual schema.
- Credentials (database user/password) are currently hardcoded for local development — move these to environment variables (e.g. a `.env` file with `python-dotenv`) before deploying or sharing publicly.
- `c45.py` reference a placeholder table (`your_table_name`) — replace with the actual specialties/students table name once the schema is finalized.

## 📌 Notes
- The "Order Specialties" (`Order_Specialties.html`) and "Specialties" (`specialties.html`) pages implement the same two‑list ranking flow used in the real Saudi university admission process, where students order their preferred specialties from most to least wanted.
- The weighted score formula (40% high school / 30% Qudrat / 30% Tahsili) matches the general formula used by many Saudi universities, though the exact weighting can vary by institution and program.
