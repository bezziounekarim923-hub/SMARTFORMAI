from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Page:
    """
    Représente une page d'un document.
    """

    number: int
    width: float
    height: float

    image: Any | None = None
    rectangles: list = field(default_factory=list)