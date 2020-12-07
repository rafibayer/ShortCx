package models

import (
	"ShortCx/api"
	"database/sql"
	"log"
	"math/rand"
	"time"

	// MySQL Driver
	_ "github.com/go-sql-driver/mysql"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// Database col is currently VARCHAR(32), so we can increases this if needed
const tokenLength = 8
const tokenChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

var randomizer *rand.Rand = rand.New(rand.NewSource(time.Now().UnixNano()))

// MySQLStore implements the ShortcutStore interface
type MySQLStore struct {
	db *sql.DB
}

// NewMySQLStore creates a instance with a given database connection
func NewMySQLStore(db *sql.DB) *MySQLStore {
	return &MySQLStore{db}
}

func (store *MySQLStore) incVisits(urlToken string) {
	updq := "UPDATE shortcuts SET visits = visits + 1 WHERE token=?"
	res, err := store.db.Exec(updq, urlToken)
	if err != nil {
		log.Printf("Could not increment vists for shortcut: %s: %v", urlToken, err)
		return
	}
	aff, err := res.RowsAffected()
	if err != nil {
		log.Printf("Could not get rows affected visits increment: %s: %v", urlToken, err)
		return
	}
	if aff != 1 {
		log.Printf("Tried to increment vists for non-existant shortcut: %s", urlToken)
		return
	}
}

// Create inserts a new Shortcut into the database and returns the generated url_token
func (store *MySQLStore) Create(userID int32, targetURL string) (string, error) {
	insq := "INSERT INTO shortcuts (user_id, token, target_url, created_at, visits) VALUES (?, ?, ?, NOW(), 0)"
	token := generateToken()
	_, err := store.db.Exec(insq, userID, token, targetURL)
	if err != nil {
		log.Printf("Encountered error on insert: %v", err)
		return "ERROR", err
	}
	return token, nil
}

// Delete removes a shortcut from the database
func (store *MySQLStore) Delete(userID int32, urlToken string) error {
	delq := "DELETE FROM shortcuts WHERE user_id = ? AND token = ?"
	res, err := store.db.Exec(delq, userID, urlToken)
	if err != nil {
		log.Printf("Encountered error on delete: %v", err)
		return status.Error(codes.Internal, "Internal Error")
	}
	count, err := res.RowsAffected()
	if err != nil {
		log.Printf("Encountered error determining rows affected: %v", err)
		return status.Error(codes.Internal, "Internal Error")
	}
	if count != 1 {
		return status.Error(codes.NotFound, "Shortcut Does Not Exist")
	}
	return nil
}

// Get returns the target_url of a shortcut from the database given a urlToken
// Also increments vists in a go routine
func (store *MySQLStore) Get(urlToken string) (string, error) {
	getq := "SELECT target_url FROM shortcuts WHERE token=?"
	var result string
	err := store.db.QueryRow(getq, urlToken).Scan(&result)
	if err != nil {
		log.Printf("Error getting result: %v", err)
		return "ERROR", status.Error(codes.NotFound, "Shortcut Does Not Exist")
	}
	defer store.incVisits(urlToken)
	return result, nil
}

// GetAll returns ShortcutDetails for all shortcuts of a given user (by userID)
func (store *MySQLStore) GetAll(userID int32) ([]*api.ShortcutDetail, error) {
	getaq := "SELECT token, target_url, created_at, visits FROM shortcuts WHERE user_id=?"
	rows, err := store.db.Query(getaq, userID)
	if err != nil {
		log.Printf("Error getting all: %v", err)
		return nil, err
	}
	defer rows.Close()

	var result []*api.ShortcutDetail
	for rows.Next() {
		cur := &api.ShortcutDetail{}
		err := rows.Scan(&cur.UrlToken, &cur.TargetUrl, &cur.CreatedAt, &cur.Visits)
		if err != nil {
			return nil, err
		}
		result = append(result, cur)
	}

	return result, nil

}

func generateToken() string {
	bytes := make([]byte, tokenLength)
	for i := range bytes {
		bytes[i] = tokenChars[randomizer.Intn(len(tokenChars))]
	}
	return string(bytes)
}
