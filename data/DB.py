import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456'
}

cpsu_connection = mysql.connector.connect(**db_config, database='cpsu')
noor_connection = mysql.connector.connect(**db_config, database='noor')
qiyasdb_connection = mysql.connector.connect(**db_config, database='qiyasdb')
timeline_connection = mysql.connector.connect(**db_config, database='timeline')

query = """
SELECT * FROM (
    SELECT * FROM cpsu.cpsudb
    UNION ALL
    SELECT * FROM noor.noordb
    UNION ALL
    SELECT * FROM qiyasdb.qiyasdb
    UNION ALL
    SELECT * FROM timeline.timeline
) AS combined_table;
"""

result = cpsu_connection.execute(query)


cpsu_connection.close()
noor_connection.close()
qiyasdb_connection.close()
timeline_connection.close()