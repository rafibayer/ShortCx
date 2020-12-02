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
        private readonly IUserDataRepository _repository;
        private readonly UserController _controller;

        // Add data-access info to this constructor?
        public UserServiceImpl(ILogger<UserServiceImpl> logger, IUserDataRepository repository)
        {
            _logger = logger;
            _repository = repository;

            _controller = new UserController(repository);
        }

        public override Task<InternalCreateUserResponse> CreateUser(CreateUserRequest request, ServerCallContext context) 
        {
            try
            {
                _controller.CreateUser(request.Username, request.Password, request.PasswordConf);
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
