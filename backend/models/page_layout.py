from dataclasses import dataclass, field

from backend.models.rectangle import Rectangle

from backend.models.text_block import TextBlock

@dataclass(slots=True)
class PageLayout:
    """
    Représente le résultat de l'analyse d'une page.
    """

    page_number: int

    rectangles: list[Rectangle] = field(default_factory=list)

    text_blocks: list[TextBlock] = field(default_factory=list)

    checkboxes: list = field(default_factory=list)

    tables: list = field(default_factory=list)