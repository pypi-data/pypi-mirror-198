import os
import re
import shutil

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
import requests


from jupytercor.utils import *

# Expression régulière pour remplacer les liens vers les images
pattern = r"\((https?://.+)\)"


# Créer une classe qui hérite de Treeprocessor et qui extrait les URL des images
class ImgExtractor(Treeprocessor):
    def __init__(self, md):
        # Utiliser self.markdown pour stocker l'instance du module markdown passée en paramètre
        self.markdown = md

    def run(self, doc):
        self.markdown.images = []
        for image in doc.findall(".//img"):
            self.markdown.images.append(image.get("src"))


# Créer une classe qui hérite de Extension et qui utilise la classe précédente
class ImgExtension(Extension):
    def extendMarkdown(self, md):
        img_ext = ImgExtractor(md)
        md.treeprocessors.register(img_ext, "img_ext", 15)


def download_image(cell):
    """Download images from url in markdown cell"""

    md = markdown.Markdown(extensions=[ImgExtension()])
    # Appliquer la méthode convert pour extraire les URL des images dans la liste md.images
    md.convert(cell)
    # Parcourir la liste des URL des images et les télécharger avec requests
    for url in md.images:
        if is_valid_url(url):
            # Récupérer le nom du fichier image à partir de l'URL (après le dernier /)
            filename = url.split("/")[-1]
            print(f"Téléchargement de {filename}")
            # Envoyer une requête GET à l'URL et vérifier le statut de la réponse (200 = OK)
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                # Ouvrir un fichier dans le dossier images avec le même nom que l'image
                with open(os.path.join("images", filename), "wb") as f:
                    # Copier le contenu de la réponse dans le fichier avec shutil
                    shutil.copyfileobj(response.raw, f)


# Définir une fonction qui remplace chaque URL par le chemin relatif vers l'image téléchargée
def replace_url(match):
    """remplace chaque URL par le chemin relatif vers l'image téléchargée"""
    # Récupérer l'URL capturée par le groupe 1 de l'expression régulière
    url = match.group(1)
    # Récupérer le nom du fichier image à partir de l'URL (après le dernier /)
    filename = url.split("/")[-1]
    # Construire le chemin relatif vers l'image téléchargée dans le dossier images
    path = os.path.join("images", filename)
    # Retourner le chemin relatif entre parenthèses à la place de l'URL
    return f"({path})"


def download_images(nb):
    """Download all images frome a notebook

    Args:
        nb 'notebook': original notebook
    """
    if os.path.exists("images"):
        print("Le répertoire images existe déjà.")
    else:
        # Créer le répertoire
        try:
            os.mkdir("images")
        except OSError as e:
            # Gérer les éventuelles erreurs
            print(
                "Une erreur est survenue lors de la création du répertoire : 'images'"
            )
            return None

    # Loop through the cells and download images in images folder
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            download_image(cell.source.encode())
            # Appliquer la fonction replace_url sur toutes les occurrences du motif dans le texte avec re.sub
            result = re.sub(pattern, replace_url, cell.source)
            cell.source = result

    return nb
