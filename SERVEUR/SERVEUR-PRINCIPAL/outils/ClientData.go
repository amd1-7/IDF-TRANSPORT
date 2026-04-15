package outils

import (
	"Server/p"
	"context"
	"log"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func ClientData(arret string, bus string, ville string) (*p.OutputServer, error) {
	succ, err := grpc.NewClient("python-app:1717", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Printf("Erreur de communication entre microservice: %v\n", err)
	}

	c := p.NewTrafiqServiceClient(succ)

	requete := p.InputUser{
		Ville: ville,
		Bus:   bus,
		Arret: arret}

	reponse, err := c.GetInput(context.Background(), &requete)
	if err != nil {
		log.Printf("Erreur (non fatale) : %v", err)
	}

	return reponse, err
}
