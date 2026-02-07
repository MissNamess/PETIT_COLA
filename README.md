# Examen de Fin de Module Python – Licence 3 🔥

Ce projet a été réalisé dans le cadre de l'évaluation finale du module Python. Il démontre la capacité à automatiser la collecte de données via le Web Scraping et à structurer une application métier via la Gestion de Stock orientée objet.

Encadrement académiqueModule :

- Programmation Python
- Institution : École Supérieure des Affaires (ESA)
- TogoObjectif : Validation des compétences en manipulation de données et logique POO.

## Description du projet 

### Partie 1 : Scraping Web Local 💻

L'objectif est d'extraire des informations structurées à partir d'un site web cloné localement (projet inggbaabrief3-main).Éléments extraits : 

- Titres (h1, h2),
- Paragraphes,
- Liens ,
- Formulaires et
- Images .

  Automatisation : Utilisation de BeautifulSoup pour parser le HTML et de la bibliothèque requests pour simuler l'accès au serveur local.

### Partie 2 : Gestion de Stock Orientée Objet 📦 

Mise en place d'une architecture robuste pour gérer un inventaire de produits et des commandes clients. 

. Classe Produit : Définit les attributs (ID, Nom, Prix, Quantité).

. Classe Stock : Le "cerveau" de l'application gérant l'inventaire via un dictionnaire (optimisation de la recherche).

. Logic métier : Vérification automatique de la disponibilité des produits avant validation de commande et mise à jour dynamique des quantités.

## Prérequis ⚠️

Environnement techniqueServeur Local :

- WAMP (ou XAMPP) pour héberger le site à scraper.
- Python : Version 3.9 ou supérieure.
- Bibliothèques nécessaires : requests, beautifulsoup4.

  Installation des dépendances
  
      Bash
      pip install requests beautifulsoup4
  
## Configuration et Exécution

1- Préparation du site :

 - Télécharger le dossier inggbaabrief3-main
 - Le placer dans le répertoire www de votre serveur WAMP
 - S'assurer que l'URL http://localhost/inggbaabrief3-main/index.html
  est accessible.
  
  2- Lancement du script :

    Bash
    python nom_de_votre_script.py
    
## Aperçu du Code 🛠️

Logique de validation des commandes

    Python
    def ajouter_commande(self, commande):
    # Vérification de l'existence du produit dans le dictionnaire
    if commande.produit.id in self.stock.Prd:
     produit_en_stock = self.stock.Prd[commande.produit.id]
        
        # Vérification du seuil de quantité
        if produit_en_stock.quantite >= commande.quantite:
            produit_en_stock.quantite -= commande.quantite
            self.commandes.append(commande)
            print(f"Commande {commande.id} validée.")
        else:
            print(f"Erreur : Stock insuffisant pour {produit_en_stock.nom}.")
            
### Extraction de données (Scraping)

    Python
    # Extraction des titres et paragraphes
    titres = soup.find_all(['h1', 'h2'])
    paragraphes = soup.find_all('p')
    
    for p in paragraphes:
        print(p.text.strip())
    
### Objectifs pédagogiques 🎯

- Maîtrise de la POO : Utilisation des classes, des constructeurs (__init__) et des méthodes spéciales (__str__).
- Encapsulation : Gestion des interactions entre la classe Stock et
- GestionDeStock.Web Data Mining : Comprendre l'arborescence du DOM HTML pour l'extraction de données.

  ## Auteurs

  Ce projet a été réalisé par une équipe de quatre collaborateurs :
  - NAMESSI Reine Essossinam  : Génie Logiciel
  - BONGOR Francine Akouvi : Génie Logiciel
  - GIDI Nyuimabu komi : Sécurité Informatique
  - Kossivi ayao david : Energie Renouvelable

  Licence 3 – École Supérieure des Affaires (ESA) - Togo
