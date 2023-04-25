from sara_compis1_tools.StateAFD import StateAFD
from sara_compis1_tools.lexEval import LexEval
from sara_compis1_tools.Error import Error
import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'f': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'o': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'r': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={},accepting=True,start=False, value='print("Palabra reservada: For\\n")'),StateAFD(name='init',transitions={'ε': 'E'},accepting=False,start=True, value=None),StateAFD(name='E',transitions={'w': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={'h': 'G'},accepting=False,start=False, value=None),StateAFD(name='G',transitions={'i': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'l': 'I'},accepting=False,start=False, value=None),StateAFD(name='I',transitions={'e': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value='print("Palabra reservada: While\\n")'),StateAFD(name='init',transitions={'ε': 'K'},accepting=False,start=True, value=None),StateAFD(name='K',transitions={'a': 'L', 'b': 'L', 'c': 'L', 'd': 'L', 'e': 'L', 'f': 'L', 'g': 'L', 'h': 'L', 'i': 'L', 'j': 'L', 'k': 'L', 'l': 'L', 'm': 'L', 'n': 'L', 'o': 'L', 'p': 'L', 'q': 'L', 'r': 'L', 's': 'L', 't': 'L', 'u': 'L', 'v': 'L', 'w': 'L', 'x': 'L', 'y': 'L', 'z': 'L', 'A': 'L', 'B': 'L', 'C': 'L', 'D': 'L', 'E': 'L', 'F': 'L', 'G': 'L', 'H': 'L', 'I': 'L', 'J': 'L', 'K': 'L', 'L': 'L', 'M': 'L', 'N': 'L', 'O': 'L', 'P': 'L', 'Q': 'L', 'R': 'L', 'S': 'L', 'T': 'L', 'U': 'L', 'V': 'L', 'W': 'L', 'X': 'L', 'Y': 'L', 'Z': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'a': 'L', 'b': 'L', 'c': 'L', 'd': 'L', 'e': 'L', 'f': 'L', 'g': 'L', 'h': 'L', 'i': 'L', 'j': 'L', 'k': 'L', 'l': 'L', 'm': 'L', 'n': 'L', 'o': 'L', 'p': 'L', 'q': 'L', 'r': 'L', 's': 'L', 't': 'L', 'u': 'L', 'v': 'L', 'w': 'L', 'x': 'L', 'y': 'L', 'z': 'L', 'A': 'L', 'B': 'L', 'C': 'L', 'D': 'L', 'E': 'L', 'F': 'L', 'G': 'L', 'H': 'L', 'I': 'L', 'J': 'L', 'K': 'L', 'L': 'L', 'M': 'L', 'N': 'L', 'O': 'L', 'P': 'L', 'Q': 'L', 'R': 'L', 'S': 'L', 'T': 'L', 'U': 'L', 'V': 'L', 'W': 'L', 'X': 'L', 'Y': 'L', 'Z': 'L', '0': 'L', '1': 'L', '2': 'L', '3': 'L', '4': 'L', '5': 'L', '6': 'L', '7': 'L', '8': 'L', '9': 'L'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'M'},accepting=False,start=True, value=None),StateAFD(name='M',transitions={'0': 'N', '1': 'N', '2': 'N', '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', '9': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={'0': 'N', '1': 'N', '2': 'N', '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', '9': 'N'},accepting=True,start=False, value='print("Numero entero\\n")'),StateAFD(name='init',transitions={'ε': 'O'},accepting=False,start=True, value=None),StateAFD(name='O',transitions={'+': 'P', '-': 'P', '*': 'P', '/': 'P'},accepting=False,start=False, value=None),StateAFD(name='P',transitions={},accepting=True,start=False, value='print("Operador aritmetico\\n")')]
errors = set([Error(line=16, error='Error: Token no definido: palabra_reservada_if en archivo .yal')])

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
