from backend.models.layout_node import LayoutNode


class LayoutGraph:
    """
    Graphe représentant tous les éléments d'une page.
    """

    def __init__(self):

        self.nodes: list[LayoutNode] = []

    def add_node(
        self,
        node: LayoutNode,
    ):

        self.nodes.append(node)

    def texts(self):

        return [
            node
            for node in self.nodes
            if node.node_type == "text"
        ]

    def fields(self):

        return [
            node
            for node in self.nodes
            if node.node_type == "field"
        ]

    def checkboxes(self):

        return [
            node
            for node in self.nodes
            if node.node_type == "checkbox"
        ]