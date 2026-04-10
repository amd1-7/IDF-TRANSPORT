import pandas as pd
import requests

class Engine:
    def __init__(self,arret,ville:str,bus):
        self.bus = bus

        self.ville = ville

        self.arret = arret
        
    def recuperer_données(self):
        data = pd.read_csv('arrets-lignes.csv',sep=';')

        filtres = ((data['stop_name'].str.lower().str.strip() == str(self.arret).lower().strip()) 
                   
                 & (data['nom_commune'].str.lower().str.strip() == str(self.ville).lower().strip()))

        data_trouvée = data.loc[filtres]

        if data_trouvée.empty:
            return 'Votre saisie est Incorrecte,veuillez redéfinir vos entrées'
        
        liste_colonne_importante = ['route_long_name','id',"mode",'nom_commune','code_insee','stop_lon','stop_lat']
        self.data = data_trouvée[liste_colonne_importante]

        return 'Recupération des données terminées'

        
