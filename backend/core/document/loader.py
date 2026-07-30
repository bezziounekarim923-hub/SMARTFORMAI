"""
Document loader base classes.

SmartForm AI
"""

from abc import ABC, abstractmethod
from pathlib import Path


class DocumentLoader(ABC):
    """
    Base class for every document loader.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    @abstractmethod
    def load(self):
        """
        Load the document.
        """
        pass