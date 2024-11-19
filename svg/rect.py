from .positioned_node import PositionedNode
from .vector2 import Vector2

class Rect(PositionedNode):
    _width: float
    _height: float

    def __init__(self, position: Vector2, width: float, height: float):
        super().__init__(position, 'rect')
        self._width = width
        self._height = height

        self.set_attribute("width", width)
        self.set_attribute("height", height)
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float) -> None:
        self._width = value
        self.set_attribute('width', value)
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def width(self, value: float) -> None:
        self._height = value
        self.set_attribute('height', value)