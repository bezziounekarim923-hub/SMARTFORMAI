from backend.models.form import Form
from backend.models.form_field import FormField
from backend.models.page_layout import PageLayout


class FormBuilder:
    """
    Construit un objet Form à partir des champs détectés.
    """

    def build(
        self,
        fields: list[FormField],
        page_layout: PageLayout | None = None,
    ) -> Form:

        name = (
            f"form_page_{page_layout.page_number}"
            if page_layout is not None
            else "form"
        )
        page_count = 1

        return Form(
            name=name,
            page_count=page_count,
            fields=fields,
        )