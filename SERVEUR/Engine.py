import pandas as pd
import requests
from dotenv import load_dotenv
import os
from joblib import Memory

cache = "./cache"
mem = Memory(cache,verbose=0)

class Engine:
    def __init__(self,arret,ville:str,bus,api_key):
        self.bus = bus

        self.ville = ville

        self.arret = arret

        self.api_key = api_key
    @mem.cache   
    def recuperer_données(self):
        data = pd.read_csv('arrets-lignes.csv',sep=';',encoding='utf-8')

        filtres = (
                   (data['stop_name'].str.lower().str.strip() == str(self.arret).lower().strip()) 
                   
                 & (data['nom_commune'].str.lower().str.strip() == str(self.ville).lower().strip())
                 
                 & (data['route_long_name'].str.lower().str.strip() == str(self.bus).lower().strip())
                 )

        data_trouvée = data.loc[filtres]

        if data_trouvée.empty:
            return 'Votre saisie est Incorrecte,veuillez redéfinir vos entrées'
        
        liste_colonne_importante = ['route_long_name','id',"mode",'nom_commune','code_insee','stop_lon','stop_lat','stop_id']
        self.data = data_trouvée[liste_colonne_importante]

        return 'Recupération des données terminées'
    
    def recuperer_temps_reel(self):
        url = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring"

        lineRef = f'STIF:Line::{str(self.data['id'].iloc[0]).split(':')[-1]}:'
        stopRef = f'STIF:StopPoint:Q:{str(self.data['stop_id'].iloc[0]).split(':')[-1]}:'

        headers = {
        'apikey':self.api_key,
        }

        query = {
            'LineRef':lineRef,
            'MonitoringRef':stopRef
            }
        
        try:
            reponse = requests.get(url=url,headers=headers,params=query)
            reponse.raise_for_status()

            reponse_json = reponse.json()
            try:
                    delivery = reponse_json['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]
                    passages = delivery.get('MonitoredStopVisit', [])
            except (KeyError, IndexError):
                return "Erreur dans la structure de la réponse API."

            if not passages:
                return f"Aucun bus en temps réel pour l'arrêt {self.arret} pour le bus {self.bus}."

            passage01 = passages[0]
            infos_trajet01 = passage01['MonitoredVehicleJourney']['MonitoredCall']

            return {
                'Horaire initiale':infos_trajet01.get('AimedArrivalTime', 'Heure non communiquée'),
                'Horaire temps réel': infos_trajet01.get('ExpectedArrivalTime', 'Pas de prévision GPS')
                }
        except Exception as e:
            return f'Erreur requète: {e}'
        

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    bus23 = Engine(arret='Châtelet',ville='Paris',bus='1',api_key=api_key)

    print(bus23.recuperer_données())
    print(bus23.recuperer_temps_reel())