package server

import (
	"errors"
	"net/url"
	"strings"
)

func valid(urlInput string) bool {
	_, err := url.ParseRequestURI(urlInput)
	return err == nil
}

// Sanitize attempts to santize a given url.
// If the URL still cannot be parsed, return an error
func Sanitize(urlInput string) (string, error) {
	urlInput = strings.TrimSpace(urlInput)

	if !valid(urlInput) {
		withProtocol := "http://" + urlInput
		if !valid(withProtocol) {
			return "INVALID", errors.New("Invalid URL")
		}
		return withProtocol, nil
	}
	return urlInput, nil
}
