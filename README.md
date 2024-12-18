# Lieu-de-rencontre-optimal

## Introduction

Des amis souhaitent se retrouver pour passer un week‑end ensemble. Ils comptent pour cela louer un gîte mais, n’habitant pas tous au même endroit, se demandent dans quelle commune louer ce gîte.

Les amis, soucieux de l’avenir de leur planète, se sont mis d’accord pour utiliser le vélo comme unique moyen de transport entre leur domicile et le gîte. Ils se sont aussi mis d’accord pour choisir un gîte qui minimise le temps de trajet maximal et en plus le gîte devra se trouver dans l’un des départements suivants : Ille‑et‑Vilaine (35), Mayenne (53), Côtes‑d’Armor (22), Sarthe (72) ou Morbihan (56).

Ce projet utilisant Python vise à trouver la commune optimale, en minimisant le temps de trajet maximal depuis leurs domiciles.

---

## Auteurs

- 22410567 Mahamat ABDRAMAN  
- 22409612 Adami ABDOURAHAMANE CHEGOU  
- 22409616 Uriel ADOTANOU

---

## Références

- **Cours de Python**
- **Erreurs et Exceptions en Python** : [Documentation officielle](https://docs.python.org/fr/3.5/tutorial/errors.html)
- **Documentation GraphHopper** : [API Adresses Amis](https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis)
- **API Découpage Administratif** : [Géo API](https://geo.api.gouv.fr/decoupage-administratif)

---

## Ressources

| Ressource                   | Description                            | Lien                                       |
|-----------------------------|----------------------------------------|---------------------------------------------|
| **API Logements**           | Données administratives des communes | [Lien](https://geo.api.gouv.fr/communes)   |
| **API Adresses Amis**       | Adresses des amis fictives            | [Lien](https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis) |
| **GraphHopper API**         | Calcul des trajets en vélo            | [Lien](https://graphhopper.com/)           |

---

## Bibliothèques Utilisées

| Bibliothèque  | Description                     |
|---------------|-------------------------------|
| `requests`    | Requêtes HTTP pour les APIs   |
| `json`        | Manipulation de fichiers JSON |
| `numpy`       | Calculs numériques            |
| `pandas`      | Traitement des données        |
| `GraphHopper` | Calcul des trajets            |

---

## Installation

Pour exécuter le projet, suivez ces étapes :

1. **Installation des dépendances**
   - Assurez-vous d'avoir Python installé.
   - Installez les dépendances à partir du fichier `requirements.txt` :

     ```bash
     pip install -r requirements.txt
     ```

2. **Obtenir une clé API GraphHopper**
   - Créez un compte sur le site officiel de [GraphHopper](https://graphhopper.com/).
   - Générez une clé API et remplacez-la dans le fichier de configuration correspondant.

---

**Fin du Projet**

---

