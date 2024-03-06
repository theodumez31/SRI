import requests
 
from calcul_hashage import recup_page

def verifier_lien_internet():
    try:
        url_test = "https://exemple.com"
        response = requests.get(url_test)
        if response.status_code == 200:
            return 1  # Code d'erreur 1 = OK
        else:
            return 2  # Code d'erreur 2 = Erreur de récupération de la page
    except Exception as e:
        print(f"Erreur : {e}")
        return 3  # Code d'erreur 3 = Échec de la requête HTTP
 
# Exemple d'utilisation
resultat = verifier_lien_internet()
print(f"Résultat du test : {resultat}")