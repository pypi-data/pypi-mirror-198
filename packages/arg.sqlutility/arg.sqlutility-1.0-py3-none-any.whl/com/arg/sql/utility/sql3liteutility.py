import sqlite3

""" This module simplify the usage of SQL without using command"""


class SQL3LiteUtility:
    """This class contains different method for CRUD operation with SQL without writing command"""

    def __init__(self):
        self._db_name = None
        self._table_name = None
        self._sql_command = None
        self._sql_rows: list[dict] | None = None

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, name):
        self._db_name = name

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, name):
        self._table_name = name

    @property
    def sql_rows(self):
        return self._sql_rows

    @sql_rows.setter
    def sql_rows(self, rows: list[dict]):
        self._sql_rows = rows

    def write_in_table(self):
        """
          This method create data in table.

          The table name has to be preset,example:sql_utility.table_name = "posts"

          The db name has to be preset,example:sql_utility.db_name = "db_social.sqlite3"

          The row has to be preset as dictionary,example:sql_utility.sql_rows = {"country":"India","state":"Karnataka",
          "capital":"Bengaluru"}

          Parameters:
          None

          Returns:
          None

          """
        values = ("?," * len(self.sql_rows[0]))[0:-1]
        self._sql_command = "INSERT INTO " + self._table_name + " VALUES(" + values + ")"

        with sqlite3.connect(self._db_name) as conn:
            for sql_row in self._sql_rows:
                print(self._sql_command)
                print(tuple(sql_row.values()))
                conn.execute(self._sql_command, tuple(sql_row.values()))
            conn.commit()

    def read_from_table(self):
        """
                  This method read data from table.

                  The table name has to be preset,example:sql_utility.table_name = "posts"

                  The db name has to be preset,example:sql_utility.db_name = "db_social.sqlite3"

                  Parameters:
                  None

                  Returns:
                  None

                  """
        self._sql_command = "select * from " + self._table_name

        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.execute(self._sql_command)
            for row in cursor:
                print(row)
            conn.commit()
