from dataclasses import dataclass

from backend.models.form_field import FormField


@dataclass(slots=True)
class MappingResult:
    """
    Associe une donnée du profil à un champ du formulaire.
    """

    profile_key: str
    value: str
    field: FormField