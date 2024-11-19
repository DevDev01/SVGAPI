from .node import Node
from .vector2 import Vector2
from typing import Tuple

class Shape(Node):
    _position: Vector2
    _position_key: Tuple[str, str]

    def __init__(self, position: Vector2, tag: str, position_key: Tuple[str, str] = ('x', 'y'), is_self_closing: bool = True):
        super().__init__(tag, is_self_closing)
        self._position = position
        self._position_key = position_key

        self.set_attribute(position_key[0], position.x)
        self.set_attribute(position_key[1], position.y)

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, value: Vector2) -> None:
        self._position = value
        self.set_attribute(self._position_key[0], value.x)
        self.set_attribute(self._position_key[1], value.y)

    @property
    def x(self) -> float:
        return self._position.x
    
    @x.setter
    def x(self, value: float) -> None:
        self._position.x = value
        self.set_attribute(self._position_key[0], value)

    @property
    def y(self) -> float:
        return self._position.y
    
    @y.setter
    def y(self, value: float) -> None:
        self._position.y = value
        self.set_attribute(self._position_key[1], value)