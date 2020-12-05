package main

import (
	"database/sql"
	"fmt"
	"log"
	"net"
	"os"
	"time"

	"ShortCx/models"
	"ShortCx/server"
	"ShortCx/shortcut"

	"google.golang.org/grpc"
)

const retryDelay = 10
const maxRetries = 6

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

func pingRetry(conn *sql.DB) error {
	log.Println("Attemtping to reach database...")
	for i := 0; i < maxRetries; i++ {
		err := conn.Ping()
		if err == nil {
			log.Println("Success!")
			return nil
		}
		log.Printf("Error connecting to DB, retrying in %d sec: %v", retryDelay, err)
		time.Sleep(retryDelay * time.Second)
	}
	return fmt.Errorf("Failed to connect to dabatase after %d retries", maxRetries)
}

func main() {
	// Server listener
	log.Println("Trying to serve ShortcutService...")
	port := getenv("PORT", ":9092")
	lis, err := net.Listen("tcp", "0.0.0.0"+port)
	if err != nil {
		log.Fatalf("Failed to listen on port %s (%v)", port, err)
	}

	// Connect to Database
	dbUser := getenv("DB_USER", "root")
	dbPass := getenv("DB_PASS", "root")
	dbHost := getenv("DB_HOST", "database_svc")
	dbName := getenv("DB_NAME", "db")

	dsn := fmt.Sprintf("%s:%s@tcp(%s:3306)/%s", dbUser, dbPass, dbHost, dbName)
	// Create connection object
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		log.Fatalf("Failed to open sql connection: %v", err)
	}
	// Verify that connection is open
	err = pingRetry(db)
	if err != nil {
		log.Fatalf("Could not reach database: %v", err)
	}
	store := models.NewMySQLStore(db)

	// Serve ShortcutService server
	s := grpc.NewServer()
	shortcut.RegisterShortcutServiceServer(s, server.NewServer(store))
	log.Printf("Serving on port %s ...", port)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve on port %s (%v)", port, err)
	}
}
