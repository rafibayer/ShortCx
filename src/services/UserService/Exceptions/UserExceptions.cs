using System;
using Grpc.Core;

namespace User.UserException
{
    class UserException: Exception
    {
        public readonly string message;
        public readonly StatusCode status;
        public UserException(string message, StatusCode status)
        {
            this.message = message;
            this.status = status;
        }
    }
}