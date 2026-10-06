"""

This module includes any mathematical methods needed for PIDDLE.
It should have no dependencies beyond the Python library.

So far, just Robert Kern's bezierArc.

"""
from __future__ import annotations
from math import ceil
from math import cos
from math import sin
__all__: list[str] = ['bezierArc', 'ceil', 'cos', 'pi', 'sin']
def bezierArc(x1, y1, x2, y2, startAng = 0, extent = 90):
    """
    bezierArc(x1,y1, x2,y2, startAng=0, extent=90) --> List of Bezier
    curve control points.
    
    (x1, y1) and (x2, y2) are the corners of the enclosing rectangle.  The
    coordinate system has coordinates that increase to the right and down.
    Angles, measured in degress, start with 0 to the right (the positive X
    axis) and increase counter-clockwise.  The arc extends from startAng
    to startAng+extent.  I.e. startAng=0 and extent=180 yields an openside-down
    semi-circle.
    
    The resulting coordinates are of the form (x1,y1, x2,y2, x3,y3, x4,y4)
    such that the curve goes from (x1, y1) to (x4, y4) with (x2, y2) and
    (x3, y3) as their respective Bezier control points.
    """
pi: float = 3.141592653589793
