import requests
from bs4 import BeautifulSoup
import os

url = "http://localhost/inggbaabrief3-main/index.html"

response = requests.get(url)
response.encoding = 'utf-8'
# print(response.text)

if response.status_code == 200:
    html = response.text
    # print(html)

    f = open("Franck.html", "w")
    f.write(html)
    f.close()
    #Parsons le contenu du site
    soup = BeautifulSoup(html, "html5lib")

    # paragraphe = soup.find_all("P")
    # print(paragraphe)
    # Image = soup.find("div", class_="photo")
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


        
            





else:
    print("ERREUR:", response.status_code)

print('Fin')