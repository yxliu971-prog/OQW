from __future__ import annotations
from _io import StringIO
import glob as glob
import os as os
__all__: list[str] = ['LINEEND', 'StringIO', 'cacheImageFile', 'cachedImageExists', 'glob', 'os', 'preProcessImages']
def _AsciiBase85Decode(input):
    """
    This is not used - Acrobat Reader decodes for you - but a round
          trip is essential for testing.
    """
def _AsciiBase85Encode(input):
    """
    This is a compact encoding used for binary data within
          a PDF file.  Four bytes of binary data become five bytes of
          ASCII.  This is the default method used for encoding images.
    """
def _AsciiBase85Test(text = 'What is the average velocity of a sparrow?'):
    """
    Do the obvious test for whether Base 85 encoding works
    """
def _AsciiHexDecode(input):
    """
    Not used except to provide a test of the preceding
    """
def _AsciiHexEncode(input):
    """
    This is a verbose encoding used for binary data within
          a PDF file.  One byte binary becomes two bytes of ASCII.
    """
def _AsciiHexTest(text = 'What is the average velocity of a sparrow?'):
    """
    Do the obvious test for whether Ascii Hex encoding works
    """
def _escape(s):
    """
    PDF escapes are almost like Python ones, but brackets
          need slashes before them too. Use Python's repr function
          and chop off the quotes first
    """
def _normalizeLineEnds(text, desired = '\r\n'):
    """
    ensures all instances of CR, LF and CRLF end up as the specified one
    """
def _wrap(input, columns = 60):
    ...
def cacheImageFile(filename):
    """
    Processes the image as if for encoding, saves to a file ending in AHX
    """
def cachedImageExists(filename):
    """
    Determines if a cached image exists which has
          the same name and equal or newer date to the given
          file.
    """
def preProcessImages(spec):
    """
    accepts either a filespec ('C:\\mydir\\*.jpg') or a list
          of image filenames, crunches them all to save time.  Run this
          to save huge amounts of time when repeatedly building image
          documents.
    """
LINEEND: str = '\r\n'
