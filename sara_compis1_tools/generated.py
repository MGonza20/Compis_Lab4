from sara_compis1_tools.StateAFD import StateAFD
from lexEval import LexEval
from Error import Error
import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'd': 'B', 'e': 'B', 'f': 'B', 'g': 'B', 'h': 'B', 'i': 'B', 'j': 'B', 'k': 'B', 'l': 'B', 'm': 'B', 'n': 'B', 'o': 'B', 'p': 'B', 'q': 'B', 'r': 'B', 's': 'B', 't': 'B', 'u': 'B', 'v': 'B', 'w': 'B', 'x': 'B', 'y': 'B', 'z': 'B', 'A': 'B', 'B': 'B', 'C': 'B', 'D': 'B', 'E': 'B', 'F': 'B', 'G': 'B', 'H': 'B', 'I': 'B', 'J': 'B', 'K': 'B', 'L': 'B', 'M': 'B', 'N': 'B', 'O': 'B', 'P': 'B', 'Q': 'B', 'R': 'B', 'S': 'B', 'T': 'B', 'U': 'B', 'V': 'B', 'W': 'B', 'X': 'B', 'Y': 'B', 'Z': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'a': 'C', 'b': 'C', 'c': 'C', 'd': 'C', 'e': 'C', 'f': 'C', 'g': 'C', 'h': 'C', 'i': 'C', 'j': 'C', 'k': 'C', 'l': 'C', 'm': 'C', 'n': 'C', 'o': 'C', 'p': 'C', 'q': 'C', 'r': 'C', 's': 'C', 't': 'C', 'u': 'C', 'v': 'C', 'w': 'C', 'x': 'C', 'y': 'C', 'z': 'C', 'A': 'C', 'B': 'C', 'C': 'C', 'D': 'C', 'E': 'C', 'F': 'C', 'G': 'C', 'H': 'C', 'I': 'C', 'J': 'C', 'K': 'C', 'L': 'C', 'M': 'C', 'N': 'C', 'O': 'C', 'P': 'C', 'Q': 'C', 'R': 'C', 'S': 'C', 'T': 'C', 'U': 'C', 'V': 'C', 'W': 'C', 'X': 'C', 'Y': 'C', 'Z': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', '4': 'C', '5': 'C', '6': 'C', '7': 'C', '8': 'C', '9': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'n': 'C', 'o': 'C', 'p': 'C', 'q': 'C', 'r': 'C', 's': 'C', 't': 'C', 'u': 'C', 'v': 'C', 'w': 'C', 'x': 'D', 'y': 'C', 'z': 'C', 'A': 'C', 'B': 'C', 'C': 'C', 'D': 'C', 'E': 'C', 'F': 'C', 'G': 'C', 'H': 'C', 'I': 'C', 'J': 'C', 'K': 'C', 'L': 'C', 'M': 'C', 'N': 'C', 'O': 'C', 'P': 'C', 'Q': 'C', 'R': 'C', 'S': 'C', 'T': 'C', 'U': 'C', 'V': 'C', 'W': 'C', 'X': 'C', 'Y': 'C', 'Z': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', '4': 'C', '5': 'C', '6': 'C', '7': 'C', '8': 'C', '9': 'C', 'a': 'C', 'b': 'C', 'c': 'C', 'd': 'C', 'e': 'C', 'f': 'C', 'g': 'C', 'h': 'C', 'i': 'C', 'j': 'C', 'k': 'C', 'l': 'C', 'm': 'C'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'n': 'C', 'o': 'C', 'p': 'C', 'q': 'C', 'r': 'C', 's': 'C', 't': 'C', 'u': 'C', 'v': 'C', 'w': 'C', 'x': 'D', 'y': 'E', 'z': 'C', 'A': 'C', 'B': 'C', 'C': 'C', 'D': 'C', 'E': 'C', 'F': 'C', 'G': 'C', 'H': 'C', 'I': 'C', 'J': 'C', 'K': 'C', 'L': 'C', 'M': 'C', 'N': 'C', 'O': 'C', 'P': 'C', 'Q': 'C', 'R': 'C', 'S': 'C', 'T': 'C', 'U': 'C', 'V': 'C', 'W': 'C', 'X': 'C', 'Y': 'C', 'Z': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', '4': 'C', '5': 'C', '6': 'C', '7': 'C', '8': 'C', '9': 'C', 'a': 'C', 'b': 'C', 'c': 'C', 'd': 'C', 'e': 'C', 'f': 'C', 'g': 'C', 'h': 'C', 'i': 'C', 'j': 'C', 'k': 'C', 'l': 'C', 'm': 'C'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={'n': 'C', 'o': 'C', 'p': 'C', 'q': 'C', 'r': 'C', 's': 'C', 't': 'C', 'u': 'C', 'v': 'C', 'w': 'C', 'x': 'D', 'y': 'C', 'z': 'F', 'A': 'C', 'B': 'C', 'C': 'C', 'D': 'C', 'E': 'C', 'F': 'C', 'G': 'C', 'H': 'C', 'I': 'C', 'J': 'C', 'K': 'C', 'L': 'C', 'M': 'C', 'N': 'C', 'O': 'C', 'P': 'C', 'Q': 'C', 'R': 'C', 'S': 'C', 'T': 'C', 'U': 'C', 'V': 'C', 'W': 'C', 'X': 'C', 'Y': 'C', 'Z': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', '4': 'C', '5': 'C', '6': 'C', '7': 'C', '8': 'C', '9': 'C', 'a': 'C', 'b': 'C', 'c': 'C', 'd': 'C', 'e': 'C', 'f': 'C', 'g': 'C', 'h': 'C', 'i': 'C', 'j': 'C', 'k': 'C', 'l': 'C', 'm': 'C'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={'n': 'C', 'o': 'C', 'p': 'C', 'q': 'C', 'r': 'C', 's': 'C', 't': 'C', 'u': 'C', 'v': 'C', 'w': 'C', 'x': 'D', 'y': 'C', 'z': 'C', 'A': 'C', 'B': 'C', 'C': 'C', 'D': 'C', 'E': 'C', 'F': 'C', 'G': 'C', 'H': 'C', 'I': 'C', 'J': 'C', 'K': 'C', 'L': 'C', 'M': 'C', 'N': 'C', 'O': 'C', 'P': 'C', 'Q': 'C', 'R': 'C', 'S': 'C', 'T': 'C', 'U': 'C', 'V': 'C', 'W': 'C', 'X': 'C', 'Y': 'C', 'Z': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', '4': 'C', '5': 'C', '6': 'C', '7': 'C', '8': 'C', '9': 'C', 'a': 'C', 'b': 'C', 'c': 'C', 'd': 'C', 'e': 'C', 'f': 'C', 'g': 'C', 'h': 'C', 'i': 'C', 'j': 'C', 'k': 'C', 'l': 'C', 'm': 'C'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H', '4': 'H', '5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H', '4': 'H', '5': 'H', '6': 'H', '7': 'H', '8': 'H', '9': 'H'},accepting=True,start=False, value='print("Número entero\\n")'),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'0': 'J', '1': 'J', '2': 'J', '3': 'J', '4': 'J', '5': 'J', '6': 'J', '7': 'J', '8': 'J', '9': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={'0': 'J', '1': 'J', '2': 'J', '3': 'J', '4': 'J', '5': 'J', '6': 'J', '7': 'J', '8': 'J', '9': 'J', '.': 'K'},accepting=False,start=False, value=None),StateAFD(name='K',transitions={'0': 'L', '1': 'L', '2': 'L', '3': 'L', '4': 'L', '5': 'L', '6': 'L', '7': 'L', '8': 'L', '9': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'0': 'L', '1': 'L', '2': 'L', '3': 'L', '4': 'L', '5': 'L', '6': 'L', '7': 'L', '8': 'L', '9': 'L'},accepting=True,start=False, value='print("Número decimal\\n")'),StateAFD(name='init',transitions={'ε': 'M'},accepting=False,start=True, value=None),StateAFD(name='M',transitions={'i': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={'f': 'O'},accepting=False,start=False, value=None),StateAFD(name='O',transitions={},accepting=True,start=False, value='print("Palabra reservada: If\\n")'),StateAFD(name='init',transitions={'ε': 'P'},accepting=False,start=True, value=None),StateAFD(name='P',transitions={'f': 'Q'},accepting=False,start=False, value=None),StateAFD(name='Q',transitions={'o': 'R'},accepting=False,start=False, value=None),StateAFD(name='R',transitions={'r': 'S'},accepting=False,start=False, value=None),StateAFD(name='S',transitions={},accepting=True,start=False, value='print("Palabra reservada: For\\n")'),StateAFD(name='init',transitions={'ε': 'T'},accepting=False,start=True, value=None),StateAFD(name='T',transitions={'"': 'U'},accepting=False,start=False, value=None),StateAFD(name='U',transitions={'a': 'U', 'b': 'U', 'c': 'U', 'd': 'U', 'e': 'U', 'f': 'U', 'g': 'U', 'h': 'U', 'i': 'U', 'j': 'U', 'k': 'U', 'l': 'U', 'm': 'U', 'n': 'U', 'o': 'U', 'p': 'U', 'q': 'U', 'r': 'U', 's': 'U', 't': 'U', 'u': 'U', 'v': 'U', 'w': 'U', 'x': 'U', 'y': 'U', 'z': 'U', 'A': 'U', 'B': 'U', 'C': 'U', 'D': 'U', 'E': 'U', 'F': 'U', 'G': 'U', 'H': 'U', 'I': 'U', 'J': 'U', 'K': 'U', 'L': 'U', 'M': 'U', 'N': 'U', 'O': 'U', 'P': 'U', 'Q': 'U', 'R': 'U', 'S': 'U', 'T': 'U', 'U': 'U', 'V': 'U', 'W': 'U', 'X': 'U', 'Y': 'U', 'Z': 'U', '0': 'U', '1': 'U', '2': 'U', '3': 'U', '4': 'U', '5': 'U', '6': 'U', '7': 'U', '8': 'U', '9': 'U', ' ': 'U', '"': 'V'},accepting=False,start=False, value=None),StateAFD(name='V',transitions={},accepting=True,start=False, value='print("Cadena\\n")')]
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
