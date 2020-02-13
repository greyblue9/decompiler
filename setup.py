#!/system/bin/python3

from distutils.core import setup


try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

try:
    from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
except ImportError:
    from distutils.command.build_scripts import build_scripts

setup(
  name = "decompiler",
  version = "0.0.00001",
  description = "The decompiler python package",
  author = "Unknown",
  license = "public domain",
  
    packages = ['filters','filters','filters','host','host','host','ir','ir','ir','output','output','host','host','host','host','host','host','host','host','host','host','host'],
    scripts  = ['setup.py','callconv.py','decompiler.py','expressions.py','decompiler_gui.py','graph.py','iterators.py','objdump-decompiler.py','propagator.py','pruner.py','renamer.py','ssa.py','statements.py'],

  cmdclass = { 'build_py': build_py, 'build_scripts': build_scripts }
)


