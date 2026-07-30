from dataclasses import dataclass

from backend.models.form_field import FormField


@dataclass(slots=True)
class MappingResult:
    """
    Résultat du mapping entre un champ et une donnée du profil.
    """

    field: FormField

    profile_key: str

    value: str

    confidence: float