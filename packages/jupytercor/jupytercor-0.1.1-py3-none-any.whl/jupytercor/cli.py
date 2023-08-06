#!/usr/bin/env python3

import nbformat
import subprocess
import argparse
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
import requests
import os
import shutil
import re

# Expression régulière pour remplacer les liens vers les images
pattern = r"\((https?://.+)\)"

# Create an argument parser object
parser = argparse.ArgumentParser(
    description="Convert markdown cells in a jupyter notebook with pandoc"
)
# Add an input file argument
parser.add_argument("input_file", help="The name of the input notebook file")
# Add an output file argument with no default value
parser.add_argument(
    "-o", "--output_file", help="The name of the output notebook file", default=None
)
# Add a clean flag argument with a default value of False
parser.add_argument(
    "--clean",
    help="Clean the markdown cells with pandoc conversions",
    action="store_true",
)
# Add a latex flag argument with a default value of False
parser.add_argument(
    "--latex", help="Convert the output to latex format", action="store_true"
)
# Add a images flag argument with a default value of False
parser.add_argument(
    "--images", help="Downlad image in images folder", action="store_true"
)
# Parse the arguments
args = parser.parse_args()


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
    print(md)
    # Parcourir la liste des URL des images et les télécharger avec requests
    for url in md.images:
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
            print(cell.source.encode())
            result = re.sub(pattern, replace_url, cell.source)
            print(result)
            cell.source = result

    return nb


def clean_markdown(nb: nbformat):
    """Read the input notebook and convert all markdown cells
    into a clean markdown without html tags"""
    # Loop through the cells and transform markdown cells with pandoc if clean is True

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            # Run a pandoc command to convert markdown to html
            html = subprocess.run(
                ["pandoc", "-f", "markdown", "-t", "html", "-o", "-"],
                input=cell.source.encode(),
                capture_output=True,
            )
            result = subprocess.run(
                ["pandoc", "-f", "html", "-t", "gfm-raw_html", "-o", "-"],
                input=html.stdout,
                capture_output=True,
            )
            # Replace the cell source with the transformed text
            cell.source = result.stdout.decode()

    return nb


def main():
    print("Hello from jupytercor !")
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")

    # Read the input notebook file from the input_file argument
    nb = nbformat.read(args.input_file, as_version=4)
    if args.clean:
        print("Démarrage du nettoyage...")
        nb = clean_markdown(nb)
        # Write the output notebook file in the same file as the input file if output_file is None or in a different file otherwise
        if args.output_file is None:
            nbformat.write(nb, args.input_file)
        else:
            nbformat.write(nb, args.output_file)
        print("Nettoyage effectué avec succès !")
    elif args.images:
        print("Téléchargement de images...")
        nb = download_images(nb)
        # Write the output notebook file in the same file as the input file if output_file is None or in a different file otherwise
        if args.output_file is None:
            nbformat.write(nb, args.input_file)
        else:
            nbformat.write(nb, args.output_file)
        print("Images téléchargées avec succès !")


if __name__ == "__main__":
    main()
