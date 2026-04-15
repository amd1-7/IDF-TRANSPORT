package outils

import (
	"Server/p"
	"context"
)

func (s *Server) GetInput(ctx context.Context, input *p.InputUser) (*p.OutputServer, error) {
	response, err := ClientData(input.Arret, input.Bus, input.Ville)
	if err != nil {
		return nil, err
	}
	return &p.OutputServer{
		TempsInitial: response.TempsInitial,
		TempsReel:    response.TempsReel}, err
}
