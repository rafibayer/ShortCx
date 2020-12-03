package server

import (
	"ShortCx/api"
	"ShortCx/shortcut"
	"context"
)

// Server implements ShortcutService gRPC service
type Server struct {
	shortcut.UnimplementedShortcutServiceServer
}

// CreateShortcut handles CreateShortcutRequests forwarded from APIService
func (s *Server) CreateShortcut(ctx context.Context, request *api.CreateShortcutRequest) (*api.CreateShortcutResponse, error) {
	return nil, nil
}

// DeleteShortcut handles DeleteShortcutRequests forwarded from APIService
func (s *Server) DeleteShortcut(ctx context.Context, request *api.DeleteShortcutRequest) (*api.DeleteShortcutResponse, error) {
	return nil, nil
}

// GetShortcut handles GetShortcutRequests forwarded from APIService
func (s *Server) GetShortcut(ctx context.Context, request *api.GetShortcutRequest) (*api.GetShortcutResponse, error) {
	return nil, nil
}
