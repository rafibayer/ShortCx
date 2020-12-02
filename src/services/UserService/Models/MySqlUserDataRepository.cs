using System;
using System.Threading;
using MySql.Data;
using MySql.Data.MySqlClient;

namespace User
{
    class MySqlUserDataRepository: IUserDataRepository
    {
        private MySqlConnection _connection;
        private const int RETRY_DELAY_SEC = 5;
        private const int MAX_RETRIES = 12;

        public MySqlUserDataRepository()
        {
             // Get enviornment variables
            string dbAddr = Environment.GetEnvironmentVariable("DB_HOST");
            string dbUser = Environment.GetEnvironmentVariable("DB_USER");
            string dbPass = Environment.GetEnvironmentVariable("DB_PASS");
            string dbName = Environment.GetEnvironmentVariable("DB_NAME");
            string dbPort = Environment.GetEnvironmentVariable("DB_PORT");

            // Build connection string and connect
            string connStr = $"Server={dbAddr};Port={dbPort};Database={dbName};Uid={dbUser};Pwd={dbPass}";
            Console.WriteLine($"Trying to connect to MySqlDB: {connStr}");
            _connection = ConnectWithRetries(connStr);
        }

        public MySqlConnection GetConnection()
        {
            return _connection;
        }

        private MySqlConnection ConnectWithRetries(string connStr)
        {
            MySqlConnection conn = new MySqlConnection(connStr);
            int tries = 0;
            while (tries < MAX_RETRIES)
            {
                try
                {
                    conn.Open();
                    Console.WriteLine("Success!");
                    return conn;
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Failed to connect to database, trying again in {RETRY_DELAY_SEC} sec:\n\t{e}");
                    Thread.Sleep(RETRY_DELAY_SEC*1000);
                }
                tries++;
            }
            throw new TimeoutException($"Failed to connect to DB after {MAX_RETRIES} retries...");
        }
    }
}