package main

import (
	"log"
	"net"
	"os"

	"ShortCx/server"
	"ShortCx/shortcut"

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

func main() {
	// Server listener
	log.Println("Trying to serve ShortcutService...")
	port := getenv("PORT", ":9092")
	lis, err := net.Listen("tcp", "0.0.0.0"+port)
	if err != nil {
		log.Fatalf("Failed to listen on port %s (%v)", port, err)
	}

	// Serve APIService server
	s := grpc.NewServer()
	shortcut.RegisterShortcutServiceServer(s, &server.Server{})
	log.Printf("Serving on port %s ...", port)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve on port %s (%v)", port, err)
	}
}
