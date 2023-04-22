
class AFD_tools:
    def __init__(self):
        pass


    get_estado = lambda self, nombre, estados: next(filter(lambda estado: estado.name == nombre, estados), None)


    def cerradura_epsilon(self, estado, estados):
        
        cerradura = {estado}
        if 'ε' in estado.transitions:
            for objetivo in estado.transitions['ε']:
                estado_siguiente = self.get_estado(objetivo, estados)
                cerradura |= self.cerradura_epsilon(estado_siguiente, estados)

        return cerradura
 

    def mover(self, conjunto_estados, simbolo, estados):
        resultado = set()

        for estado in conjunto_estados:
            if simbolo in estado.transitions:
                for objetivo in estado.transitions[simbolo]:
                    estado_siguiente = self.get_estado(objetivo, estados)
                    resultado.add(estado_siguiente)

        return resultado


    def simulacion_afn(self, afn, str_eval):
        estados_actuales = set(filter(lambda s: s.start, afn))
        estados_epsilon = set()

        for estado in estados_actuales:
            estados_epsilon |= self.cerradura_epsilon(estado, afn)

        for simbolo in str_eval:
            estados_siguientes = set()

            for estado in estados_epsilon:
                estados_siguientes |= self.mover({estado}, simbolo, afn)

            estados_epsilon = set()
            for estado in estados_siguientes:
                estados_epsilon |= self.cerradura_epsilon(estado, afn)

        for estado in estados_epsilon:
            if estado.accepting:
                return True

        return False