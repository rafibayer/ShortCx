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

// getenv gets an environment variable value given a key or returns fallback and logs decision
func getenv(key string, fallback string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		log.Printf("Environment variable \"%s\" was not set, using fallback: \"%s\"", key, fallback)
		return fallback
	}
	log.Printf("Environment variable \"%s\" was set to: \"%s\" ", key, value)
	return value
}

func getAuthClient(authAddr string) auth.AuthServiceClient {
	var opts []grpc.DialOption
	opts = append(opts, grpc.WithInsecure())
	opts = append(opts, grpc.WithBlock())
	conn, err := grpc.Dial(authAddr, opts...)
	if err != nil {
		log.Fatalf("Failed to connect to AuthService: %v", err)
	}
	defer conn.Close()
	authClient := auth.NewAuthServiceClient(conn)
	return authClient
}

func main() {

	// Connect to AuthService
	authAddr := getenv("AUTH_ADDR", "auth_svc:9091")
	authClient := getAuthClient(authAddr)

	// Server listener
	port := getenv("PORT", ":9090")
	lis, err := net.Listen("tcp", "0.0.0.0"+port)
	if err != nil {
		log.Fatalf("Failed to listen on port %s (%v)", port, err)
	}

	// Serve APIService server
	s := grpc.NewServer()
	api.RegisterAPIServiceServer(s, &server.Server{AuthClient: authClient})
	log.Printf("Serving on port %s ...", port)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve on port %s (%v)", port, err)
	}
}
