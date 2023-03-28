# Importanto a função do arquivo calculadora/__init__.py
import os
import sys
sys.path.insert(0, os.getcwd())
from projetos.calculadora.calculadora import calcule
#from calculadora import funcoes
# Executable a aplicação
calcule()
