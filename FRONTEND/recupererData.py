import requests

def RecupererData(bus:str,ville:str,arret:str):
    try:
        body = {
            "bus":bus,
            "ville":ville,
            "arret":arret
            }
        requete = requests.post(url="http://go-app:8080/temps",json=body)
        requete.raise_for_status()
        
        return requete.json()
    except Exception as e:
        return f"Erreur lors de la communication au serveur: {e}\n"