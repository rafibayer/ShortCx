import mysql.connector
import time
import logging


RETRY_DELAY=5

class DataStore:

    def __init__(self, db_host, db_user, db_pass, db_name):
        
        logging.info(f'Tying to connect to db: {db_user}@{db_host}:{db_pass} ({db_name=})')
        while True:
            try:
                self.database = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_pass,
                    auth_plugin='mysql_native_password',
                    database=db_name)
                logging.info(f'Connection succeeded!')
                break

            except Exception as e:
                logging.warn(f'Connection failed: \n\t{e}\n\tRetrying in {RETRY_DELAY} sec...')
                time.sleep(RETRY_DELAY)

    def _db_init(self):
        pass

        