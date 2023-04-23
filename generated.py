from sara_compis1_tools.StateAFD import StateAFD
from lexEval import LexEval
from Error import Error

import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'b': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'c': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'E'},accepting=False,start=True, value=None),StateAFD(name='E',transitions={' ': 'F', '\t': 'F', '\n': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={' ': 'F', '\t': 'F', '\n': 'F'},accepting=True,start=False, value=''),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'a': 'H', 'b': 'H', 'c': 'H', 'A': 'H', 'B': 'H', 'C': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'a': 'H', 'b': 'H', 'c': 'H', 'A': 'H', 'B': 'H', 'C': 'H', '0': 'H', '1': 'H', '2': 'H', '3': 'H'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'+': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value='print("Operador de suma\\n")'),StateAFD(name='init',transitions={'ε': 'K'},accepting=False,start=True, value=None),StateAFD(name='K',transitions={'*': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={},accepting=True,start=False, value='print("Operador de multiplicación\\n")'),StateAFD(name='init',transitions={'ε': 'M'},accepting=False,start=True, value=None),StateAFD(name='M',transitions={'=': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={},accepting=True,start=False, value='print("Operador de asignación\\n")')]
errors = set()

if len(sys.argv) < 2:
	print('Por favor ingrese el archivo plano')
	sys.exit(1)
txt_file = sys.argv[1]

lex = LexEval(txt_file)
results = lex.evaluate(mega, errors)
lex.print_tokens(results)
