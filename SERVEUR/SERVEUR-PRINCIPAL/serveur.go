package main

import (
	"Server/p"
	"context"
	"log"
	"net"
	"net/http"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

type Server struct {
	p.UnimplementedTrafiqServiceServer
}

func (s *Server) GetInput(ctx context.Context, input *p.InputUser) (*p.OutputServer, error) {
	response, err := ClientData(input.Arret, input.Bus, input.Ville)
	if err != nil {
		return nil, err
	}
	return &p.OutputServer{
		TempsInitial: response.TempsInitial,
		TempsReel:    response.TempsReel}, err
}

func startGRPC() {
	succ, err := net.Listen("tcp", ":8081")
	if err != nil {
		log.Fatalf("Erreur d'initialisation du serveurserveur: %v\n", err)
	}

	grpcServer := grpc.NewServer()

	serverGrpc := Server{}
	p.RegisterTrafiqServiceServer(grpcServer, &serverGrpc)

	log.Printf("Serveur gRPC lancé sur le port 8081...\n")

	if err := grpcServer.Serve(succ); err != nil {
		log.Fatalf("Erreur serveur: %v\n", err)
	}
}

func startHTTP() {
	mux := http.NewServeMux()

	log.Printf("Serveur HTTP lancé sur le port 8080...\n")
	if err := http.ListenAndServe(":8080", mux); err != nil {
		log.Fatalf("Erreur serveur HTTP: %v\n", err)
	}
}

func ClientData(arret string, bus string, ville string) (*p.OutputServer, error) {
	succ, err := grpc.NewClient(":1717", grpc.WithTransportCredentials(insecure.NewCredentials()))
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

func main() {
	go startGRPC()
	startHTTP()
}
