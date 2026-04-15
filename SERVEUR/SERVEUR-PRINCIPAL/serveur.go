package main

import "Server/outils"

func main() {
	go outils.StartGRPC()
	outils.StartHTTP()
}
