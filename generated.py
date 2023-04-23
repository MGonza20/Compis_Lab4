from sara_compis1_tools.StateAFD import StateAFD
from lexEval import LexEval
from Error import Error

import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'A': 'B', 'B': 'B', 'C': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'A': 'B', 'B': 'B', 'C': 'B', '0': 'B', '1': 'B', '2': 'B', '3': 'B', '4': 'B', '5': 'B', '6': 'B', '7': 'B', '8': 'B', '9': 'B', 'x': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'y': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'z': 'E'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={},accepting=True,start=False, value=''),StateAFD(name='init',transitions={'ε': 'F'},accepting=False,start=True, value=None),StateAFD(name='F',transitions={'0': 'G', '1': 'G', '2': 'G', '3': 'G', '4': 'G', '5': 'G', '6': 'G', '7': 'G', '8': 'G', '9': 'G'},accepting=False,start=False, value=None),StateAFD(name='G',transitions={},accepting=True,start=False, value='print("Entero\\n")'),StateAFD(name='init',transitions={'ε': 'H'},accepting=False,start=True, value=None),StateAFD(name='H',transitions={'0': 'I', '1': 'I', '2': 'I', '3': 'I', '4': 'I', '5': 'I', '6': 'I', '7': 'I', '8': 'I', '9': 'I'},accepting=False,start=False, value=None),StateAFD(name='I',transitions={'0': 'I', '1': 'I', '2': 'I', '3': 'I', '4': 'I', '5': 'I', '6': 'I', '7': 'I', '8': 'I', '9': 'I', '.': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={'0': 'K', '1': 'K', '2': 'K', '3': 'K', '4': 'K', '5': 'K', '6': 'K', '7': 'K', '8': 'K', '9': 'K'},accepting=False,start=False, value=None),StateAFD(name='K',transitions={'0': 'K', '1': 'K', '2': 'K', '3': 'K', '4': 'K', '5': 'K', '6': 'K', '7': 'K', '8': 'K', '9': 'K'},accepting=True,start=False, value='print("Aritmetico\\n")'),StateAFD(name='init',transitions={'ε': 'L'},accepting=False,start=True, value=None),StateAFD(name='L',transitions={'a': 'M', 'b': 'M', 'c': 'M', 'A': 'M', 'B': 'M', 'C': 'M', '0': 'M', '1': 'M', '2': 'M', '3': 'M', '4': 'M', '5': 'M', '6': 'M', '7': 'M', '8': 'M', '9': 'M', ' ': 'M'},accepting=False,start=False, value=None),StateAFD(name='M',transitions={'8': 'M', '9': 'M', ' ': 'M', 'a': 'M', 'b': 'M', 'c': 'M', 'A': 'M', 'B': 'M', 'C': 'M', '0': 'M', '1': 'M', '2': 'M', '3': 'M', '4': 'M', '5': 'M', '6': 'M', '7': 'M'},accepting=True,start=False, value='print("Cadena\\n")')]
errors = set([Error(line=18, error='Error: Token no definido: palabra_reservada_for'),Error(line=19, error='Error: Token no definido: palabra_reservada_while'),Error(line=17, error='Error: Token no definido: palabra_reservada_if')])

if len(sys.argv) < 2:
	print('Por favor ingrese el archivo plano')
	sys.exit(1)
txt_file = sys.argv[1]

lex = LexEval(txt_file)
results = lex.evaluate(mega, errors)
lex.print_tokens(results)
