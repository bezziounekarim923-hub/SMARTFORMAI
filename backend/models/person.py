from dataclasses import dataclass


@dataclass(slots=True)
class Person:
    """
    Informations extraites d'une personne.
    """

    nom: str = ""
    prenom: str = ""
    date_naissance: str = ""
    adresse: str = ""
    telephone: str = ""
    email: str = ""
    nationalite: str = ""
    situation_familiale: str = ""
    profession: str = ""