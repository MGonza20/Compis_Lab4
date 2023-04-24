from sara_compis1_tools.StateAFD import StateAFD
from lexEval import LexEval
from Error import Error

import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'A': 'B', 'B': 'B', 'C': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'a': 'C', 'b': 'C', 'c': 'C', 'A': 'C', 'B': 'C', 'C': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'a': 'C', 'b': 'C', 'c': 'C', 'A': 'C', 'B': 'C', 'C': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', 'x': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'y': 'E'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={'z': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H'},accepting=True,start=False, value='print("Número entero\\n")'),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'0': 'J', '1': 'J', '2': 'J', '3': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={'0': 'J', '1': 'J', '2': 'J', '3': 'J', '.': 'K'},accepting=False,start=False, value=None),StateAFD(name='K',transitions={'0': 'L', '1': 'L', '2': 'L', '3': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'0': 'L', '1': 'L', '2': 'L', '3': 'L'},accepting=True,start=False, value='print("Número decimal\\n")'),StateAFD(name='init',transitions={'ε': 'M'},accepting=False,start=True, value=None),StateAFD(name='M',transitions={'i': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={'f': 'O'},accepting=False,start=False, value=None),StateAFD(name='O',transitions={},accepting=True,start=False, value='print("Palabra reservada: If\\n")'),StateAFD(name='init',transitions={'ε': 'P'},accepting=False,start=True, value=None),StateAFD(name='P',transitions={'f': 'Q'},accepting=False,start=False, value=None),StateAFD(name='Q',transitions={'o': 'R'},accepting=False,start=False, value=None),StateAFD(name='R',transitions={'r': 'S'},accepting=False,start=False, value=None),StateAFD(name='S',transitions={},accepting=True,start=False, value='print("Palabra reservada: For\\n")'),StateAFD(name='init',transitions={'ε': 'T'},accepting=False,start=True, value=None),StateAFD(name='T',transitions={'"': 'U'},accepting=False,start=False, value=None),StateAFD(name='U',transitions={'a': 'U', 'b': 'U', 'c': 'U', 'A': 'U', 'B': 'U', 'C': 'U', '0': 'U', '1': 'U', '2': 'U', '3': 'U', '"': 'V'},accepting=False,start=False, value=None),StateAFD(name='V',transitions={},accepting=True,start=False, value='print("Cadena\\n")')]
errors = set()

if len(sys.argv) < 2:
	print('Por favor ingrese el archivo plano')
	sys.exit(1)
txt_file = sys.argv[1]

lex = LexEval(txt_file)
results = lex.evaluate(mega, errors)
lex.print_tokens(results)

from Visualizer import Visualizer
v = Visualizer()
v.draw_mega_afd(mega)
