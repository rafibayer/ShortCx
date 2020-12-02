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

        /// <summary>
        /// gRPC UserService Implementation
        /// </summary>
        /// <param name="logger">ILogger</param>
        /// <param name="repository">IUserDataRepository Implementation</param>
        public UserServiceImpl(ILogger<UserServiceImpl> logger, IUserDataRepository repository)
        {
            _logger = logger;
            _repository = repository;
            _controller = new UserController(repository);
        }

        /// <summary>
        /// UserService CreateUser rpc Implementation
        /// </summary>
        /// <param name="request">UserCreationRequest</param>
        /// <param name="context">gRPC call context</param>
        /// <returns>InteralCreateUserResponse for APIService</returns>
        public override Task<InternalCreateUserResponse> CreateUser(CreateUserRequest request, ServerCallContext context) 
        {
            try
            {
                string created = _controller.CreateUser(request.Username, request.Password, request.PasswordConf);
                return Task.FromResult(new InternalCreateUserResponse
                {
                    Created = created
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
