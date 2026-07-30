from dataclasses import dataclass, field

from backend.models.form_field import FormField


@dataclass(slots=True)
class Form:
    """
    Représente un formulaire complet.
    """

    name: str
    page_count: int
    fields: list[FormField] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "page_count": self.page_count,
            "fields": [field.to_dict() for field in self.fields],
        }
