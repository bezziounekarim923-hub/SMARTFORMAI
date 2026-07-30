from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class GraphNode:
    """
    Noeud du graphe de layout.

    Un noeud peut représenter :
        - un bloc OCR
        - un champ
        - une checkbox
        - un radio button
        - une image
        - un tableau
    """

    id: str

    kind: str
    # text
    # field
    # checkbox
    # radio
    # table
    # image

    rectangle: Any

    text: str = ""

    confidence: float = 1.0

    payload: Any = None

    # voisins
    left: "GraphNode | None" = None
    right: "GraphNode | None" = None
    top: "GraphNode | None" = None
    bottom: "GraphNode | None" = None

    # relations
    parents: list["GraphNode"] = field(default_factory=list)
    children: list["GraphNode"] = field(default_factory=list)

    # score d'association
    score: float = 0.0

    @property
    def x(self):
        return self.rectangle.x

    @property
    def y(self):
        return self.rectangle.y

    @property
    def width(self):
        return self.rectangle.width

    @property
    def height(self):
        return self.rectangle.height

    @property
    def right_edge(self):
        return self.rectangle.x + self.rectangle.width

    @property
    def bottom_edge(self):
        return self.rectangle.y + self.rectangle.height

    @property
    def center_x(self):
        return self.rectangle.x + self.rectangle.width / 2

    @property
    def center_y(self):
        return self.rectangle.y + self.rectangle.height / 2

    def add_child(self, node: "GraphNode"):

        if node not in self.children:
            self.children.append(node)

        if self not in node.parents:
            node.parents.append(self)

    def __repr__(self):

        return (
            f"<GraphNode "
            f"{self.kind} "
            f"'{self.text}' "
            f"({self.x},{self.y},{self.width},{self.height})>"
        )