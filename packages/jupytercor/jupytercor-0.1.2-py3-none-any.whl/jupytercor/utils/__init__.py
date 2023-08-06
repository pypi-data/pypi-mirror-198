from urllib.parse import urlparse


def is_valid_url(url):
    # Parse l'url en ses composants
    result = urlparse(url)
    # Retourne True si le schéma est http ou https
    return result.scheme in ("http", "https")
