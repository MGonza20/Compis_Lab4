
from AFD_tools import AFD_tools
from StateAFD import StateAFD
from Error import Error


class LexEval:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r', encoding='utf-8')
        self.lines = self.file.readlines()
        self.file.close()

 
    def evaluate(self, mega, prev_errors=None):
        lines = [line[:-1] for line in self.lines if line[-1] == '\n']
        afd_tools = AFD_tools()
        tokens = []
        errors = prev_errors if prev_errors else set() 
        afd_tools = AFD_tools()
        symbols = afd_tools.get_symbols(mega)

        for line_no, line in enumerate(lines, start=1):
            i = 0
            lenn = len(line)
            while i < lenn:
                if line[i] not in [' ', '\t', '\n']:
                    start = i
                    while i < lenn and line[i] not in [' ', '\t', '\n']:
                        current = line[i]
                        if current not in symbols:
                            errors.add(Error(line_no, f'Caracter no reconocido: {current}', i))

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
                    if lexeme not in [' ', '\t', '\n']:
                        errors.add(Error(line_no, f'Lexema no aceptado: {lexeme}', start))
        return tokens, errors
    

    def print_tokens(self, result_sim):
        tokens, errors = result_sim
        if not errors:
            print('')
            for token in tokens:
                exec(token)
        else:
            print('\n')
            for error in errors:
                if error.position:
                    print(f'Error en línea {error.line}: \n{error.error}, posición {error.position}\n')
                else:   
                    print(f'Error en línea {error.line}: \n{error.error}\n')


if __name__ == '__main__':
    lex_eval = LexEval('sara_compis1_tools/test3')
    # lex_eval = LexEval('test1')
    mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'A': 'B', 'B': 'B', 'C': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'a': 'C', 'b': 'C', 'c': 'C', 'A': 'C', 'B': 'C', 'C': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C'},accepting=False,start=False, value=None),StateAFD(name='C',transitions={'a': 'C', 'b': 'C', 'c': 'C', 'A': 'C', 'B': 'C', 'C': 'C', '0': 'C', '1': 'C', '2': 'C', '3': 'C', 'x': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'y': 'E'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={'z': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'0': 'H', '1': 'H', '2': 'H', '3': 'H'},accepting=True,start=False, value='print("Número entero\\n")'),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'0': 'J', '1': 'J', '2': 'J', '3': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={'0': 'J', '1': 'J', '2': 'J', '3': 'J', '.': 'K'},accepting=False,start=False, value=None),StateAFD(name='K',transitions={'0': 'L', '1': 'L', '2': 'L', '3': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'0': 'L', '1': 'L', '2': 'L', '3': 'L'},accepting=True,start=False, value='print("Número decimal\\n")'),StateAFD(name='init',transitions={'ε': 'M'},accepting=False,start=True, value=None),StateAFD(name='M',transitions={'i': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={'f': 'O'},accepting=False,start=False, value=None),StateAFD(name='O',transitions={},accepting=True,start=False, value='print("Palabra reservada: If\\n")'),StateAFD(name='init',transitions={'ε': 'P'},accepting=False,start=True, value=None),StateAFD(name='P',transitions={'f': 'Q'},accepting=False,start=False, value=None),StateAFD(name='Q',transitions={'o': 'R'},accepting=False,start=False, value=None),StateAFD(name='R',transitions={'r': 'S'},accepting=False,start=False, value=None),StateAFD(name='S',transitions={},accepting=True,start=False, value='print("Palabra reservada: For\\n")'),StateAFD(name='init',transitions={'ε': 'T'},accepting=False,start=True, value=None),StateAFD(name='T',transitions={'"': 'U'},accepting=False,start=False, value=None),StateAFD(name='U',transitions={'a': 'U', 'b': 'U', 'c': 'U', 'A': 'U', 'B': 'U', 'C': 'U', '0': 'U', '1': 'U', '2': 'U', '3': 'U', '"': 'V'},accepting=False,start=False, value=None),StateAFD(name='V',transitions={},accepting=True,start=False, value='print("Cadena\\n")')]
    result_sim = lex_eval.evaluate(mega)
    lex_eval.print_tokens(result_sim)