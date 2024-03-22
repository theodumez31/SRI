import requests
from bs4 import BeautifulSoup
import hashlib
from urllib.parse import urljoin

def calculer_hachage(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def recup_page(url):
# Obtenir le contenu de la page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page. Code d'erreur : {response.status_code}")
    return response

def mettre_integrity(url):
    response = recup_page(url)
    # Analyser le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver toutes les balises avec l'attribut 'src'
    src_tags = soup.find_all(src=True)

    # Mettre à jour les balises avec le hachage et l'intégrité
    for tag in src_tags:
        src_url = tag['src']

        # Résoudre l'URL relative
        absolute_url = urljoin(url, src_url)

        src_content = requests.get(absolute_url).text
        hachage = calculer_hachage(src_content)
        tag['integrity'] = f"sha256-{hachage}"
        tag['src'] = f"data:{tag['src'].split('.')[-1]};base64,{hachage}"

    # Enregistrer la page modifiée
    with open('page_modifiee.html', 'w', encoding='utf-8') as fichier:
        fichier.write(str(soup))

    print("Page modifiée enregistrée avec succès.")

# Exemple d'utilisation avec une URL
url_page = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"#input("Veuillez rentrer l'URL de votre page : ")
mettre_integrity(url_page)