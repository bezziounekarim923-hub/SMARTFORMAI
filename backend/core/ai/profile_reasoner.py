from datetime import datetime


class ProfileReasoner:
    """
    Adapte les valeurs du profil au type attendu par le formulaire.
    """

    def adapt(self, value, field_type: str):

        if value is None:
            return ""

        # Oui / Non
        if field_type == "yes_no":
            return "Oui" if bool(value) else "Non"

        # Date
        if field_type == "date":

            if isinstance(value, datetime):
                return value.strftime("%d/%m/%Y")

            if isinstance(value, str):

                for fmt in ("%Y-%m-%d", "%d/%m/%Y"):

                    try:
                        d = datetime.strptime(value, fmt)
                        return d.strftime("%d/%m/%Y")
                    except ValueError:
                        pass

        return str(value)