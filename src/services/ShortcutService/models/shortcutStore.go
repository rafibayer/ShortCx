package models

// ShortcutStore is an interface for interacting with shortcuts
type ShortcutStore interface {
	// Create creates a new shortcut to a targetUrl for a user
	Create(userID int32, targetURL string) (string, error)
	// Delete deletes a shortcut described by a userId and the urlToken
	Delete(userID int32, urlToken string) error
	// Get retrieves the targetUrl of a shortcut described by a urlToken
	Get(urlToken string) (string, error)
}
