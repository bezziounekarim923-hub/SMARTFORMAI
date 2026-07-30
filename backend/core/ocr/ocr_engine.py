from abc import ABC, abstractmethod

from backend.models.text_block import TextBlock


class OCREngine(ABC):
    """
    Interface commune à tous les moteurs OCR.
    """

    @abstractmethod
    def detect(self, image) -> list[TextBlock]:
        """
        Retourne les blocs de texte détectés.
        """
        pass