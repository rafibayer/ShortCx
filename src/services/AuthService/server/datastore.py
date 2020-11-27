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

        logging.info('Attempting to initialize users table')
        self._db_init()

    def _db_init(self):
        create = self.database.cursor()
        create_sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            created_at DATE NOT NULL,
            passhash VARCHAR(255) NOT NULL
        );
        """
        create.execute(create_sql)
        

        