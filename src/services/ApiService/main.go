package main

import (
	"log"
	"net"
	"os"

	"github.com/rafibayer/ShortCx/api"
	server "github.com/rafibayer/ShortCx/server"
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
	PORT := getenv("PORT", ":9090")
	lis, err := net.Listen("tcp", "localhost"+PORT)
	if err != nil {
		log.Fatalf("Failed to listen on port %s (%v)", PORT, err)
	}
	s := grpc.NewServer()
	api.RegisterAPIServiceServer(s, &server.Server{ /* Inject service addresses here later */ })
	log.Printf("Serving on port %s ...", PORT)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve on port %s (%v)", PORT, err)
	}
}
