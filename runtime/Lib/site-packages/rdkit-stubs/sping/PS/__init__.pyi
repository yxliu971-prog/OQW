from __future__ import annotations
from _io import StringIO
import math as math
from rdkit.sping.PS.pidPS import EpsDSC
from rdkit.sping.PS.pidPS import PSCanvas
from rdkit.sping.PS.pidPS import PostScriptLevelException
from rdkit.sping.PS.pidPS import PsDSC
from rdkit.sping.PS.pidPS import dashLineDefinition
from rdkit.sping.PS.pidPS import latin1FontEncoding
import rdkit.sping.colors
from rdkit.sping.colors import Color
from rdkit.sping.colors import HexColor
from rdkit.sping.pid import AffineMatrix
from rdkit.sping.pid import Canvas
from rdkit.sping.pid import Font
from rdkit.sping.pid import StateSaver
from rdkit.sping.pid import getFileObject
from .fontinfo import *
from .latin1MetricsCache import *
from .pidPS import *
from .psmetrics import *
__all__: list[str] = ['AffineMatrix', 'Bold', 'Canvas', 'Color', 'EpsDSC', 'Font', 'HexColor', 'Italic', 'PSCanvas', 'PSFontMapLatin1Enc', 'PSFontMapStdEnc', 'PiddleLegalFonts', 'PostScriptLevelException', 'PsDSC', 'Roman', 'StateSaver', 'StringIO', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'cm', 'coral', 'cornflower', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'dashLineDefinition', 'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue', 'figureArc', 'figureCurve', 'figureLine', 'firebrick', 'floralwhite', 'fontinfo', 'forestgreen', 'fuchsia', 'gainsboro', 'getFileObject', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'inch', 'indianred', 'indigo', 'ivory', 'keyBksp', 'keyClear', 'keyDel', 'keyDown', 'keyEnd', 'keyHome', 'keyLeft', 'keyPgDn', 'keyPgUp', 'keyRight', 'keyTab', 'keyUp', 'khaki', 'latin1FontEncoding', 'latin1MetricsCache', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'linesep', 'magenta', 'maroon', 'math', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'modControl', 'modShift', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pidPS', 'pink', 'plum', 'powderblue', 'psmetrics', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'transparent', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']
Bold: str = 'Bold'
Italic: str = 'Italic'
PSFontMapLatin1Enc: dict = {('helvetica', 'Roman'): 'Helvetica-Roman-ISOLatin1', ('helvetica', 'Bold'): 'Helvetica-Bold-ISOLatin1', ('helvetica', 'Italic'): 'Helvetica-Oblique-ISOLatin1', ('times', 'Roman'): 'Times-Roman-ISOLatin1', ('times', 'Bold'): 'Times-Bold-ISOLatin1', ('times', 'Italic'): 'Times-Italic-ISOLatin1', ('courier', 'Roman'): 'Courier-Roman-ISOLatin1', ('courier', 'Bold'): 'Courier-Bold-ISOLatin1', ('courier', 'Italic'): 'Courier-Oblique-ISOLatin1', ('symbol', 'Roman'): 'Symbol', ('symbol', 'Bold'): 'Symbol', ('symbol', 'Italic'): 'Symbol', 'EncodingName': 'Latin1Encoding'}
PSFontMapStdEnc: dict = {('helvetica', 'Roman'): 'Helvetica-Roman', ('helvetica', 'Bold'): 'Helvetica-Bold', ('helvetica', 'Italic'): 'Helvetica-Oblique', ('times', 'Roman'): 'Times-Roman', ('times', 'Bold'): 'Times-Bold', ('times', 'Italic'): 'Times-Italic', ('courier', 'Roman'): 'Courier-Roman', ('courier', 'Bold'): 'Courier-Bold', ('courier', 'Italic'): 'Courier-Oblique', ('symbol', 'Roman'): 'Symbol', ('symbol', 'Bold'): 'Symbol', ('symbol', 'Italic'): 'Symbol', 'EncodingName': 'StandardEncoding'}
PiddleLegalFonts: dict = {'helvetica': 'helvetica', 'times': 'times', 'courier': 'courier', 'serif': 'times', 'sansserif': 'helvetica', 'monospaced': 'courier', 'symbol': 'symbol'}
Roman: str = 'Roman'
aliceblue: rdkit.sping.colors.Color  # value = Color(0.94,0.97,1.00)
antiquewhite: rdkit.sping.colors.Color  # value = Color(0.98,0.92,0.84)
aqua: rdkit.sping.colors.Color  # value = Color(0.00,1.00,1.00)
aquamarine: rdkit.sping.colors.Color  # value = Color(0.50,1.00,0.83)
azure: rdkit.sping.colors.Color  # value = Color(0.94,1.00,1.00)
beige: rdkit.sping.colors.Color  # value = Color(0.96,0.96,0.86)
bisque: rdkit.sping.colors.Color  # value = Color(1.00,0.89,0.77)
black: rdkit.sping.colors.Color  # value = Color(0.00,0.00,0.00)
blanchedalmond: rdkit.sping.colors.Color  # value = Color(1.00,0.92,0.80)
blue: rdkit.sping.colors.Color  # value = Color(0.00,0.00,1.00)
blueviolet: rdkit.sping.colors.Color  # value = Color(0.54,0.17,0.89)
brown: rdkit.sping.colors.Color  # value = Color(0.65,0.16,0.16)
burlywood: rdkit.sping.colors.Color  # value = Color(0.87,0.72,0.53)
cadetblue: rdkit.sping.colors.Color  # value = Color(0.37,0.62,0.63)
chartreuse: rdkit.sping.colors.Color  # value = Color(0.50,1.00,0.00)
chocolate: rdkit.sping.colors.Color  # value = Color(0.82,0.41,0.12)
cm: float = 28.346456692913385
coral: rdkit.sping.colors.Color  # value = Color(1.00,0.50,0.31)
cornflower: rdkit.sping.colors.Color  # value = Color(0.39,0.58,0.93)
cornsilk: rdkit.sping.colors.Color  # value = Color(1.00,0.97,0.86)
crimson: rdkit.sping.colors.Color  # value = Color(0.86,0.08,0.24)
cyan: rdkit.sping.colors.Color  # value = Color(0.00,1.00,1.00)
darkblue: rdkit.sping.colors.Color  # value = Color(0.00,0.00,0.55)
darkcyan: rdkit.sping.colors.Color  # value = Color(0.00,0.55,0.55)
darkgoldenrod: rdkit.sping.colors.Color  # value = Color(0.72,0.53,0.04)
darkgray: rdkit.sping.colors.Color  # value = Color(0.66,0.66,0.66)
darkgreen: rdkit.sping.colors.Color  # value = Color(0.00,0.39,0.00)
darkkhaki: rdkit.sping.colors.Color  # value = Color(0.74,0.72,0.42)
darkmagenta: rdkit.sping.colors.Color  # value = Color(0.55,0.00,0.55)
darkolivegreen: rdkit.sping.colors.Color  # value = Color(0.33,0.42,0.18)
darkorange: rdkit.sping.colors.Color  # value = Color(1.00,0.55,0.00)
darkorchid: rdkit.sping.colors.Color  # value = Color(0.60,0.20,0.80)
darkred: rdkit.sping.colors.Color  # value = Color(0.55,0.00,0.00)
darksalmon: rdkit.sping.colors.Color  # value = Color(0.91,0.59,0.48)
darkseagreen: rdkit.sping.colors.Color  # value = Color(0.56,0.74,0.55)
darkslateblue: rdkit.sping.colors.Color  # value = Color(0.28,0.24,0.55)
darkslategray: rdkit.sping.colors.Color  # value = Color(0.18,0.31,0.31)
darkturquoise: rdkit.sping.colors.Color  # value = Color(0.00,0.81,0.82)
darkviolet: rdkit.sping.colors.Color  # value = Color(0.58,0.00,0.83)
deeppink: rdkit.sping.colors.Color  # value = Color(1.00,0.08,0.58)
deepskyblue: rdkit.sping.colors.Color  # value = Color(0.00,0.75,1.00)
dimgray: rdkit.sping.colors.Color  # value = Color(0.41,0.41,0.41)
dodgerblue: rdkit.sping.colors.Color  # value = Color(0.12,0.56,1.00)
figureArc: int = 2
figureCurve: int = 3
figureLine: int = 1
firebrick: rdkit.sping.colors.Color  # value = Color(0.70,0.13,0.13)
floralwhite: rdkit.sping.colors.Color  # value = Color(1.00,0.98,0.94)
forestgreen: rdkit.sping.colors.Color  # value = Color(0.13,0.55,0.13)
fuchsia: rdkit.sping.colors.Color  # value = Color(1.00,0.00,1.00)
gainsboro: rdkit.sping.colors.Color  # value = Color(0.86,0.86,0.86)
ghostwhite: rdkit.sping.colors.Color  # value = Color(0.97,0.97,1.00)
gold: rdkit.sping.colors.Color  # value = Color(1.00,0.84,0.00)
goldenrod: rdkit.sping.colors.Color  # value = Color(0.85,0.65,0.13)
gray: rdkit.sping.colors.Color  # value = Color(0.50,0.50,0.50)
green: rdkit.sping.colors.Color  # value = Color(0.00,0.50,0.00)
greenyellow: rdkit.sping.colors.Color  # value = Color(0.68,1.00,0.18)
grey: rdkit.sping.colors.Color  # value = Color(0.50,0.50,0.50)
honeydew: rdkit.sping.colors.Color  # value = Color(0.94,1.00,0.94)
hotpink: rdkit.sping.colors.Color  # value = Color(1.00,0.41,0.71)
inch: int = 72
indianred: rdkit.sping.colors.Color  # value = Color(0.80,0.36,0.36)
indigo: rdkit.sping.colors.Color  # value = Color(0.29,0.00,0.51)
ivory: rdkit.sping.colors.Color  # value = Color(1.00,1.00,0.94)
keyBksp: str = '\x08'
keyClear: str = '\x1b'
keyDel: str = '\x7f'
keyDown: str = '\x1f'
keyEnd: str = '\x04'
keyHome: str = '\x01'
keyLeft: str = '\x1c'
keyPgDn: str = '\x0c'
keyPgUp: str = '\x0b'
keyRight: str = '\x1d'
keyTab: str = '\t'
keyUp: str = '\x1e'
khaki: rdkit.sping.colors.Color  # value = Color(0.94,0.90,0.55)
lavender: rdkit.sping.colors.Color  # value = Color(0.90,0.90,0.98)
lavenderblush: rdkit.sping.colors.Color  # value = Color(1.00,0.94,0.96)
lawngreen: rdkit.sping.colors.Color  # value = Color(0.49,0.99,0.00)
lemonchiffon: rdkit.sping.colors.Color  # value = Color(1.00,0.98,0.80)
lightblue: rdkit.sping.colors.Color  # value = Color(0.68,0.85,0.90)
lightcoral: rdkit.sping.colors.Color  # value = Color(0.94,0.50,0.50)
lightcyan: rdkit.sping.colors.Color  # value = Color(0.88,1.00,1.00)
lightgoldenrodyellow: rdkit.sping.colors.Color  # value = Color(0.98,0.98,0.82)
lightgreen: rdkit.sping.colors.Color  # value = Color(0.56,0.93,0.56)
lightgrey: rdkit.sping.colors.Color  # value = Color(0.83,0.83,0.83)
lightpink: rdkit.sping.colors.Color  # value = Color(1.00,0.71,0.76)
lightsalmon: rdkit.sping.colors.Color  # value = Color(1.00,0.63,0.48)
lightseagreen: rdkit.sping.colors.Color  # value = Color(0.13,0.70,0.67)
lightskyblue: rdkit.sping.colors.Color  # value = Color(0.53,0.81,0.98)
lightslategray: rdkit.sping.colors.Color  # value = Color(0.47,0.53,0.60)
lightsteelblue: rdkit.sping.colors.Color  # value = Color(0.69,0.77,0.87)
lightyellow: rdkit.sping.colors.Color  # value = Color(1.00,1.00,0.88)
lime: rdkit.sping.colors.Color  # value = Color(0.00,1.00,0.00)
limegreen: rdkit.sping.colors.Color  # value = Color(0.20,0.80,0.20)
linen: rdkit.sping.colors.Color  # value = Color(0.98,0.94,0.90)
linesep: str = '\n'
magenta: rdkit.sping.colors.Color  # value = Color(1.00,0.00,1.00)
maroon: rdkit.sping.colors.Color  # value = Color(0.50,0.00,0.00)
mediumaquamarine: rdkit.sping.colors.Color  # value = Color(0.40,0.80,0.67)
mediumblue: rdkit.sping.colors.Color  # value = Color(0.00,0.00,0.80)
mediumorchid: rdkit.sping.colors.Color  # value = Color(0.73,0.33,0.83)
mediumpurple: rdkit.sping.colors.Color  # value = Color(0.58,0.44,0.86)
mediumseagreen: rdkit.sping.colors.Color  # value = Color(0.24,0.70,0.44)
mediumslateblue: rdkit.sping.colors.Color  # value = Color(0.48,0.41,0.93)
mediumspringgreen: rdkit.sping.colors.Color  # value = Color(0.00,0.98,0.60)
mediumturquoise: rdkit.sping.colors.Color  # value = Color(0.28,0.82,0.80)
mediumvioletred: rdkit.sping.colors.Color  # value = Color(0.78,0.08,0.52)
midnightblue: rdkit.sping.colors.Color  # value = Color(0.10,0.10,0.44)
mintcream: rdkit.sping.colors.Color  # value = Color(0.96,1.00,0.98)
mistyrose: rdkit.sping.colors.Color  # value = Color(1.00,0.89,0.88)
moccasin: rdkit.sping.colors.Color  # value = Color(1.00,0.89,0.71)
modControl: int = 2
modShift: int = 1
navajowhite: rdkit.sping.colors.Color  # value = Color(1.00,0.87,0.68)
navy: rdkit.sping.colors.Color  # value = Color(0.00,0.00,0.50)
oldlace: rdkit.sping.colors.Color  # value = Color(0.99,0.96,0.90)
olive: rdkit.sping.colors.Color  # value = Color(0.50,0.50,0.00)
olivedrab: rdkit.sping.colors.Color  # value = Color(0.42,0.56,0.14)
orange: rdkit.sping.colors.Color  # value = Color(1.00,0.65,0.00)
orangered: rdkit.sping.colors.Color  # value = Color(1.00,0.27,0.00)
orchid: rdkit.sping.colors.Color  # value = Color(0.85,0.44,0.84)
palegoldenrod: rdkit.sping.colors.Color  # value = Color(0.93,0.91,0.67)
palegreen: rdkit.sping.colors.Color  # value = Color(0.60,0.98,0.60)
paleturquoise: rdkit.sping.colors.Color  # value = Color(0.69,0.93,0.93)
palevioletred: rdkit.sping.colors.Color  # value = Color(0.86,0.44,0.58)
papayawhip: rdkit.sping.colors.Color  # value = Color(1.00,0.94,0.84)
peachpuff: rdkit.sping.colors.Color  # value = Color(1.00,0.85,0.73)
peru: rdkit.sping.colors.Color  # value = Color(0.80,0.52,0.25)
pink: rdkit.sping.colors.Color  # value = Color(1.00,0.75,0.80)
plum: rdkit.sping.colors.Color  # value = Color(0.87,0.63,0.87)
powderblue: rdkit.sping.colors.Color  # value = Color(0.69,0.88,0.90)
purple: rdkit.sping.colors.Color  # value = Color(0.50,0.00,0.50)
red: rdkit.sping.colors.Color  # value = Color(1.00,0.00,0.00)
rosybrown: rdkit.sping.colors.Color  # value = Color(0.74,0.56,0.56)
royalblue: rdkit.sping.colors.Color  # value = Color(0.25,0.41,0.88)
saddlebrown: rdkit.sping.colors.Color  # value = Color(0.55,0.27,0.07)
salmon: rdkit.sping.colors.Color  # value = Color(0.98,0.50,0.45)
sandybrown: rdkit.sping.colors.Color  # value = Color(0.96,0.64,0.38)
seagreen: rdkit.sping.colors.Color  # value = Color(0.18,0.55,0.34)
seashell: rdkit.sping.colors.Color  # value = Color(1.00,0.96,0.93)
sienna: rdkit.sping.colors.Color  # value = Color(0.63,0.32,0.18)
silver: rdkit.sping.colors.Color  # value = Color(0.75,0.75,0.75)
skyblue: rdkit.sping.colors.Color  # value = Color(0.53,0.81,0.92)
slateblue: rdkit.sping.colors.Color  # value = Color(0.42,0.35,0.80)
slategray: rdkit.sping.colors.Color  # value = Color(0.44,0.50,0.56)
snow: rdkit.sping.colors.Color  # value = Color(1.00,0.98,0.98)
springgreen: rdkit.sping.colors.Color  # value = Color(0.00,1.00,0.50)
steelblue: rdkit.sping.colors.Color  # value = Color(0.27,0.51,0.71)
tan: rdkit.sping.colors.Color  # value = Color(0.82,0.71,0.55)
teal: rdkit.sping.colors.Color  # value = Color(0.00,0.50,0.50)
thistle: rdkit.sping.colors.Color  # value = Color(0.85,0.75,0.85)
tomato: rdkit.sping.colors.Color  # value = Color(1.00,0.39,0.28)
transparent: rdkit.sping.colors.Color  # value = Color(-1.00,-1.00,-1.00)
turquoise: rdkit.sping.colors.Color  # value = Color(0.25,0.88,0.82)
violet: rdkit.sping.colors.Color  # value = Color(0.93,0.51,0.93)
wheat: rdkit.sping.colors.Color  # value = Color(0.96,0.87,0.70)
white: rdkit.sping.colors.Color  # value = Color(1.00,1.00,1.00)
whitesmoke: rdkit.sping.colors.Color  # value = Color(0.96,0.96,0.96)
yellow: rdkit.sping.colors.Color  # value = Color(1.00,1.00,0.00)
yellowgreen: rdkit.sping.colors.Color  # value = Color(0.60,0.80,0.20)
