"""
Document metadata extraction utilities.

This module defines the metadata structure used throughout SmartForm AI.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class DocumentMetadata:
    """
    Stores metadata extracted from a PDF document.
    """

    title: Optional[str] = None
    author: Optional[str] = None
    subject: Optional[str] = None
    creator: Optional[str] = None
    producer: Optional[str] = None

    creation_date: Optional[str] = None
    modification_date: Optional[str] = None

    page_count: int = 0