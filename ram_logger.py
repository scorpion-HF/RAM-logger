import threading
from sql_connector import SqlConnection
from free import get_free_command_output
import time


class RamLogger:
    def __init__(self, db_path):
        self.db_path = db_path
        self.thread = threading.Thread(target=self.logging_to_database, name='ram_logger', daemon=True)
        self.logger_status = True

    def logging_to_database(self):
        database_connection = SqlConnection(self.db_path)
        while self.logger_status:
            free_output = get_free_command_output()
            status = (free_output["total"], free_output["used"], free_output["free"])
            database_connection.write_ram_status(status)
            time.sleep(3)

    def start_logging(self):
        self.thread.start()

    def stop_logging(self):
        self.logger_status = False
