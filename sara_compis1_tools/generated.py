from sara_compis1_tools.StateAFD import StateAFD
from lexEval import LexEval
from Error import Error

import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'0': 'B', '1': 'B', '2': 'B', '3': 'B', '4': 'B', '5': 'B', '6': 'B', '7': 'B', '8': 'B', '9': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={},accepting=True,start=False, value=''),StateAFD(name='init',transitions={'ε': 'C'},accepting=False,start=True, value=None),StateAFD(name='C',transitions={'0': 'D', '1': 'D', '2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'0': 'D', '1': 'D', '2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '.': 'E'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={'0': 'F', '1': 'F', '2': 'F', '3': 'F', '4': 'F', '5': 'F', '6': 'F', '7': 'F', '8': 'F', '9': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={'0': 'F', '1': 'F', '2': 'F', '3': 'F', '4': 'F', '5': 'F', '6': 'F', '7': 'F', '8': 'F', '9': 'F'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H', '4': 'H', '5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H', 'a': 'H', 'b': 'H', 'c': 'H', 'd': 'H', 'e': 'H', 'f': 'H', 'A': 'H', 'B': 'H', 'C': 'H', 'D': 'H', 'E': 'H', 'F': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H', '4': 'H', '5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H', 'a': 'H', 'b': 'H', 'c': 'H', 'd': 'H', 'e': 'H', 'f': 'H', 'A': 'H', 'B': 'H', 'C': 'H', 'D': 'H', 'E': 'H', 'F': 'H'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'+': 'J', '-': 'J', '*': 'J', '/': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'K'},accepting=False,start=True, value=None),StateAFD(name='K',transitions={'^': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={},accepting=True,start=False, value='print("Identificador\\n")')]
errors = set()

# if len(sys.argv) < 2:
# 	print('Por favor ingrese el archivo plano')
# 	sys.exit(1)
# txt_file = sys.argv[1]

# lex = LexEval(txt_file)
# results = lex.evaluate(mega, errors)
# lex.print_tokens(results)

from Visualizer import Visualizer
v = Visualizer()
v.draw_mega_afd(mega)
