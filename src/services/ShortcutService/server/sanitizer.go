package server

import (
	"errors"
	"net/url"
	"regexp"
	"strings"
)

// Sanitizer attempts to sanitize a URL
type Sanitizer struct {
	hostValidator *regexp.Regexp
}

// NewSanitizer creates a new Sanitizer instance with compiled regex
func NewSanitizer() *Sanitizer {
	return &Sanitizer{hostValidator: regexp.MustCompile(`[A-Za-z0-9]+\.[A-Za-z]+$`)}
}

func (s *Sanitizer) valid(urlInput string) bool {
	u, err := url.ParseRequestURI(urlInput)
	// If there is an error, statement will short-circuit before derefrencing null var u
	return err == nil && u.Host != "" && s.hostValidator.MatchString(u.Host)
}

// Sanitize attempts to santize a given url.
// If the URL still cannot be parsed, return an error
func (s *Sanitizer) Sanitize(urlInput string) (string, error) {
	urlInput = strings.TrimSpace(urlInput)

	if !s.valid(urlInput) {
		withProtocol := "http://" + urlInput
		if !s.valid(withProtocol) {
			return "INVALID", errors.New("Invalid URL")
		}
		return withProtocol, nil
	}
	return urlInput, nil
}
