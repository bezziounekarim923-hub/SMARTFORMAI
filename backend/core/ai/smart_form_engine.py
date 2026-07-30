from pathlib import Path

from backend.core.ai.confidence_score import ConfidenceScore
from backend.core.ai.form_understanding import FormUnderstanding
from backend.core.ai.profile_reasoner import ProfileReasoner
from backend.core.ai.semantic_matcher import SemanticMatcher
from backend.models.mapping_result import MappingResult


class SmartFormEngine:
    """
    Moteur principal de SmartFormAI.
    """

    def __init__(self):

        self.understanding = FormUnderstanding()

        self.matcher = SemanticMatcher()

        self.reasoner = ProfileReasoner()

        self.confidence = ConfidenceScore()

    def prepare(
        self,
        pdf_path: Path,
        profile: dict,
    ):

        form = self.understanding.analyze(pdf_path)

        mappings = []

        for field in form.fields:

            key = self.matcher.match(
                field.label,
                profile,
            )

            if key is None:
                continue

            value = self.reasoner.adapt(
                profile.get(key),
                field.field_type,
            )

            score = self.confidence.compute(
                field.label,
                key,
            )

            mappings.append(

                MappingResult(

                    field=field,

                    profile_key=key,

                    value=value,

                    confidence=score,
                )

            )

        return form, mappings