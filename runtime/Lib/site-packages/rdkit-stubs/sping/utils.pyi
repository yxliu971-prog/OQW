from __future__ import annotations
__all__: list[str] = ['availableCanvases']
availableCanvases: dict = {'pdf': ('PDF.pidPDF', 'PDFCanvas', 'PDF'), 'ps': ('PS.pidPS', 'PSCanvas', 'PS'), 'svg': ('SVG.pidSVG', 'SVGCanvas', 'SVG'), 'jpg': ('PIL.pidPIL', 'PILCanvas', 'JPEG'), 'png': ('PIL.pidPIL', 'PILCanvas', 'PNG')}
