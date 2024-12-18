


# 22410567 Mahamat ABDRAMAN
# 22409612 Adami ABDOURAHAMANE CHEGOU
# 22409616 Uriel ADOTANOU

#Références: 

 # cours

 

 # Erreurs et Exception en python(https://docs.python.org/fr/3.5/tutorial/errors.html)

 #Documentation Graph: https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis

 #API Découpage administratif: https://geo.api.gouv.fr/decoupage-administratif




# Section 1 : les imports
import requests
from graphh import GraphHopper
import json
from pprint import pprint
import numpy as np
import pandas as pd














#Section 2 : fonctions


#recuperation de données communes

def données_communes(url,code_departement=[35,53,22,72,23]):
    
    list_communes=[]
    # Nous allons malheureusement devoir envoyer une requête pour chaque département,
    # car l'API ne permet pas de donner plusieurs valeurs au paramètre 'codeDepartement'.

    for code in code_departement:
        #definri les parmètre à mettre dans la requetes, fields et  les codes departement pour filtrer(pour ne recuperer que ce que nous intersse)
        params = {
            "codeDepartement": code,
            "fields": "nom,code,codeDepartement,population,centre",
           
        }
        #on va utiliser un bloc try et except pour capturer des evantuelles erreurs de réseau qui empêchent la requête d'atteindre le serveur
        
        try:
            reponse=requests.get(url,params)
            # Vérification si le statut de la réponse est un succès (200) et que les données JSON existent
            if reponse.status_code==200 and reponse.json():
                print("recupération reussie pour le departement :",code)
                communes=reponse.json()
                 


                #on va filtrer pour ne garder que les communes de plus de 20000 habitants(on a pas non plus la possiblité de mettre cette conditon dans les parametres lors de l'envoie des requêtes)
                departement_filtré=[commune for commune in communes if commune["population"]>=20000]

                
                #on verifie si le departement n'est pas vide et que la clef  n'est pas déjà renseignée, si c'est pas le cas, on insère le depatement dans le dict  

                if departement_filtré not in list_communes and departement_filtré:
                    list_communes.append(departement_filtré)
            else:
                print("il y a une erreur au niveau du departement : ",code)
                
        except requests.RequestException as erreur:
            print("une erreur de connexion: ",erreur)
            
    return list_communes



#recuperartion de adresses des amis 

def adresses_amis(url):
    

    #pareil un bloc try et except pour capturer des evantuelles erreurs
    try:
        reponse=requests.get(url)

        if reponse.status_code==200 and reponse.json():

            print("adresse des amis recuperées avec succès")
            adresses=reponse.json()
        
    except requests.RequestException as erreur:
        print("erreur de connexion ",erreur)
        
    return adresses






#fonction pour recuperer la clef de l'api GraphHopper 
def clef_graphhopper(fichier):


    try:

        #ouvrir le fichier en mode lecture 
        with open(fichier,"r") as file:

            #recuper la clef si elle existe et un element None si non
            
            dic=(json.load(file)).get("graphhopper",{})
           
            clef=dic.get("API_KEY",None)
            #verifier quand même si la clef est un element valide
            if clef:
                print('clef recuperé avec succès')
            else:
                print("element recuperé n'est pas valide")
            

            
            return clef
        
    #gerer les erreurs dans le cas où il y a un problème de chemin ou type
            
    except FileNotFoundError:

        print("le fichier est introuvable")
        return None
    
    except json.JSONDecodeError:

        print("l'element recçu n'est pas json")
    
            
        
    




#on va utiliser le module graphHopper pour calculer le temps de trajets et trouver la commune qui minimse le temps maximal


#transformer les adresses des amis par coordonnées géographiques(la methode "duration()" de graphhopper exige)
def coordonnées_géos_amis(url_amis,client):
    liste_adresses_amis={}
    
    liste_dic_adresses=adresses_amis(url_amis)
#     definir un compteur pour donner un identidiant à chaque adresse après conversion
    identifiant=0
    
    for val in liste_dic_adresses:
        
        #constituer une adresse complète avec le numéro de la voie
        adresse=str(val["adresse"]["numéro"])+" "+val["adresse"]["voie"]+" "+str(val["adresse"]["code_postal"])+" "+val["adresse"]["ville"]
        
        #recuperation des coordonnées à l'aide de la methode address_to_latlong() et notre variable adresse
        latlong=client.address_to_latlong(adresse)

        #inserer le tuple obtnue dans le dictionnaire avec un identifiant
        liste_adresses_amis[identifiant]=latlong

        identifiant+=1
        
    
    return liste_adresses_amis

#transformer le dictionnaire des communes par un dictionnaire de seulement nom de commune avec lat et long(pour ne garder que les elements qui nous sont encore utiles)

def coordonnées_géos_communes(url_communes):
    

    #recuperer les communes 
    communes=données_communes(url_communes)
    #definir un dictionnaire vide pour stocker les données après traitement
    coordonnées_communes={}
    

    #parcourir le dictionnaire des communes
    for commune in communes:
        
        for dic in commune:

            nom=dic["nom"]
            
            # Il faut remarquer qu'ici la longitude est récupérée en premier, car dans les données fournies par l'API(communes), le tuple contenant les coordonnées géographiques est structuré comme (longitude, latitude).
            long=dic["centre"]["coordinates"][0]
            lat=dic["centre"]["coordinates"][1]
            
            #inserer dans le dictionnaire
            coordonnées_communes[nom]=(lat,long)
            
    return coordonnées_communes


#maintenant que nous avons les adresses, nous allons calculer le temps de trajets, pour cela nous allons utiliser la methode duration() du module GraphHopper
        
def temps_en_velo(client,url_amis,url_communes):
    

    # Nous allons récupérer les données des amis et des communes après traitement par les fonctions ci-dessus.

    adresss_amis=coordonnées_géos_amis(url_amis,client)
    adresses_communes=coordonnées_géos_communes(url_communes)
    temps_trajet={}
    
    #on va parcourir chaque commune 4 fois(nombre des amis) pour calculer la distances entre chaque commune et chaque adresse
    for commune,val in adresses_communes.items():

        #definir une liste vide qui contiendra les temps de trajets des amis vers la commune
        valeurs_temps=[]
        
        for adresse in adresss_amis.values():
            
            #utilisation de la methode duration(), avec 3 parametres,une liste qui contient les coordonnées , le moyen de deplacement(vélo pour notre cas) et l'unité de mesure(par heur ici)
            temps=client.duration([adresse,val],"bike","h")


            valeurs_temps.append(temps)

            temps_trajet[commune]=valeurs_temps
            
            
            
    
            
    #Transformer le dictionnaire en DataFrame 

    dataframe=pd.DataFrame(temps_trajet)
    
    #prendre le max de chaque colonne(commune)
    temps_max=dataframe.max()
    #minimiser ce temps et recuperer la commune optimale
    commune_optimale=temps_max.idxmin()
    temps_trajet=temps_max.min()

    print("la matrice des temps de trajets est :")
    print(dataframe)
    print("la commune optimale est ",commune_optimale,", ", "le  temps de trajet maximal en heures est de :", temps_trajet)
            
    return (dataframe,commune_optimale,temps_trajet)
            
            
        
            
            
        
    
    





#Section 3: testes

#a-urls api
url_communes="https://geo.api.gouv.fr/communes"
url_amis="https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis"

#b-clef
chemin_fichier_clef="nom_fichier.json"
clef=clef_graphhopper(chemin_fichier_clef)

#c-création d'un client GraphHopper
client =GraphHopper(api_key=clef)

#d-fonctions
temps_en_velo(client,url_amis,url_communes)

