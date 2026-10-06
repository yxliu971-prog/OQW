from __future__ import annotations
import os as os
import sys as sys
import typing
__all__: list[str] = ['BUILD_TYPE_ENVVAR', 'OutputRedirectC', 'isDebugBuild', 'os', 'redirect_stderr', 'redirect_stdout', 'sys']
class OutputRedirectC:
    """
    Context manager which uses low-level file descriptors to suppress
      output to stdout/stderr, optionally redirecting to the named file(s).
    
      Suppress all output
      with Silence():
        <code>
    
      Redirect stdout to file
      with OutputRedirectC(stdout='output.txt', mode='w'):
        <code>
    
      Redirect stderr to file
      with OutputRedirectC(stderr='output.txt', mode='a'):
        <code>
      http://code.activestate.com/recipes/577564-context-manager-for-low-level-redirection-of-stdou/
      >>>
    
      
    """
    def __enter__(self):
        ...
    def __exit__(self, *args):
        ...
    def __init__(self, stdout = 'nul', stderr = 'nul', mode = 'wb'):
        ...
class _RedirectStream:
    _stream = None
    def __enter__(self):
        ...
    def __exit__(self, exctype, excinst, exctb):
        ...
    def __init__(self, new_target):
        ...
class redirect_stderr(_RedirectStream):
    """
    Context manager for temporarily redirecting stderr to another file.
    """
    _stream: typing.ClassVar[str] = 'stderr'
class redirect_stdout(_RedirectStream):
    """
    Context manager for temporarily redirecting stdout to another file.
    
            # How to send help() to stderr
            with redirect_stdout(sys.stderr):
                help(dir)
    
            # How to write help() to a file
            with open('help.txt', 'w') as f:
                with redirect_stdout(f):
                    help(pow)
        
    """
    _stream: typing.ClassVar[str] = 'stdout'
def isDebugBuild():
    ...
BUILD_TYPE_ENVVAR: str = 'RDKIT_BUILD_TYPE'
