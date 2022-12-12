class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    def __init__(self, red, green, blue) -> None:
        self.initialization(red, green, blue)
    
    def __str__(self) -> str:
        return (f'{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}')
    
    def __eq__(self, other: object) -> bool:
        if self.r == other.r and self.b == other.b and self.g == other.g:
            return True
        return False
    
    def __rmul__(self, contrast):
        if not isinstance(contrast, float) or not 0 <= contrast <= 1:
            raise ValueError('wrong walue')
        cl = -256 * (1 - contrast)
        f = (259 * (cl + 255)) / (255 * (259 - cl))
        r = round(f * (self.r - 128) + 128)
        g = round(f * (self.g - 128) + 128)
        b = round(f * (self.b - 128) + 128)
        return Color(r, g, b)
    
    def initialization(self, red, green, blue):
        if not isinstance(red, int) or not isinstance(green, int) or not isinstance(blue, int):
            raise ValueError('color must be int')
        if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
            self.r = red
            self.b = blue
            self.g = green
        else:
            raise ValueError('value must be between 0 and 255')
    



if __name__ == '__main__':
    dot = Color(255, 0, 0)
    dot1 = Color(155, 12, 43)
    print(0.5 * dot)