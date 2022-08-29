import sqlite3


class SqlConnection:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS RamStatus"
            "(total INTEGER, used INTEGER, free INTEGER , date_time TEXT DEFAULT CURRENT_TIMESTAMP);"
        )

    def write_ram_status(self, status):
        self.connection.execute(
            "INSERT INTO RamStatus"
            "(total, used, free)"
            "VALUES"
            "({}, {}, {});".format(status[0], status[1], status[2])
        )
        print("ram status logged")
        self.connection.commit()

    def get_last_status(self, number):
        if not isinstance(number, int):
            raise "Invalid argument, input for number of logs must be an integer number"
        statuses = self.connection.execute(
            "SELECT total, used, free FROM RamStatus ORDER BY date_time DESC LIMIT {};".format(number)
        )
        return list(statuses)
