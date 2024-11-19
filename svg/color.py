from typing import Tuple

class Color:
    TRANSPARENT: "Color" = None

    red: int
    green: int
    blue: int
    alpha: int

    def __init__(self, rgb: Tuple[int, int, int] = None, grayscale: int = None, hex: str = None, alpha: int = 255):
        r, g, b = self._parse_colors(rgb, grayscale, hex)
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = alpha
    
    def _parse_colors(self, rgb: Tuple[int, int, int] = None, grayscale: int = None, hex: str = None) -> Tuple[int, int, int]:
        if rgb is not None:
            return rgb
        elif grayscale is not None:
            return (grayscale, grayscale, grayscale)
        elif hex is not None:
            self._parse_hex(hex)
        else:
            return 0, 0, 0
    
    def _parse_hex(hex: str) -> tuple[int, int, int]:
        hex = hex.lstrip('#')
        
        if len(hex) != 6:
            raise ValueError("Hex color must be 6 characters long.")
        
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        
        return r, g, b        
   
    def is_transparent(self) -> bool:
        return (self.red == -1 or self.green == -1 or self.blue == -1) and self.alpha == 0

    def as_string(self) -> str:
        return f'rgba({self.red},{self.green},{self.blue},{round(self.alpha / 255, 2)})'   

Color.TRANSPARENT = Color(rgb=(-1, -1, -1), alpha=0)