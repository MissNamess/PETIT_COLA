class Produit:
    def __init__(self, id, nom, prix, quantite):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f'Produit {self.id} : {self.nom}, Prix : {self.prix}, Quantité : {self.quantite}'

# Classe Stock
class Stock:
    def __init__(self):
        self.produits = {}

    def ajouter_produit(self, produit):
        if produit.id in self.produits:
            print(f"Erreur : Le produit ID {produit.id} existe déjà.")
        else:
            self.produits[produit.id] = produit
            print(f"Produit '{produit.nom}' ajouté avec succès.")

    def supprimer_produit(self, id):
        if id in self.produits:
            del self.produits[id]
            print('Produit supprimé avec succès.')
        else:
            print('Erreur : Produit non trouvé.')

    def modifier_produit(self, id, nom=None, prix=None, quantite=None):
        if id in self.produits:
            if nom: self.produits[id].nom = nom
            if prix: self.produits[id].prix = prix
            if quantite is not None: self.produits[id].quantite = quantite
            print('Produit modifié avec succès.')
        else:
            print('Erreur : Produit non trouvé.')

    def afficher_produits(self):
        print("\n--- État actuel du Stock ---")
        for produit in self.produits.values():
            print(produit)

# Classe Commande
class Commande:
    def __init__(self, id, produit, quantite):
        self.id = id
        self.produit = produit
        self.quantite = quantite

    def __str__(self):
        return f'Commande {self.id} : {self.produit.nom} (x{self.quantite})'

# Classe Gestion de Stock
class GestionDeStock:
    def __init__(self):
        self.stock = Stock()
        self.commandes = []

    def ajouter_commande(self, commande):
        # On vérifie si le produit existe dans le dictionnaire du stock
        if commande.produit.id in self.stock.produits:
            produit_en_stock = self.stock.produits[commande.produit.id]
            
            if produit_en_stock.quantite >= commande.quantite:
                produit_en_stock.quantite -= commande.quantite
                self.commandes.append(commande)
                print(f'Commande {commande.id} validée.')
            else:
                print(f'Erreur : Stock insuffisant pour {produit_en_stock.nom}.')
        else:
            print('Erreur : Produit non répertorié dans le stock.')

    def afficher_commandes(self):
        print("\n--- Historique des Commandes ---")
        for commande in self.commandes:
            print(commande)

# --- Exemple d'utilisation ---
gestion_de_stock = GestionDeStock()

# Création des produits
p1 = Produit(1, 'Ordinateur', 1200, 10)
p2 = Produit(2, 'Souris', 25, 50)

# Ajout au stock
gestion_de_stock.stock.ajouter_produit(p1)
gestion_de_stock.stock.ajouter_produit(p2)

# Création et passage de commandes
c1 = Commande(101, p1, 2)
c2 = Commande(102, p2, 60) # Test de dépassement de stock

gestion_de_stock.ajouter_commande(c1)
gestion_de_stock.ajouter_commande(c2)

# Affichage final
gestion_de_stock.stock.afficher_produits()
gestion_de_stock.afficher_commandes()