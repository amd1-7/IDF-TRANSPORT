# Trafiq - Initiation Microservices & gRPC

## 📌 Objectif du Projet
Ce projet est une initiative personnelle visant à s'initier à l'architecture **microservices** et aux protocoles de communication modernes, plus précisément **gRPC** fonctionnant sur **HTTP/2.0**.

L'idée centrale est de faire communiquer un serveur principal en **Go** avec un microservice de traitement en **Python**. Les données exploitées (horaires de transport) servent de support concret pour valider les échanges de données entre les différents services.

## 🏗️ Architecture du Projet
Voici la structure actuelle du dépôt :

```text
.
├── LICENSE
├── SERVEUR
│   ├── MICROSERVICE (Backend Python)
│   │   ├── Engine.py
│   │   ├── __pycache__
│   │   ├── arrets-lignes.csv
│   │   ├── serveur.py
│   │   ├── test.py
│   │   ├── trafiq.proto
│   │   ├── trafiq_pb2.py
│   │   └── trafiq_pb2_grpc.py
│   └── SERVEUR-PRINCIPAL (Proxy Go)
│       ├── client_cmd
│       │   └── client.go
│       ├── go.mod
│       ├── go.sum
│       ├── p
│       │   ├── trafiq.pb.go
│       │   └── trafiq_grpc.pb.go
│       ├── serveur.go
│       └── trafiq.proto
└── requirements.txt
```
## Installation des dépendances via le fichier requirements
```bash
pip install -r requirements.txt
```
**Se placer dans le dossier du serveur principal**
```bash
cd SERVEUR/SERVEUR-PRINCIPAL
```

**Téléchargement des dépendances mentionnées dans le go.sum**
```bash
go get google.golang.org/grpc
go get google.golang.org/protobuf
go get golang.org/x/net
go mod tidy
```

# Utilisation
**Pour faire fonctionner l'ensemble, lancez les composants dans l'ordre suivant dans des terminaux séparés** :
```bash
cd SERVEUR/MICROSERVICE
python serveur.py
```

**Ensuite lancer le Serveur Principal Go (Port 8081)**:
```bash
cd SERVEUR/SERVEUR-PRINCIPAL
go run serveur.go
```

**Pour finir lancer le Client de test (Requête)**:
```bash
cd SERVEUR/SERVEUR-PRINCIPAL
go run client_cmd/client.go
```

## Licence & Conditions
Ce projet est sous **Licence MIT**.

Il est ouvert et peut être librement repris, modifié ou partagé. Toutefois, conformément aux termes de la licence, vous devez mentionner l'auteur original (moi-même) dans toute reprise du code ou du projet.

🔗 Contact
Retrouvez-moi sur GitHub pour suivre l'évolution de mes projets :
Retrouvez-moi sur GitHub : [amd1-7](https://github.com/amd1-7/)
