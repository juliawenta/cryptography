import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.lucas import *

def task1():
   result = fast_exponentation_modulo()
   return result

task1()