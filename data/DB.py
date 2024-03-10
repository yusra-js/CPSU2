import psycopg2

connection = psycopg2.connect (
    host="localhost", 
    port="5432", database="CPSU",
    user="postgres",
    password="12345"
      
)
 
#create a cursor
cursor = connection.cursor()
 
# execute the queries
cursor.execute("SELECT * FROM CPSU_DB1")
result=cursor.fetchall()
 
cursor.close()
connection.close
 
 
 
 