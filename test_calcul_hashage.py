import requests
import pytest
import hashlib

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


def calculer_hachage(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def test_calculer_hachage():
    # Données d'entrée
    data = "Hello, World!"

    # Résultat attendu
    expected_hash = "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"

    # Calcul du hachage
    result = calculer_hachage(data)

    # Vérification
    assert result == expected_hash