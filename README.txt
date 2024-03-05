# Script de Mise à jour de l'intégrité des balises 'src' dans une page web

Ce script Python utilise les bibliothèques `requests`, `BeautifulSoup`, et `hashlib` pour mettre à jour les balises 'src' dans le HTML d'une page web 
avec leur hachage SHA-256 et l'attribut 'integrity'. Le script résout également les URLs relatives pour garantir une intégrité correcte.

## Prérequis
- Python 3.x
- Bibliothèques Python requises : `requests`, `beautifulsoup4`

## Installation des dépendances
```bash
pip install requests beautifulsoup4


Utilisation

1.Modifiez la variable url_page dans le script avec l'URL de la page que vous souhaitez traiter.
2.Exécutez le script.

Le script récupérera le contenu de la page, calculera le hachage SHA-256 de chaque ressource externe liée dans les balises 'src', et mettra à jour les balises
avec les attributs 'integrity' et 'src'. La page modifiée sera enregistrée dans un fichier nommé page_modifiee.html.
