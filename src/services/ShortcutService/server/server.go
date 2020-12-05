package server

import (
	"ShortCx/api"
	"ShortCx/models"
	"ShortCx/shortcut"
	"context"
	"log"
	"regexp"
	"runtime"
	"strings"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

const urlRegex = `^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$`

// Server implements ShortcutService gRPC service
type Server struct {
	shortcut.UnimplementedShortcutServiceServer
	Store     models.ShortcutStore
	validator *regexp.Regexp
}

// NewServer returns a pointer to a new server with a given store
func NewServer(store models.ShortcutStore) *Server {
	return &Server{
		Store:     store,
		validator: regexp.MustCompile(urlRegex),
	}
}

func gRPCError(err error) error {
	_, fn, line, _ := runtime.Caller(1)
	log.Printf("[ERROR]: %s:%d %v", fn, line, err)
	errStatus, _ := status.FromError(err)
	return status.Errorf(errStatus.Code(), errStatus.Message())
}

// CreateShortcut handles CreateShortcutRequests forwarded from APIService
func (s *Server) CreateShortcut(ctx context.Context, request *shortcut.InternalCreateShortcutRequest) (*api.CreateShortcutResponse, error) {
	clean := strings.TrimSpace(request.TargetUrl)
	if !s.validator.MatchString(clean) {
		return nil, status.Error(codes.InvalidArgument, "Invalid URL")
	}
	token, err := s.Store.Create(request.AuthUserId, clean)
	if err != nil {
		return nil, gRPCError(err)
	}
	resp := &api.CreateShortcutResponse{UrlToken: token}
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
