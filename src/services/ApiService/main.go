package main

import (
	"context"
	"log"
	"reflect"

	api "github.com/rafibayer/ShortCx/api"
)

type server struct {
	api.UnimplementedAPIServiceServer
}

func (s *server) CreateUser(ctx context.Context, in *api.CreateUserRequest) (*api.CreateUserResponse, error) {
	return nil, nil
}

func main() {
	//myvar := server{}

	log.Println(reflect.TypeOf(api.CreateUserRequest{}).NumMethod())

}
