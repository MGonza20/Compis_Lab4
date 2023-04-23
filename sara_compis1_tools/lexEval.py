
from AFD_tools import AFD_tools
from StateAFD import StateAFD

class LexEval:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.lines = self.file.readlines()
        self.file.close()

        self.tokens = []
        self.lexemes = []

    def evaluate(self, mega):
        lines = self.lines
        lines = [line[:-1] for line in lines if line[-1] == '\n']
        afd_tools = AFD_tools()
        tokens = []
        errors = {}

        for line_no, line in enumerate(lines, start=1):
            i = 0
            lenn = len(line)
            while i < lenn:
                if line[i] not in [' ', '\t', '\n']:
                    start = i
                    while i < lenn and line[i] not in [' ', '\t', '\n']:
                        i += 1
                    lexeme = line[start:i]
                else:
                    lexeme = line[i]
                    i += 1

                accepted = afd_tools.afn_simulation(mega, lexeme)
                if accepted:
                    if accepted != 'empty_value':
                        tokens.append(accepted)
                else:
                    if line_no not in errors: errors[line_no] = []
                    errors[line_no].append(lexeme)

        return tokens, errors


if __name__ == '__main__':
    lex_eval = LexEval('sara_compis1_tools/test')
    mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={' ': 'B', '\t': 'B', '\n': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={' ': 'B', '\t': 'B', '\n': 'B'},accepting=True,start=False, value=''),StateAFD(name='init',transitions={'ε': 'C'},accepting=False,start=True, value=None),StateAFD(name='C',transitions={'a': 'D', 'b': 'D', 'c': 'D', 'd': 'D', 'e': 'D', 'f': 'D', 'g': 'D', 'h': 'D', 'i': 'D', 'j': 'D', 'k': 'D', 'l': 'D', 'm': 'D', 'n': 'D', 'o': 'D', 'p': 'D', 'q': 'D', 'r': 'D', 's': 'D', 't': 'D', 'u': 'D', 'v': 'D', 'w': 'D', 'x': 'D', 'y': 'D', 'z': 'D', 'A': 'D', 'B': 'D', 'C': 'D', 'D': 'D', 'E': 'D', 'F': 'D', 'G': 'D', 'H': 'D', 'I': 'D', 'J': 'D', 'K': 'D', 'L': 'D', 'M': 'D', 'N': 'D', 'O': 'D', 'P': 'D', 'Q': 'D', 'R': 'D', 'S': 'D', 'T': 'D', 'U': 'D', 'V': 'D', 'W': 'D', 'X': 'D', 'Y': 'D', 'Z': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'a': 'D', 'b': 'D', 'c': 'D', 'd': 'D', 'e': 'D', 'f': 'D', 'g': 'D', 'h': 'D', 'i': 'D', 'j': 'D', 'k': 'D', 'l': 'D', 'm': 'D', 'n': 'D', 'o': 'D', 'p': 'D', 'q': 'D', 'r': 'D', 's': 'D', 't': 'D', 'u': 'D', 'v': 'D', 'w': 'D', 'x': 'D', 'y': 'D', 'z': 'D', 'A': 'D', 'B': 'D', 'C': 'D', 'D': 'D', 'E': 'D', 'F': 'D', 'G': 'D', 'H': 'D', 'I': 'D', 'J': 'D', 'K': 'D', 'L': 'D', 'M': 'D', 'N': 'D', 'O': 'D', 'P': 'D', 'Q': 'D', 'R': 'D', 'S': 'D', 'T': 'D', 'U': 'D', 'V': 'D', 'W': 'D', 'X': 'D', 'Y': 'D', 'Z': 'D', '0': 'D', '1': 'D', '2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D'},accepting=True,start=False, value="print('Identificador\n')"),StateAFD(name='init',transitions={'ε': 'E'},accepting=False,start=True, value=None),StateAFD(name='E',transitions={'+': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={},accepting=True,start=False, value="print('Operador de suma\n')"),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'*': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={},accepting=True,start=False, value="print('Operador de multiplicaciÃ³n\n')"),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'=': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value="print('Operador de asignaciÃ³n\n')")]
    results = lex_eval.evaluate(mega)
    aa = 123

    # afd_tools = AFD_tools()
    # print(afd_tools.afn_simulation(mega, '\t'))

