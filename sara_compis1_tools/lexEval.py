
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


# if __name__ == '__main__':
#     lex_eval = LexEval('sara_compis1_tools/test2')
#     # lex_eval = LexEval('test1')
#     mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'A': 'B', 'B': 'B', 'C': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'a': 'B', 'b': 'B', 'c': 'B', 'A': 'B', 'B': 'B', 'C': 'B', '0': 'B', '1': 'B', '2': 'B', '3': 'B', '4': 'B', '5': 'B', '6': 'B', '7': 'B', '8': 'B', '9': 'B'},accepting=True,start=False, value='print("Identificador\\n")'),StateAFD(name='init',transitions={'ε': 'C'},accepting=False,start=True, value=None),StateAFD(name='C',transitions={'i': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'f': 'E'},accepting=False,start=False, value=None),StateAFD(name='E',transitions={},accepting=True,start=False, value='print("If\\n")'),StateAFD(name='init',transitions={'ε': 'F'},accepting=False,start=True, value=None),StateAFD(name='F',transitions={'f': 'G'},accepting=False,start=False, value=None),StateAFD(name='G',transitions={'o': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={'r': 'I'},accepting=False,start=False, value=None),StateAFD(name='I',transitions={},accepting=True,start=False, value='print("For\\n")'),StateAFD(name='init',transitions={'ε': 'J'},accepting=False,start=True, value=None),StateAFD(name='J',transitions={'w': 'K'},accepting=False,start=False, value=None),StateAFD(name='K',transitions={'h': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={'i': 'M'},accepting=False,start=False, value=None),StateAFD(name='M',transitions={'l': 'N'},accepting=False,start=False, value=None),StateAFD(name='N',transitions={'e': 'O'},accepting=False,start=False, value=None),StateAFD(name='O',transitions={},accepting=True,start=False, value='print("While\\n")'),StateAFD(name='init',transitions={'ε': 'P'},accepting=False,start=True, value=None),StateAFD(name='P',transitions={'0': 'Q', '1': 'Q', '2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q'},accepting=False,start=False, value=None),StateAFD(name='Q',transitions={'0': 'Q', '1': 'Q', '2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q'},accepting=True,start=False, value='print("Entero\\n")'),StateAFD(name='init',transitions={'ε': 'R'},accepting=False,start=True, value=None),StateAFD(name='R',transitions={'+': 'S', '-': 'S', '*': 'S', '/': 'S'},accepting=False,start=False, value=None),StateAFD(name='S',transitions={},accepting=True,start=False, value='print("Operador aritmetico\\n")')]
#     result_sim = lex_eval.evaluate(mega)
#     lex_eval.print_tokens(result_sim)