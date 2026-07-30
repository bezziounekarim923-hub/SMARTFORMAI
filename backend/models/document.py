"""
Document model.

Represents a document loaded by SmartForm AI.
"""

from dataclasses import dataclass, field
from pathlib import Path

from backend.models.metadata import DocumentMetadata
from backend.models.page import Page

@dataclass(slots=True)
class Document:
    """
    Represents a loaded document.
    """

    path: Path
    page_count: int
    metadata: DocumentMetadata
    pages: list[Page] = field(default_factory=list)