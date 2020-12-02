using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Grpc.Core;
using MySql.Data;
using MySql.Data.MySqlClient;
using bc = BCrypt.Net.BCrypt;

namespace User
{
    class UserController
    {
        private IUserDataRepository _repository;
       
        /// <summary>
        /// Username and password validation parameters
        /// </summary>
        private const int MIN_USERNAME_LENGTH = 4;
        private const int MAX_USERNAME_LENGTH = 20;
        private const int MIN_PASSWORD_LENGTH = 8;
        private const int MAX_PASSWORD_LENGTH = 50;

        /// <summary>
        /// Create a new UserController
        /// </summary>
        /// <param name="repository">Data Access</param>
        public UserController(IUserDataRepository repository)
        {
            _repository = repository;
        }

        /// <summary>
        /// Validates and inserts a new user into the database
        /// </summary>
        /// <param name="username">New username (unsanitized)</param>
        /// <param name="password">New password</param>
        /// <param name="passwordConf">New password confirmation</param>
        /// <returns>Created user's username after sanitization</returns>
        /// <exception cref="UserException.UserException">Thrown if username or password is invalid</exception>
        public string CreateUser(string username, string password, string passwordConf)
        {
            username = SanitizeUsername(username);
            MySqlConnection conn = _repository.GetConnection();
            ValidateUser(username, password, passwordConf);
            string passHash = bc.HashPassword(password);

            string sql = "INSERT INTO users (username, created_at, passhash) VALUES(@username, NOW(), @passhash)";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            cmd.Parameters.AddWithValue("@username", username);
            cmd.Parameters.AddWithValue("@passhash", passHash);

            cmd.ExecuteNonQuery();
            return username;
        }

        /// <summary>
        /// Queries database to check if username is available
        /// </summary>
        /// <param name="username">New username</param>
        /// <returns>true if available</returns>
        private bool UsernameAvailable(string username)
        {
            MySqlConnection conn = _repository.GetConnection();
            string sql = "SELECT COUNT(*) FROM users WHERE username=@username";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            cmd.Parameters.AddWithValue("@username", username);

            object result = cmd.ExecuteScalar();
            return Convert.ToInt32(result) == 0;
        }

        /// <summary>
        /// Sanitizes username
        /// </summary>
        /// <param name="username">New username</param>
        /// <returns>Sanitized username</returns>
        private string SanitizeUsername(string username)
        {
            return username.Trim();
        }

        /// <summary>
        /// Validates username and password
        /// </summary>
        /// <param name="username"></param>
        /// <param name="password"></param>
        /// <param name="passwordConf"></param>
        /// <exception cref="UserException.UserException">Thrown if username or password is invalid</exception>
        private void ValidateUser(string username, string password, string passwordConf)
        {
            if (username.Length > MAX_USERNAME_LENGTH)
            {
                throw new UserException.UserException(
                    $"Username cannot excede {MAX_USERNAME_LENGTH} characters",
                    StatusCode.InvalidArgument);
            }
            if (username.Length < MIN_USERNAME_LENGTH)
            {
                throw new UserException.UserException(
                    $"Username must be at least {MIN_USERNAME_LENGTH} characters",
                    StatusCode.InvalidArgument);
            }

            if (password.Length < MIN_PASSWORD_LENGTH)
            {
                throw new UserException.UserException(
                    $"Password must be at least {MIN_PASSWORD_LENGTH} characters",
                    StatusCode.InvalidArgument);
            }

            if (password.Length > MAX_PASSWORD_LENGTH)
            {
                throw new UserException.UserException(
                    $"Password cannot excede {MAX_PASSWORD_LENGTH} characters",
                    StatusCode.InvalidArgument);
            }

            if (!password.Equals(passwordConf))
            {
                throw new UserException.UserException(
                    $"Passwords Do Not Match",
                    StatusCode.InvalidArgument);
            }

            if (!UsernameAvailable(username))
            {
                throw new UserException.UserException(
                    "Username Is Already Taken",
                    StatusCode.AlreadyExists);
            }
        }
    }
}