"""Test for the database class

Ideally should use a Mock object rather than live database, but time is limited
"""

import env

from reportservice.database import Database


class TestDatabase(object):
    def setup_method(self):
        db_host = 'candidate.suade.org'
        db_name = 'suade'
        db_username = 'interview'
        db_password = 'LetMeIn'
        self._database = Database(db_host, db_name, db_username, db_password)

    def teardown_method(self):
        self._database.close()

    def test_database_connection(self):
        connected = self._database.connect()
        assert connected

    def test_execute_valid(self):
        connected = self._database.connect()
        assert connected
        result = \
            self._database.execute("select * from information_schema.tables")
        assert result

    def test_execute_invalid(self):
        connected = self._database.connect()
        assert connected
        result = self._database.execute("select * from unknown_table")
        assert result is False

    def test_fetch_one_row(self):
        connected = self._database.connect()
        assert connected
        result = \
            self._database.execute("select * from information_schema.tables")
        assert result
        result = self._database.fetch_one_row()
        assert result

    def test_fetch_one_row_no_result(self):
        connected = self._database.connect()
        assert connected
        result = \
            self._database.execute("select id, type from reports where id='0'")
        assert result
        result = self._database.fetch_one_row()
        assert result is None

    def test_fetch_all_rows(self):
        connected = self._database.connect()
        assert connected
        sql = ("select column_name, data_type, character_maximum_length "
               "from INFORMATION_SCHEMA.COLUMNS "
               "where table_name = 'reports';"
               )
        result = self._database.execute(sql)
        assert result
        results = self._database.fetch_all_rows()
        assert len(results) == 2
