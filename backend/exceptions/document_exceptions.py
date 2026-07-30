"""
Exceptions utilisées par le module Document.
"""


class DocumentError(Exception):
    """Exception de base pour les erreurs liées aux documents."""
    pass


class DocumentNotFoundError(DocumentError):
    """Le fichier demandé est introuvable."""
    pass


class UnsupportedDocumentError(DocumentError):
    """Le format du document n'est pas supporté."""
    pass


class InvalidDocumentError(DocumentError):
    """Le document est invalide ou corrompu."""
    pass