# Importando a função do arquivo calculadora/__init__.py
import os
import sys
sys.path.insert(0, os.getcwd())
from projetos.calculadora import calcule
# Executable a aplicação
calcule()
