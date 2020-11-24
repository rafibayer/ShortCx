package main

import (
	"context"

	pb "github.com/rafibayer/ShortCx/src/services/ApiService/protos"
)

type ApiServiceServer struct {
	pb.UnimplementedAPIServiceServer
}

func (s *ApiServiceServer) CreateUser(ctx context.Context, request *CreateUserRequest) (*CreateUserResponse, error) {

}
