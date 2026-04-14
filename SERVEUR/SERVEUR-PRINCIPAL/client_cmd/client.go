package main

import (
	"Server/p"
	"context"
	"log"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	succ, err := grpc.NewClient("localhost:8081", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("Erreur de la connexion au serveur: %v\n", err)
	}

	c := p.NewTrafiqServiceClient(succ)

	requete := p.InputUser{
		Ville: "Paris",
		Bus:   "1",
		Arret: "Châtelet",
	}

	reponse, err := c.GetInput(context.Background(), &requete)
	if err != nil {
		log.Fatalf("Erreur de transmissions de la DATA: %v\n", err)
	}
	log.Printf("TempsInitial: %v| TempsReel: %v", reponse.TempsInitial, reponse.TempsReel)

}
