from backend.core.layout.layout_graph import LayoutGraph
from backend.models.layout_node import LayoutNode


class LayoutGraphBuilder:
    """
    Construit le graphe logique de la page.

    Le graphe contient :
      - les blocs OCR
      - les champs détectés
    """

    def build(
        self,
        text_blocks,
        fields,
    ) -> LayoutGraph:

        graph = LayoutGraph()

        node_id = 0

        # -------------------------------------------------
        # Blocs OCR
        # -------------------------------------------------

        for block in text_blocks:

            text = block.text.strip()

            graph.add_node(

                LayoutNode(

                    id=node_id,

                    node_type="text",

                    rectangle=block.bbox,

                    text=text,

                    confidence=getattr(block, "confidence", 1.0),

                )

            )

            node_id += 1

        # -------------------------------------------------
        # Champs
        # -------------------------------------------------

        for field in fields:

            graph.add_node(

                LayoutNode(

                    id=node_id,

                    node_type="field",

                    rectangle=field.rectangle,

                    text=field.label,

                    confidence=1.0,

                )

            )

            node_id += 1

        return graph