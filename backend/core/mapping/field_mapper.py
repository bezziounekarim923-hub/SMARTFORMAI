from backend.core.mapping.mapping_result import MappingResult


class FieldMapper:
    """
    Associe les informations d'un profil
    aux champs détectés d'un formulaire.
    """

    def map(self, form, profile):

        mappings = []

        # Dictionnaire des correspondances
        aliases = {
            "nom": ["nom"],
            "prenom": ["prénom", "prenom"],
            "telephone": ["téléphone", "telephone", "tel"],
            "email": ["email", "e-mail", "mail"],
            "adresse": ["adresse"],
            "date_naissance": ["date de naissance", "naissance"],
        }

        for field in form.fields:

            label = field.label.lower().strip()

            for key, value in profile.items():

                if key not in aliases:
                    continue

                if label in aliases[key]:

                    mappings.append(
                        MappingResult(
                            profile_key=key,
                            value=value,
                            field=field,
                        )
                    )

        return mappings