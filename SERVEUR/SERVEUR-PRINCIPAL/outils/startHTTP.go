package outils

import (
	"log"
	"net/http"
)

func StartHTTP() {
	mux := http.NewServeMux()

	mux.HandleFunc("/temps", ClientJsontoGrpc)

	log.Printf("Serveur HTTP lancé sur le port 8080...\n")
	if err := http.ListenAndServe("0.0.0.0:8080", mux); err != nil {
		log.Fatalf("Erreur serveur HTTP: %v\n", err)
	}
}
