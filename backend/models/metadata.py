from dataclasses import dataclass


@dataclass(slots=True)
class DocumentMetadata:
    """
    Métadonnées d'un document.
    """

    title: str | None = None
    author: str | None = None
    subject: str | None = None
    creator: str | None = None
    producer: str | None = None