# IDF-TRANSPORT - Initiation Microservices & gRPC

## 📌 Objectif du Projet
Ce projet est une initiative personnelle visant à s'initier à l'architecture **microservices** et aux protocoles de communication modernes, plus précisément **gRPC** fonctionnant sur **HTTP/2.0**.

L'idée centrale est de faire communiquer un serveur principal en **Go** avec un microservice de traitement en **Python**. Les données exploitées (horaires de transport en ile de france) servent de support concret pour valider les échanges de données entre les différents services.

> ** Source des données :**
> Les données utilisées dans ce projet proviennent de **PRIM**, le portail Open Data d'Île-de-France Mobilités. Pour faire fonctionner l'application (notamment obtenir une clé API), il est nécessaire de se créer un compte sur [prim.iledefrance-mobilites.fr](https://prim.iledefrance-mobilites.fr/).
> Le fichier CSV contenant les arrêts de bus (`arrets-lignes.csv`) requis par le microservice Python peut être téléchargé ici : [Jeu de données : Arrêts et lignes associées](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets-lignes).


# 🏗️ Architecture du Projet
Voici la structure actuelle du dépôt :

```text
.
├── docker-compose.yml       # Orchestration des services
├── FRONTEND                 # Interface Utilisateur
│   ├── Dockerfile
│   ├── app.py
│   ├── isoFormat.py
│   └── recupererData.py
├── LICENSE
├── README.md
└── SERVEUR
    ├── MICROSERVICE (Backend Python) 
    │   ├── Dockerfile
    │   ├── Engine.py
    │   ├── arrets-lignes.csv
    │   ├── requirements.txt
    │   ├── serveur.py
    │   ├── test.py
    │   ├── trafiq.proto
    │   ├── trafiq_pb2.py
    │   └── trafiq_pb2_grpc.py
    └── SERVEUR-PRINCIPAL (Proxy Go)
        ├── Dockerfile
        ├── client_cmd
        │   └── client.go
        ├── go.mod
        ├── go.sum
        ├── outils
        │   ├── ClientData.go
        │   ├── ClientJsontoGrpc.go
        │   ├── GetInput.go
        │   ├── startGRPC.go
        │   └── startHTTP.go
        ├── p
        │   ├── trafiq.pb.go
        │   └── trafiq_grpc.pb.go
        ├── serveur.go
        └── trafiq.proto
```
# Installation des dépendances et lancement du serveur manuellement
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

## Utilisation
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

**Pour Lancer le Frontend**:
```bash
cd FRONTEND
python app.py
```
# Lancement centralisé avec Docker 
Grâce à Docker, le déploiement des serveurs est automatisé.

## Configurer l'environnement
Assurez-vous d'avoir un fichier .env à la racine contenant votre clé API si nécessaire (ex: API_KEY=votre_cle).

## Lancer les microservices
**Depuis la racine du projet, exécutez** :
```bash
docker compose up --build -d
```
Cette commande va construire et lancer le conteneur Python (port 1717) et le conteneur Go (ports 8080 et 8081) en arrière-plan.

## Lancer le client de test (depuis votre machine locale)
**Pour vérifier que les services communiquent bien, lancez le client Go qui va interroger le serveur principal sur le port 8081** :
```bash
go run SERVEUR/SERVEUR-PRINCIPAL/client_cmd/client.go
```
**Pour accéder au Frontend il suffit d'ouvrir cette url**:
```text
http://localhost:8501
```

## Mise en veille ou suppresion
**Pour supprimer les conteneurs** :
```bash
docker compose down
```

**Pour mettre en veille les conteneurs** :
```bash
docker compose stop
```

# Licence & Conditions
Ce projet est sous **Licence MIT**.

Il est ouvert et peut être librement repris, modifié ou partagé. Toutefois, conformément aux termes de la licence, vous devez mentionner l'auteur original (moi-même) dans toute reprise du code ou du projet.

🔗 Contact
Retrouvez-moi sur GitHub pour suivre l'évolution de mes projets :
Retrouvez-moi sur GitHub : [amd1-7](https://github.com/amd1-7/)
