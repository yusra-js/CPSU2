import psycopg2
import unittest
from unittest.mock import patch

def connect_postgresql(database: str, user: str, password: str, host: str, port: str) -> psycopg2.extensions.connection:
    try:
        # Establishing a connection to the PostgreSQL database
        connection = psycopg2.connect(
            database=database,
            host=host,
            port=port,
            user=user,
            password=password
        )

        return connection

    except psycopg2.OperationalError as e:
        # Corrected exception handling syntax
        raise psycopg2.OperationalError(f"Error connecting to the PostgreSQL DB:{e}")

class TestConnectPostgreSQL(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_success_connection(self, mock_connect):
        mock_connect.return_value = 'connection'
        connection = connect_postgresql("CPUS", "postgres", "12345", "localhost", "5432")
        self.assertEqual(connection, 'connection')

    @patch('psycopg2.connect')
    def test_fail_connection(self, mock_connect):
        mock_connect.side_effect = psycopg2.OperationalError("Connection error")
        with self.assertRaises(psycopg2.OperationalError):
            connect_postgresql("HI", "postgres", "12345", "localhost", "5432")

if __name__ == "__main__":
    unittest.main()
