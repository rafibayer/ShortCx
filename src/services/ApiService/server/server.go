package server

import (
	"ShortCx/api"
	"ShortCx/auth"
	"ShortCx/user"
	"context"

	"google.golang.org/grpc/status"
)

// Server implements APIService gRPC service
type Server struct {
	api.UnimplementedAPIServiceServer
	AuthClient auth.AuthServiceClient
	UserClient user.UserServiceClient
	// More fields for other service clients
}

// CreateUser handles CreateUser requests, passing them to UserService
func (s *Server) CreateUser(ctx context.Context, request *api.CreateUserRequest) (*api.CreateUserResponse, error) {
	internalCreateResp, err := s.UserClient.CreateUser(context.Background(), request)
	if err != nil {
		errStatus, _ := status.FromError(err)
		return nil, status.Errorf(errStatus.Code(), errStatus.Message())
	}

	// If user creation succeeded, make a session for the new user
	loginRequest := &api.LoginRequest{Username: internalCreateResp.Created, Password: request.Password}
	loginResponse, err := s.AuthClient.Login(context.Background(), loginRequest)
	if err != nil {
		errStatus, _ := status.FromError(err)
		return nil, status.Errorf(errStatus.Code(), errStatus.Message())
	}
	return &api.CreateUserResponse{AuthToken: loginResponse.AuthToken}, nil

}

// GetSession handles GetSession requests, passing them to AuthService
func (s *Server) GetSession(ctx context.Context, request *api.GetSessionRequest) (*api.GetSessionResponse, error) {
	resp, err := s.AuthClient.GetSession(context.Background(), request)
	if err != nil {
		// If there is an error from a downstream service, propagate it up
		errStatus, _ := status.FromError(err)
		return nil, status.Errorf(errStatus.Code(), errStatus.Message())
	}
	return resp, nil
}

// Login handles Login requests, passing them to AuthService
func (s *Server) Login(ctx context.Context, request *api.LoginRequest) (*api.LoginResponse, error) {
	resp, err := s.AuthClient.Login(context.Background(), request)
	if err != nil {
		// If there is an error from a downstream service, propagate it up
		errStatus, _ := status.FromError(err)
		return nil, status.Errorf(errStatus.Code(), errStatus.Message())
	}
	return resp, nil
}

// Logout handles Logout requests, passing them to AuthService
func (s *Server) Logout(ctx context.Context, request *api.LogoutRequest) (*api.LogoutResponse, error) {
	resp, err := s.AuthClient.Logout(context.Background(), request)
	if err != nil {
		// If there is an error from a downstream service, propagate it up
		errStatus, _ := status.FromError(err)
		return nil, status.Errorf(errStatus.Code(), errStatus.Message())
	}
	return resp, nil
}

// CreateShortcut handles CreateShortcut requests, passing them to ShortcutService
func (s *Server) CreateShortcut(ctx context.Context, request *api.CreateShortcutRequest) (*api.CreateShortcutResponse, error) {
	return &api.CreateShortcutResponse{UrlToken: "UNIMPLEMENTED URL"}, nil
}

// DeleteShortcut handles DeleteShortcut requests, passing them to ShortcutService
func (s *Server) DeleteShortcut(ctx context.Context, request *api.DeleteShortcutRequest) (*api.DeleteShortcutResponse, error) {
	return &api.DeleteShortcutResponse{Success: true}, nil
}

// GetShortcut handles GetShortcut requests, passing them to ShortcutService
func (s *Server) GetShortcut(ctx context.Context, request *api.GetShortcutRequest) (*api.GetShortcutResponse, error) {
	return &api.GetShortcutResponse{TargetUrl: "UNIMPLEMENTED URL"}, nil
}
