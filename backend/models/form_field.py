from dataclasses import dataclass

from backend.models.rectangle import Rectangle


@dataclass(slots=True)
class FormField:
    """
    Représente un champ détecté dans un formulaire.
    """

    id: str

    page: int

    label: str

    field_type: str
    # text
    # checkbox
    # radio
    # yes_no
    # date
    # textarea

    rectangle: Rectangle

    options: list[str] | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "page": self.page,
            "label": self.label,
            "field_type": self.field_type,
            "rectangle": self.rectangle.to_dict(),
            "options": self.options,
        }