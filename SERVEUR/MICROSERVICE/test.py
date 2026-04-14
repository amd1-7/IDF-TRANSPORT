import grpc
import trafiq_pb2
import trafiq_pb2_grpc

def run():
    # 1. Créer le canal de communication vers le serveur
    with grpc.insecure_channel('localhost:1717') as channel:
        # 2. Créer le stub (le client)
        stub = trafiq_pb2_grpc.TrafiqServiceStub(channel)
        
        # 3. Préparer la requête
        requete = trafiq_pb2.InputUser(arret='Châteleffrt',ville='Paris',bus='1')
        
        # 4. Appeler le serveur
        try:
            reponse = stub.GetInput(requete)
            print(f"Réponse reçue : {reponse.temps_reel} (Prévu: {reponse.temps_initial})")
        except grpc.RpcError as e:
            print(f"Erreur gRPC : {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()