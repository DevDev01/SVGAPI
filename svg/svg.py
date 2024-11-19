from .node import Node
from .color import Color
from .rect import Rect
from .vector2 import Vector2

class SVG(Node):
    _width: int
    _height: int

    def __init__(self, width: int, height: int):
        super().__init__('svg', False)
        self._width = width
        self._height = height

        self.set_attribute('width', width)
        self.set_attribute('height', height)
    
    def background(self, color: Color):
        background_rect = Rect(Vector2(0, 0), self.width, self.height)
        background_rect.fill(color=color)
        self.add_node(background_rect)

    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int) -> None:
        self._width = value
        self.set_attribute('width', value)
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def width(self, value: int) -> None:
        self._height = value
        self.set_attribute('height', value)
