from sara_compis1_tools.StateAFD import StateAFD
from sara_compis1_tools.lexEval import LexEval
from sara_compis1_tools.Error import Error
import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'f': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'o': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'r': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={},accepting=True,start=False, value='print("Palabra reservada: For\\n")'),StateAFD(name='init',transitions={'ε': 'E'},accepting=False,start=True, value=None),StateAFD(name='E',transitions={'w': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={'h': 'G'},accepting=False,start=False, value=None),StateAFD(name='G',transitions={'i': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'l': 'I'},accepting=False,start=False, value=None),StateAFD(name='I',transitions={'e': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value='print("Palabra reservada: While\\n")'),StateAFD(name='init',transitions={'ε': 'K'},accepting=False,start=True, value=None),StateAFD(name='K',transitions={'i': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'f': 'M'},accepting=False,start=False, value=None),StateAFD(name='M',transitions={},accepting=True,start=False, value='print("Palabra reservada: If\\n")'),StateAFD(name='init',transitions={'ε': 'N'},accepting=False,start=True, value=None),StateAFD(name='N',transitions={'a': 'O', 'b': 'O', 'c': 'O', 'd': 'O', 'e': 'O', 'f': 'O', 'g': 'O', 'h': 'O', 'i': 'O', 'j': 'O', 'k': 'O', 'l': 'O', 'm': 'O', 'n': 'O', 'o': 'O', 'p': 'O', 'q': 'O', 'r': 'O', 's': 'O', 't': 'O', 'u': 'O', 'v': 'O', 'w': 'O', 'x': 'O', 'y': 'O', 'z': 'O', 'A': 'O', 'B': 'O', 'C': 'O', 'D': 'O', 'E': 'O', 'F': 'O', 'G': 'O', 'H': 'O', 'I': 'O', 'J': 'O', 'K': 'O', 'L': 'O', 'M': 'O', 'N': 'O', 'O': 'O', 'P': 'O', 'Q': 'O', 'R': 'O', 'S': 'O', 'T': 'O', 'U': 'O', 'V': 'O', 'W': 'O', 'X': 'O', 'Y': 'O', 'Z': 'O'},accepting=False,start=False, value=None),StateAFD(name='O',transitions={'a': 'O', 'b': 'O', 'c': 'O', 'd': 'O', 'e': 'O', 'f': 'O', 'g': 'O', 'h': 'O', 'i': 'O', 'j': 'O', 'k': 'O', 'l': 'O', 'm': 'O', 'n': 'O', 'o': 'O', 'p': 'O', 'q': 'O', 'r': 'O', 's': 'O', 't': 'O', 'u': 'O', 'v': 'O', 'w': 'O', 'x': 'O', 'y': 'O', 'z': 'O', 'A': 'O', 'B': 'O', 'C': 'O', 'D': 'O', 'E': 'O', 'F': 'O', 'G': 'O', 'H': 'O', 'I': 'O', 'J': 'O', 'K': 'O', 'L': 'O', 'M': 'O', 'N': 'O', 'O': 'O', 'P': 'O', 'Q': 'O', 'R': 'O', 'S': 'O', 'T': 'O', 'U': 'O', 'V': 'O', 'W': 'O', 'X': 'O', 'Y': 'O', 'Z': 'O', '0': 'O', '1': 'O', '2': 'O', '3': 'O', '4': 'O', '5': 'O', '6': 'O', '7': 'O', '8': 'O', '9': 'O'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'P'},accepting=False,start=True, value=None),StateAFD(name='P',transitions={'0': 'Q', '1': 'Q', '2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q'},accepting=False,start=False, value=None),StateAFD(name='Q',transitions={'0': 'Q', '1': 'Q', '2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q'},accepting=True,start=False, value='print("Numero entero\\n")'),StateAFD(name='init',transitions={'ε': 'R'},accepting=False,start=True, value=None),StateAFD(name='R',transitions={'+': 'S', '-': 'S', '*': 'S', '/': 'S'},accepting=False,start=False, value=None),StateAFD(name='S',transitions={},accepting=True,start=False, value='print("Operador aritmetico\\n")')]
errors = set()

if len(sys.argv) < 2:
	print('Por favor ingrese el archivo plano')
	sys.exit(1)
txt_file = sys.argv[1]

lex = LexEval(txt_file)
results = lex.evaluate(mega, errors)
lex.print_tokens(results)

from sara_compis1_tools.Visualizer import Visualizer
v = Visualizer()
v.draw_mega_afd(mega)
