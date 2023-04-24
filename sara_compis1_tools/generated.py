from sara_compis1_tools.StateAFD import StateAFD
from sara_compis1_tools.lexEval import LexEval
from sara_compis1_tools.Error import Error
import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'd': 'B', 'e': 'B', 'f': 'B', 'g': 'B', 'h': 'B', 'i': 'B', 'j': 'B', 'k': 'B', 'l': 'B', 'm': 'B', 'n': 'B', 'o': 'B', 'p': 'B', 'q': 'B', 'r': 'B', 's': 'B', 't': 'B', 'u': 'B', 'v': 'B', 'w': 'B', 'x': 'B', 'y': 'B', 'z': 'B', 'A': 'B', 'B': 'B', 'C': 'B', 'D': 'B', 'E': 'B', 'F': 'B', 'G': 'B', 'H': 'B', 'I': 'B', 'J': 'B', 'K': 'B', 'L': 'B', 'M': 'B', 'N': 'B', 'O': 'B', 'P': 'B', 'Q': 'B', 'R': 'B', 'S': 'B', 'T': 'B', 'U': 'B', 'V': 'B', 'W': 'B', 'X': 'B', 'Y': 'B', 'Z': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'd': 'B', 'e': 'B', 'f': 'B', 'g': 'B', 'h': 'B', 'i': 'B', 'j': 'B', 'k': 'B', 'l': 'B', 'm': 'B', 'n': 'B', 'o': 'B', 'p': 'B', 'q': 'B', 'r': 'B', 's': 'B', 't': 'B', 'u': 'B', 'v': 'B', 'w': 'B', 'x': 'B', 'y': 'B', 'z': 'B', 'A': 'B', 'B': 'B', 'C': 'B', 'D': 'B', 'E': 'B', 'F': 'B', 'G': 'B', 'H': 'B', 'I': 'B', 'J': 'B', 'K': 'B', 'L': 'B', 'M': 'B', 'N': 'B', 'O': 'B', 'P': 'B', 'Q': 'B', 'R': 'B', 'S': 'B', 'T': 'B', 'U': 'B', 'V': 'B', 'W': 'B', 'X': 'B', 'Y': 'B', 'Z': 'B', '0': 'B', '1': 'B', '2': 'B', '3': 'B', '4': 'B', '5': 'B', '6': 'B', '7': 'B', '8': 'B', '9': 'B'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'C'},accepting=False,start=True, value=None),StateAFD(name='C',transitions={'i': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'f': 'E'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={},accepting=True,start=False, value='print("Palabra reservada: If\\n")'),StateAFD(name='init',transitions={'ε': 'F'},accepting=False,start=True, value=None),StateAFD(name='F',transitions={'f': 'G'},accepting=False,start=False, value=None),StateAFD(name='G',transitions={'o': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'r': 'I'},accepting=False,start=False, value=None),StateAFD(name='I',transitions={},accepting=True,start=False, value='print("Palabra reservada: For\\n")'),StateAFD(name='init',transitions={'ε': 'J'},accepting=False,start=True, value=None),StateAFD(name='J',transitions={'w': 'K'},accepting=False,start=False, value=None),StateAFD(name='K',transitions={'h': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'i': 'M'},accepting=False,start=False, value=None),StateAFD(name='M',transitions={'l': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={'e': 'O'},accepting=False,start=False, value=None),StateAFD(name='O',transitions={},accepting=True,start=False, value='print("Palabra reservada: While\\n")'),StateAFD(name='init',transitions={'ε': 'P'},accepting=False,start=True, value=None),StateAFD(name='P',transitions={'0': 'Q', '1': 'Q', '2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q'},accepting=False,start=False, value=None),StateAFD(name='Q',transitions={'0': 'Q', '1': 'Q', '2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q'},accepting=True,start=False, value='print("Numero entero\\n")'),StateAFD(name='init',transitions={'ε': 'R'},accepting=False,start=True, value=None),StateAFD(name='R',transitions={'+': 'S', '-': 'S', '*': 'S', '/': 'S'},accepting=False,start=False, value=None),StateAFD(name='S',transitions={},accepting=True,start=False, value='print("Operador aritmetico\\n")')]
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
