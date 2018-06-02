import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.DSS import *

def task():
    name = "../resources/short_text_8.txt"
    #result = JHA("../resources/long_text.txt")
    #result1 = JHA(name)
    result2 = DSS(name)



task()
