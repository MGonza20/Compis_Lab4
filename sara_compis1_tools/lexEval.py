
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

