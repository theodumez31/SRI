import requests
 
from calcul_hashage import mettre_integrity

def verifier_lien_internet(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 1  # Code d'erreur 1 = OK
        else:
            return 2  # Code d'erreur 2 = Erreur de récupération de la page
    except Exception as e:
        print(f"Erreur : {e}")
        return 3  # Code d'erreur 3 = Échec de la requête HTTP
 
# Exemple d'utilisation
url_page = input("Veuillez entrer l'URL de votre page : ")
resultat = verifier_lien_internet(url_page)
print(f"Résultat du test : {resultat}")