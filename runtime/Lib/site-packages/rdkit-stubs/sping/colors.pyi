from __future__ import annotations
__all__: list[str] = ['Color', 'HexColor', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflower', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'transparent', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']
class Color:
    """
    This class is used to represent color.  Components red, green, blue 
              are in the range 0 (dark) to 1 (full intensity).
    """
    def __add__(self, x):
        ...
    def __cmp__(self, other):
        ...
    def __div__(self, x):
        ...
    def __hash__(self):
        ...
    def __init__(self, red = 0, green = 0, blue = 0):
        """
        Initialize with red, green, blue in range [0-1].
        """
    def __mul__(self, x):
        ...
    def __rdiv__(self, x):
        ...
    def __repr__(self):
        ...
    def __rmul__(self, x):
        ...
    def __setattr__(self, name, value):
        ...
    def __sub__(self, x):
        ...
    def __truediv__(self, x):
        ...
    def toHexRGB(self):
        """
        Convert the color back to an integer suitable for the 
        """
    def toHexStr(self):
        ...
def HexColor(val):
    """
    This class converts a hex string, or an actual integer number,
              into the corresponding color.  E.g., in "AABBCC" or 0xAABBCC,
              AA is the red, BB is the green, and CC is the blue (00-FF).
    """
aliceblue: Color  # value = Color(0.94,0.97,1.00)
antiquewhite: Color  # value = Color(0.98,0.92,0.84)
aqua: Color  # value = Color(0.00,1.00,1.00)
aquamarine: Color  # value = Color(0.50,1.00,0.83)
azure: Color  # value = Color(0.94,1.00,1.00)
beige: Color  # value = Color(0.96,0.96,0.86)
bisque: Color  # value = Color(1.00,0.89,0.77)
black: Color  # value = Color(0.00,0.00,0.00)
blanchedalmond: Color  # value = Color(1.00,0.92,0.80)
blue: Color  # value = Color(0.00,0.00,1.00)
blueviolet: Color  # value = Color(0.54,0.17,0.89)
brown: Color  # value = Color(0.65,0.16,0.16)
burlywood: Color  # value = Color(0.87,0.72,0.53)
cadetblue: Color  # value = Color(0.37,0.62,0.63)
chartreuse: Color  # value = Color(0.50,1.00,0.00)
chocolate: Color  # value = Color(0.82,0.41,0.12)
coral: Color  # value = Color(1.00,0.50,0.31)
cornflower: Color  # value = Color(0.39,0.58,0.93)
cornsilk: Color  # value = Color(1.00,0.97,0.86)
crimson: Color  # value = Color(0.86,0.08,0.24)
cyan: Color  # value = Color(0.00,1.00,1.00)
darkblue: Color  # value = Color(0.00,0.00,0.55)
darkcyan: Color  # value = Color(0.00,0.55,0.55)
darkgoldenrod: Color  # value = Color(0.72,0.53,0.04)
darkgray: Color  # value = Color(0.66,0.66,0.66)
darkgreen: Color  # value = Color(0.00,0.39,0.00)
darkkhaki: Color  # value = Color(0.74,0.72,0.42)
darkmagenta: Color  # value = Color(0.55,0.00,0.55)
darkolivegreen: Color  # value = Color(0.33,0.42,0.18)
darkorange: Color  # value = Color(1.00,0.55,0.00)
darkorchid: Color  # value = Color(0.60,0.20,0.80)
darkred: Color  # value = Color(0.55,0.00,0.00)
darksalmon: Color  # value = Color(0.91,0.59,0.48)
darkseagreen: Color  # value = Color(0.56,0.74,0.55)
darkslateblue: Color  # value = Color(0.28,0.24,0.55)
darkslategray: Color  # value = Color(0.18,0.31,0.31)
darkturquoise: Color  # value = Color(0.00,0.81,0.82)
darkviolet: Color  # value = Color(0.58,0.00,0.83)
deeppink: Color  # value = Color(1.00,0.08,0.58)
deepskyblue: Color  # value = Color(0.00,0.75,1.00)
dimgray: Color  # value = Color(0.41,0.41,0.41)
dodgerblue: Color  # value = Color(0.12,0.56,1.00)
firebrick: Color  # value = Color(0.70,0.13,0.13)
floralwhite: Color  # value = Color(1.00,0.98,0.94)
forestgreen: Color  # value = Color(0.13,0.55,0.13)
fuchsia: Color  # value = Color(1.00,0.00,1.00)
gainsboro: Color  # value = Color(0.86,0.86,0.86)
ghostwhite: Color  # value = Color(0.97,0.97,1.00)
gold: Color  # value = Color(1.00,0.84,0.00)
goldenrod: Color  # value = Color(0.85,0.65,0.13)
gray: Color  # value = Color(0.50,0.50,0.50)
green: Color  # value = Color(0.00,0.50,0.00)
greenyellow: Color  # value = Color(0.68,1.00,0.18)
grey: Color  # value = Color(0.50,0.50,0.50)
honeydew: Color  # value = Color(0.94,1.00,0.94)
hotpink: Color  # value = Color(1.00,0.41,0.71)
indianred: Color  # value = Color(0.80,0.36,0.36)
indigo: Color  # value = Color(0.29,0.00,0.51)
ivory: Color  # value = Color(1.00,1.00,0.94)
khaki: Color  # value = Color(0.94,0.90,0.55)
lavender: Color  # value = Color(0.90,0.90,0.98)
lavenderblush: Color  # value = Color(1.00,0.94,0.96)
lawngreen: Color  # value = Color(0.49,0.99,0.00)
lemonchiffon: Color  # value = Color(1.00,0.98,0.80)
lightblue: Color  # value = Color(0.68,0.85,0.90)
lightcoral: Color  # value = Color(0.94,0.50,0.50)
lightcyan: Color  # value = Color(0.88,1.00,1.00)
lightgoldenrodyellow: Color  # value = Color(0.98,0.98,0.82)
lightgreen: Color  # value = Color(0.56,0.93,0.56)
lightgrey: Color  # value = Color(0.83,0.83,0.83)
lightpink: Color  # value = Color(1.00,0.71,0.76)
lightsalmon: Color  # value = Color(1.00,0.63,0.48)
lightseagreen: Color  # value = Color(0.13,0.70,0.67)
lightskyblue: Color  # value = Color(0.53,0.81,0.98)
lightslategray: Color  # value = Color(0.47,0.53,0.60)
lightsteelblue: Color  # value = Color(0.69,0.77,0.87)
lightyellow: Color  # value = Color(1.00,1.00,0.88)
lime: Color  # value = Color(0.00,1.00,0.00)
limegreen: Color  # value = Color(0.20,0.80,0.20)
linen: Color  # value = Color(0.98,0.94,0.90)
magenta: Color  # value = Color(1.00,0.00,1.00)
maroon: Color  # value = Color(0.50,0.00,0.00)
mediumaquamarine: Color  # value = Color(0.40,0.80,0.67)
mediumblue: Color  # value = Color(0.00,0.00,0.80)
mediumorchid: Color  # value = Color(0.73,0.33,0.83)
mediumpurple: Color  # value = Color(0.58,0.44,0.86)
mediumseagreen: Color  # value = Color(0.24,0.70,0.44)
mediumslateblue: Color  # value = Color(0.48,0.41,0.93)
mediumspringgreen: Color  # value = Color(0.00,0.98,0.60)
mediumturquoise: Color  # value = Color(0.28,0.82,0.80)
mediumvioletred: Color  # value = Color(0.78,0.08,0.52)
midnightblue: Color  # value = Color(0.10,0.10,0.44)
mintcream: Color  # value = Color(0.96,1.00,0.98)
mistyrose: Color  # value = Color(1.00,0.89,0.88)
moccasin: Color  # value = Color(1.00,0.89,0.71)
navajowhite: Color  # value = Color(1.00,0.87,0.68)
navy: Color  # value = Color(0.00,0.00,0.50)
oldlace: Color  # value = Color(0.99,0.96,0.90)
olive: Color  # value = Color(0.50,0.50,0.00)
olivedrab: Color  # value = Color(0.42,0.56,0.14)
orange: Color  # value = Color(1.00,0.65,0.00)
orangered: Color  # value = Color(1.00,0.27,0.00)
orchid: Color  # value = Color(0.85,0.44,0.84)
palegoldenrod: Color  # value = Color(0.93,0.91,0.67)
palegreen: Color  # value = Color(0.60,0.98,0.60)
paleturquoise: Color  # value = Color(0.69,0.93,0.93)
palevioletred: Color  # value = Color(0.86,0.44,0.58)
papayawhip: Color  # value = Color(1.00,0.94,0.84)
peachpuff: Color  # value = Color(1.00,0.85,0.73)
peru: Color  # value = Color(0.80,0.52,0.25)
pink: Color  # value = Color(1.00,0.75,0.80)
plum: Color  # value = Color(0.87,0.63,0.87)
powderblue: Color  # value = Color(0.69,0.88,0.90)
purple: Color  # value = Color(0.50,0.00,0.50)
red: Color  # value = Color(1.00,0.00,0.00)
rosybrown: Color  # value = Color(0.74,0.56,0.56)
royalblue: Color  # value = Color(0.25,0.41,0.88)
saddlebrown: Color  # value = Color(0.55,0.27,0.07)
salmon: Color  # value = Color(0.98,0.50,0.45)
sandybrown: Color  # value = Color(0.96,0.64,0.38)
seagreen: Color  # value = Color(0.18,0.55,0.34)
seashell: Color  # value = Color(1.00,0.96,0.93)
sienna: Color  # value = Color(0.63,0.32,0.18)
silver: Color  # value = Color(0.75,0.75,0.75)
skyblue: Color  # value = Color(0.53,0.81,0.92)
slateblue: Color  # value = Color(0.42,0.35,0.80)
slategray: Color  # value = Color(0.44,0.50,0.56)
snow: Color  # value = Color(1.00,0.98,0.98)
springgreen: Color  # value = Color(0.00,1.00,0.50)
steelblue: Color  # value = Color(0.27,0.51,0.71)
tan: Color  # value = Color(0.82,0.71,0.55)
teal: Color  # value = Color(0.00,0.50,0.50)
thistle: Color  # value = Color(0.85,0.75,0.85)
tomato: Color  # value = Color(1.00,0.39,0.28)
transparent: Color  # value = Color(-1.00,-1.00,-1.00)
turquoise: Color  # value = Color(0.25,0.88,0.82)
violet: Color  # value = Color(0.93,0.51,0.93)
wheat: Color  # value = Color(0.96,0.87,0.70)
white: Color  # value = Color(1.00,1.00,1.00)
whitesmoke: Color  # value = Color(0.96,0.96,0.96)
yellow: Color  # value = Color(1.00,1.00,0.00)
yellowgreen: Color  # value = Color(0.60,0.80,0.20)
