# EXAMEN DE FINI DE MODULE PYTHON 

Pour définr simple, Python, c'est un langage de programmation. C'est l'outil qui permet de donner des instructions à un ordinateur pour qu'il réalise des tâches.

Et Le web Scraping , c'est une technique qui consiste à utiliser un robot pour extraire automatiquement des données d'un site web. A la suite nous avons eu à traiter deux exercices un en web scraping et 

l'autre en python.

# LES EXERCICES 

Exercice 1:

Scrapper un site en local en ressorttant les images , les titres , les paragraphes , le formulaire ainsi les liens .

Exercice 2 :

Utiliser la logique d'une application de gestion de stock en vérifiant tout les concepts 


Ces exercices ont été faite en groupe de quatre (4) personnes 

Collaborateurs : 

    -reinenamessi8@gmail.com
    -francinebongor@gmail.com 
    -pierregidi445@gmail.com
    -kossiviayaodavid@gmail.com

# GESTION_STOCK

Ce code permet de gérer un inventaire de produits, d'effectuer des mises à jour de stock et de traiter des commandes clients avec vérification automatique des disponibilités.

## Prerequis

### Prérequis du Projet SCRAPING_CODE

Avant de lancer le script de scraping :

On à clôner le projet inggbaabrief3-main en téléchargeant d'abord le dossier dans le github , désiper , copier et coller dans wamp qui est un serveur après installer le beautifulsoup. 

Bibliothèques d'Extraction :

  BeautifulSoup4 ou Scrapy pour le parsing du code HTML.

  Requests pour envoyer les requêtes HTTP (si le site n'est pas purement local).

### Prerequis python

1. Environnement Python
Version : Python 3.6 ou plus récent. Le code utilise des f-strings (ex: f"Prix : {self.prix}"), une syntaxe qui n'est pas supportée par les versions plus anciennes.

Installation : Vérifie ta version avec la commande :

    Bash
    python --version
    
2. Éditeur de texte (IDE)
Bien que le Bloc-notes suffise, il est fortement recommandé d'utiliser un éditeur qui gère l'indentation (les espaces en début de ligne), car Python y est très sensible :

VS Code (recommandé avec l'extension Python).

PyCharm.

IDLE (installé par défaut avec Python).

### Prérequis Conceptuels (POO)
Pour comprendre et modifier ce code, tu dois maîtriser quelques notions de Programmation Orientée Objet (POO) :

Les Classes et Instances : Comprendre que Produit est le moule et produit1 est l'objet réel créé à partir de ce moule.

Les Méthodes Spéciales :

__init__ : Le constructeur qui prépare l'objet.

__str__ : Ce qui permet d'afficher l'objet proprement avec print().

L'Encapsulation : Le fait que la classe GestionDeStock contienne un objet de type Stock.

## titre
Exemple de Menu Interactif

    Python
    while True:
    print("\n1. Afficher Stock | 2. Ajouter Produit | 3. Passer Commande | 4. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        gestion_de_stock.stock.afficher_produits()
    elif choix == "2":
        id_p = int(input("ID : "))
        nom_p = input("Nom : ")
        prix_p = float(input("Prix : "))
        qte_p = int(input("Quantité : "))
        gestion_de_stock.stock.ajouter_produit(Produit(id_p, nom_p, prix_p, qte_p))
    elif choix == "4":
        print("Au revoir !")
        break

 Exemple de mise en forme pour ton code :

    Python
    # --- Exemple de structure pour l'extraction ---
    import os
    from bs4 import BeautifulSoup

    def extraire_donnees_locales(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Extraction des images, titres, etc.
    # [Ton code ici...]
    
