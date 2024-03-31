from flask import Flask, render_template , jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Database connection parameters
db_params = {
    "host": "localhost",
    "user": "postgres",
    "password": "12345",
    "database": "CPSU-DB"
}
@app.route('/specialties')
def specialties():
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(**db_params)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example query: Replace with your actual query
        query = sql.SQL("""
            SELECT u.name AS university_name, c.name AS college_name, s.name AS specialty_name
            FROM universities u
            JOIN colleges c ON u.common_column = c.common_column
            JOIN specialties s ON c.another_common_column = s.another_common_column
        """)

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Pass the fetched data to the HTML template
        return render_template('specialties.html', specialties=rows)

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return "Error fetching data from the database."

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
