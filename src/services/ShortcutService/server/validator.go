package server

import "net/url"

func validateURL(inputURL string) error {
	_, err := url.ParseRequestURI(inputURL)
	if err != nil {
		return err
	}
	return nil
}
