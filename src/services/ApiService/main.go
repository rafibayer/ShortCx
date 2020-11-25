package main

import (
	api "ShortCx/protos"
	"context"
)

type APIServiceServer struct {
	api.UnimplementedAPIServiceServer
}

func (s *APIServiceServer) CreateUser(ctx context.Context, request *api.CreateUserRequest) (*api.CreateUserResponse, error) {
	return nil, nil
}

func main() {

}
