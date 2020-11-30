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

        // Add data-access info to this constructor?
        public UserServiceImpl(ILogger<UserServiceImpl> logger)
        {
            _logger = logger;
        }

        public override Task<CreateUserResponse> CreateUser(CreateUserRequest request, ServerCallContext context) 
        {
            Console.WriteLine($"Recieved CreateUserRequest {request.ToString()}");
            return Task.FromResult(new CreateUserResponse
            {
                AuthToken = "USER SERVICE UNIMPLEMENTED"
            });
        }
    }
}
