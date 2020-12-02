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
       
        private const int MIN_USERNAME_LENGTH = 4;
        private const int MAX_USERNAME_LENGTH = 20;
        private const int MIN_PASSWORD_LENGTH = 8;
        private const int MAX_PASSWORD_LENGTH = 50;

        public UserController(IUserDataRepository repository)
        {
            _repository = repository;
        }

        public void CreateUser(string username, string password, string passwordConf)
        {

            MySqlConnection conn = _repository.GetConnection();
            ValidateUser(username, password, passwordConf);
            string passHash = bc.HashPassword(password);

            string sql = "INSERT INTO users (username, created_at, passhash) VALUES(@username, NOW(), @passhash)";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            cmd.Parameters.AddWithValue("@username", username);
            cmd.Parameters.AddWithValue("@passhash", passHash);

            cmd.ExecuteNonQuery();
        }

        private bool UsernameAvailable(string username)
        {
            MySqlConnection conn = _repository.GetConnection();
            string sql = "SELECT COUNT(*) FROM users WHERE username=@username";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            cmd.Parameters.AddWithValue("@username", username);

            object result = cmd.ExecuteScalar();
            return Convert.ToInt32(result) == 0;
        }

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