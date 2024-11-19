from .color import Color
from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Style:
    fill: Color = Color.TRANSPARENT
    stroke: Color = Color.TRANSPARENT
    stroke_weight: float = 0.0

    def populate_node(self, node: "Node") -> None:
        if not self.fill.is_transparent(): 
            node.set_attribute('fill', self.fill.as_string())        
        if self.fill.is_transparent() and not self.stroke.is_transparent():
            node.set_attribute('fill', 'none')

        if not self.stroke.is_transparent(): 
            node.set_attribute('stroke', self.stroke.as_string())
        if self.stroke.is_transparent() and not self.fill.is_transparent():
            node.set_attribute('stroke', 'none')
        
        if self.stroke_weight > 0.0:
            node.set_attribute('stroke-width', self.stroke_weight)
          
class Node:
    _tag: str
    _is_self_closing: bool
    _attributes: List[Tuple[str, str]]
    _child_nodes: List['Node']
    _style: Style

    def __init__(self, tag: str, is_self_closing: bool = True):
        self._tag = tag
        self._is_self_closing = is_self_closing
        self._attributes = []
        self._child_nodes = []
        self._style = Style()
    
    #Shared
    def set_attribute(self, key: str, value) -> None:
        for i, (k, v) in enumerate(self._attributes):
            if k == key:
                self._attributes[i] = (key, f'{value}')
                return
        
        self._attributes.append((key, f'{value}'))

    def has_attribute(self, key: str) -> bool:
        for k, v in self._attributes:
            if k == key:
                return True
        
        return False
    
    def add_node(self, node: 'Node') -> None:
        self._child_nodes.append(node)

    def clear_nodes(self) -> None:
        self._child_nodes.clear()
        
    #Building
    def stringify_attributes(self) -> str:
        attributes_str = ''
        for key, value in self._attributes:
            attributes_str += f' {key}="{value}"'
        return attributes_str

    def stringify_child_nodes(self) -> str:
        nodes_str = ''
        for node in self._child_nodes:
            nodes_str += node.as_string()
        return nodes_str

    def as_string(self) -> str:
        self._style.populate_node(self)
        if self._is_self_closing:
            return f'<{self._tag}{self.stringify_attributes()} />'
        else:
            return f'<{self._tag}{self.stringify_attributes()}>{self.stringify_child_nodes()}</{self._tag}>'
    
    #Styling
    def fill(self, color: Color = None, rgb: Tuple[int, int, int] = None, grayscale: int = None, hex: str = None, alpha: int = 255) -> None:
        if color is None:
            self.style.fill = Color(rgb, grayscale, hex, alpha)
        else:
            self.style.fill = color
    
    def stroke(self, color: Color = None, rgb: Tuple[int, int, int] = None, grayscale: int = None, hex: str = None, alpha: int = 255) -> None:
        if color is None:
            self.style.stroke = Color(rgb, grayscale, hex, alpha)
        else:
            self.style.stroke = color
    
    def stroke_weight(self, weight: float) -> None:
        self.style.stroke_weight = weight

    #Properties
    @property
    def style(self) -> Style:
        return self._style
    
    @style.setter
    def style(self, value: Style) -> None:
        self._style = value