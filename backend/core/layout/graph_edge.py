from dataclasses import dataclass

from backend.core.layout.graph_node import GraphNode


@dataclass(slots=True)
class GraphEdge:
    """
    Représente une relation spatiale entre deux noeuds.

    Exemples :

        label ------LABEL_OF------> champ

        texte ------LEFT_OF-------> champ

        checkbox ---OPTION_OF-----> groupe

        cellule ----INSIDE--------> tableau
    """

    source: GraphNode

    target: GraphNode

    relation: str

    weight: float = 1.0

    def __repr__(self):

        return (
            f"<Edge "
            f"{self.source.id}"
            f" --{self.relation}--> "
            f"{self.target.id}"
            f" ({self.weight:.2f})>"
        )


# ==========================================================
# Relations standards
# ==========================================================

LEFT_OF = "LEFT_OF"

RIGHT_OF = "RIGHT_OF"

ABOVE = "ABOVE"

BELOW = "BELOW"

SAME_LINE = "SAME_LINE"

SAME_COLUMN = "SAME_COLUMN"

OVERLAP = "OVERLAP"

CONTAINS = "CONTAINS"

INSIDE = "INSIDE"

NEAR = "NEAR"

LABEL_OF = "LABEL_OF"

OPTION_OF = "OPTION_OF"

NEXT = "NEXT"

PREVIOUS = "PREVIOUS"

PARENT = "PARENT"

CHILD = "CHILD"