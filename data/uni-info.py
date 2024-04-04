import psycopg2


# Connect to database
conn = psycopg2.connect(
    database="CPUS",
     host="localhost", 
    port="5432", 
    user="postgres",
    password="12345",
)
cursor = conn.cursor()

# Take input from user
University_abstract = input("Enter university abstract: ")
College_name = input("Enter college name: ")
spec_name = input("Enter specialization name: ")
gpa_male = input("Enter specialization name: ")
qudurat_male =  input(" ")
tahsili_male =  input(" ")
gpa_female =  input(" ")
qudurat_female =  input(" ")
tahsili_female =  input(" ")

# Insert user data into the table
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (University_abstract,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (College_name,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (spec_name,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (gpa_male,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (qudurat_male,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (tahsili_male,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (gpa_female,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (qudurat_female,))
cursor.execute("INSERT INTO users (abstract) VALUES (%s)", (tahsili_female,))

conn.commit()

# Close connection
conn.close()


