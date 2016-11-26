import psycopg2
import psycopg2.extras
from psycopg2 import ProgrammingError


class Database(object):
    """Database class to abstract underlying database platform and driver

    host -- database host to connect to
    db -- name of database to use
    username -- username to connect with
    password -- oassword to use for connection
    """
    def __init__(self, host, db, username, password):
        self._host = host
        self._db = db
        self._username = username
        self._password = password
        self._cursor = None
        self._conn = None

    def connect(self):
        """Connect to the database specified in the constructor"""
        try:
            self._conn = psycopg2.connect(host=self._host,
                                          database=self._db,
                                          user=self._username,
                                          password=self._password
                                          )
            self._cursor = \
                self._conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            return True
        except Exception:
            return False

    def close(self):
        """Close the connection to the database,
        should be called once the database is no longer required
        """
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()

    def execute(self, query):
        """Execute a SQL query against the current database

        query -- the sql query to run

        returns True if the query succeeded, False otherwise
        """
        try:
            self._cursor.execute(query)
        except ProgrammingError:
            return False
        return True

    def fetch_one_row(self):
        """Fetch the next row from the database,
        a query should have been executed first
        """
        try:
            return self._cursor.fetchone()
        except ProgrammingError:
            pass
        return {}

    def fetch_all_rows(self):
        """Fecth all rows from the database,
        a query should have been executed first
        """
        try:
            return self._cursor.fetchall()
        except ProgrammingError:
            pass
        return {}
