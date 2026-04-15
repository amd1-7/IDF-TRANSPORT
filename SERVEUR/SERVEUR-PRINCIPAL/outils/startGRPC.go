package outils

import (
	"Server/p"
	"log"
	"net"

	"google.golang.org/grpc"
)

type Server struct {
	p.UnimplementedTrafiqServiceServer
}

func StartGRPC() {
	succ, err := net.Listen("tcp", "0.0.0.0:8081")
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
