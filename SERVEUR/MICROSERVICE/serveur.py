import grpc
from concurrent import futures
import trafiq_pb2
import trafiq_pb2_grpc
from Engine import Engine
import os
from dotenv import load_dotenv
import traceback


load_dotenv()

class Greeter(trafiq_pb2_grpc.TrafiqServiceServicer):
    def GetInput(self, requete, context):
        # 1. PHASE DE LOGIQUE (On attrape les vrais bugs ici)
        try:
            requeteClient = Engine(
                ville=requete.ville, 
                bus=requete.bus, 
                arret=requete.arret, 
                api_key=os.getenv("API_KEY")
            )
            status = requeteClient.recuperer_données()
        except Exception as e:
            traceback.print_exc()
            context.abort(grpc.StatusCode.INTERNAL, f"Erreur logique : {str(e)}")

        if "Incorrecte" in status:
            return None,context.abort(grpc.StatusCode.NOT_FOUND, status)

        # 3. PHASE D'APPEL API
        try:
            resultat = requeteClient.recuperer_temps_reel()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, f"Erreur API : {str(e)}")

        if isinstance(resultat, dict):
            return trafiq_pb2.OutputServer(
                temps_reel=resultat.get("Horaire temps réel", "N/A"),
                temps_initial=resultat.get("Horaire initiale", "N/A")
            )
        else:
            context.abort(grpc.StatusCode.INTERNAL, resultat)
    
def startServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    trafiq_pb2_grpc.add_TrafiqServiceServicer_to_server(servicer=Greeter(),server=server)

    server.add_insecure_port('[::]:1717')
    print("Démarage du serveur GRPC sur le port 1717...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    startServer()
