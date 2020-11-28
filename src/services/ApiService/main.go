package main

import (
	"log"
	"net"
	"os"

	"ShortCx/api"
	auth "ShortCx/auth"
	server "ShortCx/server"

	"google.golang.org/grpc"
)

// getenv gets an enviornment variable value given a key or returns fallback and logs if empty
func getenv(key string, fallback string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		log.Printf("Env key %s was not set, using fallback value \"%s\"", key, fallback)
		return fallback
	}
	return value
}

func main() {

	// Connect to AuthService
	authAddr := getenv("AUTH_ADDR", "auth_svc:9091")
	var opts []grpc.DialOption
	opts = append(opts, grpc.WithInsecure())
	opts = append(opts, grpc.WithBlock())
	conn, err := grpc.Dial(authAddr, opts...)
	if err != nil {
		log.Fatalf("Failed to connect to AuthService: %v", err)
	}
	defer conn.Close()
	authClient := auth.NewAuthServiceClient(conn)

	// Service APIService
	port := getenv("PORT", ":9090")
	lis, err := net.Listen("tcp", "localhost"+port)
	if err != nil {
		log.Fatalf("Failed to listen on port %s (%v)", port, err)
	}
	s := grpc.NewServer()
	api.RegisterAPIServiceServer(s, &server.Server{AuthClient: authClient})
	log.Printf("Serving on port %s ...", port)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve on port %s (%v)", port, err)
	}
}
