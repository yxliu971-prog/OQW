from __future__ import annotations
import sys as sys
import traceback as traceback
__all__: list[str] = ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING', 'logger', 'sys', 'traceback']
class logger:
    def critical(self, msg, *args, **kwargs):
        ...
    def debug(self, msg, *args, **kwargs):
        ...
    def error(self, msg, *args, **kwargs):
        ...
    def info(self, msg, *args, **kwargs):
        ...
    def logIt(self, dest, msg, *args, **kwargs):
        ...
    def setLevel(self, val):
        ...
    def warning(self, msg, *args, **kwargs):
        ...
CRITICAL: int = 4
DEBUG: int = 0
ERROR: int = 3
INFO: int = 1
WARNING: int = 2
_levels: list = ['rdApp.debug', 'rdApp.info', 'rdApp.warning', 'rdApp.error']
