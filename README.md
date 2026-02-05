# EXAMEN DE FINI DE MODULE PYTHON 

Pour définr simple, Python, c'est un langage de programmation. C'est l'outil qui permet de donner des instructions à un ordinateur pour qu'il réalise des tâches.

Et Le web Scraping , c'est une technique qui consiste à utiliser un robot pour extraire automatiquement des données d'un site web. A la suite nous avons eu à traiter deux exercices un en web scraping et 

l'autre en python.

## LES EXERCICES 

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

## GESTION_STOCK

Ce code permet de gérer un inventaire de produits, d'effectuer des mises à jour de stock et de traiter des commandes clients avec vérification automatique des disponibilités.

## Prerequis

### Prérequis du Projet SCRAPING_CODE

Avant de lancer le script de scraping :

On à clôner le projet inggbaabrief3-main en téléchargeant d'abord le dossier dans le github , désiper , copier et coller dans wamp qui est un serveur après installer le beautifulsoup. 

    import requests
    from bs4 import BeautifulSoup
    import os
    
    url = "http://localhost/inggbaabrief3-main/index.html"
    
    response = requests.get(url)
    response.encoding = 'utf-8'
    
Bibliothèques d'Extraction :

  BeautifulSoup4 ou Scrapy pour le parsing du code HTML.

  Requests pour envoyer les requêtes HTTP (si le site n'est pas purement local).

### Prerequis python

Class produit : définir les entiers idantifiant du produit , nom du produit , prix du produit et quantité du produit . 

Class stock : C'est le "cerveau" de mon application . c'est elle qui gère l'inventaire, permet d'ajouter des articles, de les modifier ou de les supprimer. Elle utilise un dictionnaire pour stocker les objets, ce qui rend la recherche très rapide.

Class commande : on défini la commande son id , le produit et la quantité après on retourne pour afficher.

Class Gestion de stock : on vérifie si le produit existe dans le dictionnaire de stock .

Les Méthodes Spéciales :

__init__ : Le constructeur qui prépare l'objet.

__str__ : Ce qui permet d'afficher l'objet proprement avec print().

L'Encapsulation : Le fait que la classe GestionDeStock contienne un objet de type Stock.

## titre
Exemple de Menu Interactif

    Python
       class GestionDeStock:
        def __init__(self):
            self.stock = Stock()
            self.commandes = []
    
    # On vérifie si le produit existe dans le dictionnaire du stock
    def ajouter_commande(self, commande):
        
        if commande.produit.id in self.stock.Prd:
            produit_en_stock = self.stock.Prd[commande.produit.id]
            
            if produit_en_stock.quantite >= commande.quantite:
                produit_en_stock.quantite -= commande.quantite
                self.commandes.append(commande)
                print(f'Commande {commande.id} validée.')
            else:
                print(f'Erreur : Stock insuffisant pour {produit_en_stock.nom}.')
        else:
            print('Erreur : Produit non retrouvé.')

    def afficher_commandes(self):
        print("\n Historique ")
        for commande in self.commandes:
            print(commande)

            
 Exemple de mise en forme pour ton code scraping :

    Python
    if response.status_code == 200:
        html = response.text  
    f = open("Franck.html", "w")
    f.write(html)
    f.close()
    
    # Extraire les images
    images = soup.find_all("img")
    for image in images :
        print(image['src'])

    #Extraire les titres
    titres = soup.find_all(['h1', 'h2'])
    for titre in titres :
        print(titre.text.strip())
    #Extraire les paragraphes
    paragraphes = soup.find_all('p')
    for paragraphe in paragraphes:
        print(paragraphe.text.strip())
    #Extraire les formulaires
    formulaires = soup.find_all('form')
    for formulaire in formulaires:
        print(formulaire)
    #Extraire les liens
    liens = soup.find_all('a')
    for lien in liens:
        print(lien['href'])
