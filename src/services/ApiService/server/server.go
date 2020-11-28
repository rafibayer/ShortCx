package server

import (
	"context"

	api "github.com/rafibayer/ShortCx/api"
)

// Server implements APIService gRPC service
type Server struct {
	api.UnimplementedAPIServiceServer
	// More fields for other service clients (stubs/addresses/connections idk)
}

// CreateUser handles CreateUser requests, passing them to UserService
func (s *Server) CreateUser(ctx context.Context, request *api.CreateUserRequest) (*api.CreateUserResponse, error) {
	return &api.CreateUserResponse{AuthToken: "UNIMPLEMENTED AUTH"}, nil
}

// Login handles Login requests, passing them to AuthService
func (s *Server) Login(ctx context.Context, request *api.LoginRequest) (*api.LoginResponse, error) {
	return &api.LoginResponse{AuthToken: "UNIMPLEMENTED AUTH"}, nil
}

// Logout handles Logout requests, passing them to AuthService
func (s *Server) Logout(ctx context.Context, request *api.LogoutRequest) (*api.LogoutResponse, error) {
	return &api.LogoutResponse{Success: true}, nil
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
