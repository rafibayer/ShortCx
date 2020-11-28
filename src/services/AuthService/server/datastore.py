import exceptions
import mysql.connector
import time
import logging


RETRY_DELAY=10
MAX_RETRIES=10

class DataStore:

    def __init__(self, db_host: str, db_user: str, db_pass: str, db_name: str):
        """Creates a new DataStore object

        Args:
            db_host (str): Database host
            db_user (str): Database username
            db_pass (str): Database password
            db_name (str): Database db name
        """
        logging.info(f'Tying to connect to db: {db_user}@{db_host}:{db_pass} ({db_name=})')
        self._connect_with_retries(db_host, db_user, db_pass, db_name)

        logging.info('Attempting to initialize users table')
        self._db_init()

    def get_credentials(self, email: str) -> str:
        """Get credentials for a given email

        Args:
            email (str): User email

        Raises:
            exceptions.BadCredentialsError: User/email not found

        Returns:
            str: passhash associated with given email
        """
        select = self.database.cursor()
        sel_sql = 'SELECT passhash FROM users WHERE email=%s'
        select.execute(sel_sql, (email, ))
        result = select.fetchone()
        if result is None:
            raise exceptions.BadCredentialsError()
        
        return result

    def _connect_with_retries(self, db_host, db_user, db_pass, db_name):
        """Connect to the database with retries

        Args:
            db_host (str): Database host
            db_user (str): Database username
            db_pass (str): Database password
            db_name (str): Database db name

        Raises:
            ConnectionError: Connection could not be established after MAX_RETRIES attempts
        """
        tries = 0
        while tries < MAX_RETRIES:
            try:
                self.database = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_pass,
                    auth_plugin='mysql_native_password',
                    database=db_name)
                logging.info(f'Connection succeeded!')
                return
            except Exception as e:
                logging.warn(f'Connection failed: \n\t{e}\n\tRetrying in {RETRY_DELAY} sec...')
                time.sleep(RETRY_DELAY)
                tries += 1

        logging.CRITICAL(f'DB failed to connect after {MAX_RETRIES} attempts ...')
        raise ConnectionError()

    def _db_init(self):
        """Initializes all required tables for DataStore
        """
        create = self.database.cursor()
        create_sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            username VARCHAR(255) NOT NULL UNIQUE,
            created_at DATE NOT NULL,
            passhash VARCHAR(255) NOT NULL
        );
        """
        create.execute(create_sql)
        self.database.commit()
        

        