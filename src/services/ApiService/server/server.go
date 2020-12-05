package server

import (
	"ShortCx/api"
	"ShortCx/auth"
	"ShortCx/shortcut"
	"ShortCx/user"
	"context"
	"log"
	"runtime"

	"google.golang.org/grpc/status"
)

// Server implements APIService gRPC service
type Server struct {
	api.UnimplementedAPIServiceServer
	AuthClient     auth.AuthServiceClient
	ShortcutClient shortcut.ShortcutServiceClient
	UserClient     user.UserServiceClient
	// More fields for other service clients
}

func gRPCError(err error) error {
	_, fn, line, _ := runtime.Caller(1)
	log.Printf("[ERROR]: %s:%d %v", fn, line, err)
	errStatus, _ := status.FromError(err)
	return status.Errorf(errStatus.Code(), errStatus.Message())
}

// Factored out to share between any request that requires auth
func (s *Server) getSession(authToken string) (*api.GetSessionResponse, error) {
	request := &api.GetSessionRequest{AuthToken: authToken}
	resp, err := s.AuthClient.GetSession(context.Background(), request)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}

// CreateUser handles CreateUser requests, passing them to UserService
func (s *Server) CreateUser(ctx context.Context, request *api.CreateUserRequest) (*api.CreateUserResponse, error) {
	internalCreateResp, err := s.UserClient.CreateUser(context.Background(), request)
	if err != nil {
		return nil, gRPCError(err)
	}

	// If user creation succeeded, make a session for the new user
	loginRequest := &api.LoginRequest{Username: internalCreateResp.Created, Password: request.Password}
	loginResponse, err := s.AuthClient.Login(context.Background(), loginRequest)
	if err != nil {
		return nil, gRPCError(err)
	}
	return &api.CreateUserResponse{AuthToken: loginResponse.AuthToken}, nil
}

// GetSession handles GetSession requests, passing them to AuthService
func (s *Server) GetSession(ctx context.Context, request *api.GetSessionRequest) (*api.GetSessionResponse, error) {
	resp, err := s.AuthClient.GetSession(context.Background(), request)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}

// Login handles Login requests, passing them to AuthService
func (s *Server) Login(ctx context.Context, request *api.LoginRequest) (*api.LoginResponse, error) {
	resp, err := s.AuthClient.Login(context.Background(), request)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}

// Logout handles Logout requests, passing them to AuthService
func (s *Server) Logout(ctx context.Context, request *api.LogoutRequest) (*api.LogoutResponse, error) {
	resp, err := s.AuthClient.Logout(context.Background(), request)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}

// CreateShortcut handles CreateShortcut requests, passing them to ShortcutService
func (s *Server) CreateShortcut(ctx context.Context, request *api.CreateShortcutRequest) (*api.CreateShortcutResponse, error) {

	sessionState, err := s.getSession(request.AuthToken)
	if err != nil {
		return nil, gRPCError(err)
	}

	internalCreate := &shortcut.InternalCreateShortcutRequest{
		AuthUserId: sessionState.UserId,
		TargetUrl:  request.TargetUrl,
	}

	resp, err := s.ShortcutClient.CreateShortcut(context.Background(), internalCreate)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}

// DeleteShortcut handles DeleteShortcut requests, passing them to ShortcutService
func (s *Server) DeleteShortcut(ctx context.Context, request *api.DeleteShortcutRequest) (*api.DeleteShortcutResponse, error) {
	sessionState, err := s.getSession(request.AuthToken)
	if err != nil {
		return nil, gRPCError(err)
	}

	internalDelete := &shortcut.InternalDeleteShortcutRequest{
		AuthUserId: sessionState.UserId,
		UrlToken:   request.UrlToken,
	}

	resp, err := s.ShortcutClient.DeleteShortcut(context.Background(), internalDelete)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}

// GetShortcut handles GetShortcut requests, passing them to ShortcutService
func (s *Server) GetShortcut(ctx context.Context, request *api.GetShortcutRequest) (*api.GetShortcutResponse, error) {
	resp, err := s.ShortcutClient.GetShortcut(context.Background(), request)
	if err != nil {
		return nil, gRPCError(err)
	}
	return resp, nil
}
