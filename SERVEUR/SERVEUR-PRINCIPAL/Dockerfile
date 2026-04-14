FROM golang:1.26-alpine

WORKDIR /App

COPY SERVEUR/SERVEUR-PRINCIPAL/go.mod SERVEUR/SERVEUR-PRINCIPAL/go.sum ./

RUN go mod download

COPY SERVEUR/SERVEUR-PRINCIPAL/ .

RUN go build -o main serveur.go

RUN chmod +x main

CMD [ "./main" ]
