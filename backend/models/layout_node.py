from dataclasses import dataclass

from backend.models.rectangle import Rectangle


@dataclass
class LayoutNode:
    """
    Représente un élément du document.

    Un nœud peut être :
    - un texte OCR
    - un champ
    - une case à cocher
    - un tableau
    - etc.
    """

    node_type: str
    rectangle: Rectangle
    text: str = ""
    confidence: float = 1.0
    id: int = 0