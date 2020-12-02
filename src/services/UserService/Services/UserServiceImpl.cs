using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Grpc.Core;
using Microsoft.Extensions.Logging;

namespace User
{
    public class UserServiceImpl: UserService.UserServiceBase
    {
        private readonly ILogger<UserServiceImpl> _logger;
        private UserController controller;

        // Add data-access info to this constructor?
        public UserServiceImpl(ILogger<UserServiceImpl> logger)
        {
            _logger = logger;
            
            // Get enviornment variables
            string dbAddr = Environment.GetEnvironmentVariable("DB_HOST");
            string dbUser = Environment.GetEnvironmentVariable("DB_USER");
            string dbPass = Environment.GetEnvironmentVariable("DB_PASS");
            string dbName = Environment.GetEnvironmentVariable("DB_NAME");
            string dbPort = Environment.GetEnvironmentVariable("DB_PORT");
            
            controller = new UserController(dbAddr, dbUser, dbPass, dbName, dbPort);
        }

        public override Task<InternalCreateUserResponse> CreateUser(CreateUserRequest request, ServerCallContext context) 
        {
            try
            {
                controller.CreateUser(request.Username, request.Password, request.PasswordConf);
                return Task.FromResult(new InternalCreateUserResponse
                {
                    Success = true
                });
            }
            catch (UserException.UserException e)
            {
                _logger.LogInformation(e, "Error encountered");
                throw new RpcException(new Status(e.status, e.message));
            }
            
        }
    }
}
