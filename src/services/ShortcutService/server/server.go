package server

import (
	"ShortCx/api"
	"ShortCx/models"
	"ShortCx/shortcut"
	"context"
	"log"
	"runtime"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// Server implements ShortcutService gRPC service
type Server struct {
	shortcut.UnimplementedShortcutServiceServer
	Store      models.ShortcutStore
	Sanitizier *Sanitizer
}

// NewServer returns a pointer to a new server with a given store
func NewServer(store models.ShortcutStore) *Server {
	return &Server{Store: store, Sanitizier: NewSanitizer()}
}

// Helper to return error with appropriate gRPC status
// Also logs function and location
func gRPCError(err error) error {
	_, fn, line, _ := runtime.Caller(1)
	log.Printf("[ERROR]: %s:%d %v", fn, line, err)
	errStatus, _ := status.FromError(err)
	return status.Errorf(errStatus.Code(), errStatus.Message())
}

// CreateShortcut handles CreateShortcutRequests forwarded from APIService
func (s *Server) CreateShortcut(ctx context.Context, request *shortcut.InternalCreateShortcutRequest) (*api.CreateShortcutResponse, error) {
	clean, err := s.Sanitizier.Sanitize(request.TargetUrl)
	if err != nil {
		return nil, status.Error(codes.InvalidArgument, err.Error())
	}
	newShortcut, err := s.Store.Create(request.AuthUserId, clean)
	if err != nil {
		return nil, gRPCError(err)
	}
	resp := &api.CreateShortcutResponse{Shortcut: newShortcut}
	return resp, nil
}

// DeleteShortcut handles DeleteShortcutRequests forwarded from APIService
func (s *Server) DeleteShortcut(ctx context.Context, request *shortcut.InternalDeleteShortcutRequest) (*api.DeleteShortcutResponse, error) {
	err := s.Store.Delete(request.AuthUserId, request.UrlToken)
	if err != nil {
		return nil, gRPCError(err)
	}
	resp := &api.DeleteShortcutResponse{Success: true}
	return resp, nil
}

// GetShortcut handles GetShortcutRequests forwarded from APIService
func (s *Server) GetShortcut(ctx context.Context, request *api.GetShortcutRequest) (*api.GetShortcutResponse, error) {
	target, err := s.Store.Get(request.UrlToken)
	if err != nil {
		return nil, gRPCError(err)
	}
	resp := &api.GetShortcutResponse{TargetUrl: target}
	return resp, nil
}

// GetAllShortcuts handles GetAllShortcutsRequests forwarded from APIService
func (s *Server) GetAllShortcuts(ctx context.Context, request *shortcut.InternalGetAllRequest) (*api.GetAllShortcutsResponse, error) {
	shortcuts, err := s.Store.GetAll(request.AuthUserId)
	if err != nil {
		return nil, gRPCError(err)
	}

	resp := &api.GetAllShortcutsResponse{Shortcuts: shortcuts}
	return resp, nil
}
