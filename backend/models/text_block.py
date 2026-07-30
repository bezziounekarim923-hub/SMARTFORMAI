from dataclasses import dataclass

from backend.models.rectangle import Rectangle


@dataclass(slots=True)
class TextBlock:
    """
    Représente un bloc de texte détecté par OCR.
    """

    text: str

    confidence: float

    rectangle: Rectangle

    @property
    def bbox(self) -> Rectangle:
        return self.rectangle