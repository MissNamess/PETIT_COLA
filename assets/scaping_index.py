

from bs4 import BeautifulSoup

# Lire le fichier HTML local
with open("../index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Afficher le titre de la page
print("Titre:", soup.title.string if soup.title else "Pas de titre")

# Afficher tous les liens
print("\nLiens trouvés:")
for link in soup.find_all("a"):
    print(f"  - {link.get_text()}: {link.get('href')}")

# Afficher tous les paragraphes
print("\nParagraphes:")
for p in soup.find_all("p"):
    print(f"  - {p.get_text()}")