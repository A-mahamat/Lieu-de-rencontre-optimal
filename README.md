<!-- Centrer le titre -->
<h1 style="text-align: center;">Lieu-de-rencontre-optimal</h1>

<!-- Afficher les images horizontalement -->
<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://camo.githubusercontent.com/5efb9df0b493930aa6f022435951aa064d5e3eb914852e5d843b17cabc81e53c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d79656c6c6f773f7374796c653d666c6174266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465" alt="python" width="150">

  <img src="https://camo.githubusercontent.com/4b6d1896289e516b408d9359429c367a5b18403414932c712c4db0698254cdf5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50616e6461732d3661613834663f7374796c653d666c6174266c6f676f3d70616e646173266c6f676f436f6c6f723d7768697465" alt="pandas" width="150">

  <img src="https://camo.githubusercontent.com/41cfb13664ec1918911ebc27162b51f3ad3892637ccea7d7b6f46745592a597c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a7570797465722d6f72616e67653f7374796c653d666c6174266c6f676f3d6a757079746572266c6f676f436f6c6f723d7768697465" alt="jupyter" width="150">

  <img src="https://camo.githubusercontent.com/5148b102493357fd2bf9d7f0fcbeebe82fc7c1fe7de8f4f1637cdee867a99e9c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4150492d626c75653f7374796c653d666c6174266c6f676f3d66617374617069266c6f676f436f6c6f723d7768697465" alt="apis" width="100">
</div>






## Introduction

Des amis souhaitent se retrouver pour passer un week‑end ensemble. Ils comptent pour cela louer un gîte mais, n’habitant pas tous au même endroit, se demandent dans quelle commune louer ce gîte.

Les amis, soucieux de l’avenir de leur planète, se sont mis d’accord pour utiliser le vélo comme unique moyen de transport entre leur domicile et le gîte. Ils se sont aussi mis d’accord pour choisir un gîte qui minimise le temps de trajet maximal et en plus le gîte devra se trouver dans l’un des départements suivants : Ille‑et‑Vilaine (35), Mayenne (53), Côtes‑d’Armor (22), Sarthe (72) ou Morbihan (56).

Ce projet utilisant Python vise à trouver la commune optimale, en minimisant le temps de trajet maximal depuis leurs domiciles.

---

## Auteurs

- Mahamat ABDRAMAN  
- Adami ABDOURAHAMANE CHEGOU  
- Uriel ADOTANOU

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
| **API communes**           | Données administratives des communes | [Lien](https://geo.api.gouv.fr/communes)   |
| **API Adresses Amis**       | Adresses des amis fictives            | [Lien](https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis) |
| **GraphHopper API**         | Calcul des trajets en vélo            | [Lien](https://graphhopper.com/)           |

---

## Bibliothèques Utilisées

| Bibliothèque  | Description                     |
|---------------|-------------------------------|
| `requests`    | Requêtes HTTP pour les APIs   |
| `json`        | Manipulation de fichiers JSON |
| `pandas`      | Traitement des données        |
| `GraphHopper` | Calcul des trajets            |

---

## Installation

Pour exécuter le projet, suivez ces étapes :

1. **Installation des dépendances**
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

