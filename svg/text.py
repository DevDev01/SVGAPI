from .positioned_node import PositionedNode
from .vector2 import Vector2

class Text(PositionedNode):
    def __init__(self, value: str, position: Vector2):
        super().__init__(position, 'text', is_self_closing=False)
        self.text = value