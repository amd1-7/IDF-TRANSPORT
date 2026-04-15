package outils

import (
	"encoding/json"
	"log"
	"net/http"
)

type RequeteJson struct {
	Ville string `json:"ville"`
	Bus   string `json:"bus"`
	Arret string `json:"arret"`
}

type ReponseJson struct {
	Temps_reel    string `json:"temps_reel"`
	Temps_initial string `json:"temps_initial"`
}

func ClientJsontoGrpc(w http.ResponseWriter, r *http.Request) {
	var requete RequeteJson

	err := json.NewDecoder(r.Body).Decode(&requete)
	if err != nil {
		log.Fatalf("La requète n'a pas la structure json attendu...")
	}
	reponse, err := ClientData(requete.Arret, requete.Bus, requete.Ville)
	if err != nil {
		log.Fatalf("Erreur de la communication vers le serveur: %v\n", err)
	}
	w.Header().Set("Content-Type", "application/json")

	responseJson := ReponseJson{
		Temps_reel:    reponse.TempsReel,
		Temps_initial: reponse.TempsInitial,
	}

	encoder := json.NewEncoder(w)
	encoder.SetIndent("", "  ")

	if err := encoder.Encode(responseJson); err != nil {
		log.Fatalf("Erreur de récupération des données: %v\n", err)
	}
}
