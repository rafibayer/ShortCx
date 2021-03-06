import exceptions
import mysql.connector
import time
import logging


RETRY_DELAY=10
MAX_RETRIES=10

class User:
    def __init__(self, user_id, username, created_at, passhash):
        self.user_id = user_id
        self.username = username
        self.created_at = created_at
        self.passhash = passhash
    
    @classmethod
    def from_row(cls, row):
        return cls(*row)


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

    def get_user(self, username: str) -> User:
        """Get credentials for a given username

        Args:
            username (str): Username

        Raises:
            exceptions.BadCredentialsError: User not found

        Returns:
            str: passhash associated with given username
        """
        self.database.start_transaction()
        select = self.database.cursor()
        sel_sql = 'SELECT * FROM users WHERE username=%s'
        select.execute(sel_sql, (username, ))
        result = select.fetchone()
        if result is None:
            self.database.rollback()
            raise exceptions.BadCredentialsError()
        
        self.database.commit()
        return User.from_row(result)

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