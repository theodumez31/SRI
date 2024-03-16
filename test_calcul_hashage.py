import requests
import pytest

def recup_page(url):
    # Obtenir le contenu de la page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page. Code d'erreur : {response.status_code}")
    return response

def test_recup_page():
    # URL de test
    test_url = "https://www.example.com"
    
    # Appel de la fonction avec l'URL de test
    result = recup_page(test_url)
    
    # Vérification que le résultat est un objet Response
    assert isinstance(result, requests.Response)
    
    # Vérification du code d'état HTTP
    assert result.status_code == 200
