

from Bridge import Bridge
from Format import Format
from StateAFD import StateAFD
from Syntax import Syntax
import pydot
import networkx as nx
from graphviz import Digraph
from networkx.drawing.nx_agraph import to_agraph




import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'    

class AFN:
    def __init__(self, regex):
        self.regex = regex
        self.statesNo = 0
        self.afn = None
        self.afd = None

    def get_transitions(self, afn):
        
        transitions = {}
        for state_obj in afn:
            if state_obj.name not in transitions:
                transitions[state_obj.name] = {}

            for k, v in state_obj.transitions.items():
                key = chr(int(k))

                if key not in transitions[state_obj.name]:
                    transitions[state_obj.name][key] = []

                if v not in transitions[state_obj.name][key]:
                    transitions[state_obj.name][key].append(v)    
        return transitions
    


    def cerradura_kleene(self, state,  afn, checked=None):
        if not checked:
            checked = set()

        transitions = self.get_transitions(afn)
        checked.add(state)

        for next_ep in transitions.get(state, {}).get('ε', []):
            if next_ep not in checked:
                checked.update(self.cerradura_kleene(state=next_ep, afn=afn, checked=checked))
        return list(checked)
    

    def mover(self, state, symbol, afn):
        transitions = self.get_transitions(afn)
        return transitions.get(state, {}).get(symbol, [])

    def many_move(self, states, symbol, afn):
        move = [self.mover(state, symbol, afn) for state in states]
        return list(set(sum(move, [])))

    def many_kleene(self, states, afn):
        kleene = [self.cerradura_kleene(state=state, afn=afn) for state in states]
        return list(set(sum(kleene, [])))

    def to_afd(self, afn):
        counter = 0
        afd = {}
        start = [state.name for state in afn if state.start][0]
        symbols = list(set([chr(int(symbol)) for state in afn for symbol in state.transitions.keys() if symbol != '949']))
        to_do = [self.cerradura_kleene(start, afn=afn)]
        checked = []

        while to_do:
            name = to_do.pop(0)
            if name not in checked:
                afd_t = {}
                for symbol in symbols:
                    afd_t[symbol] = self.many_kleene(self.many_move(name, symbol, afn), afn)
                    
                # afd_t = {symbol: self.many_kleene(self.many_move(name, symbol, afn), afn) for symbol in symbols}
                for state in afd_t.values():
                    if len(state) > 0:
                        to_do.append(state)
                checked.append(name)
                afd[counter] = StateAFD(name, afd_t, True) if counter == 0 else StateAFD(name, afd_t)
                counter += 1

        for i in range(len(afd)):
            if afd[i].name in [state.name for state in afn if state.accepting]:
                afd[i].accepting = True
        return afd



    def createNewStates(self):
        sts = []
        afd = self.afd
        for i in range(len(afd)):
            if afd[i].name not in sts:
                sts.append(afd[i].name)
        letters = {}
        for i in range(len(sts)):
            letters[chr(65+i)] = sts[i]
        return letters
    

    def assignStates(self):
        afd = self.afd
        letters = self.createNewStates()
        for i in range(len(afd)):
            for k, v in letters.items():
                if afd[i].name == v:
                    afd[i].name = k
            for k, v in afd[i].transitions.items():
                for k2, v2 in letters.items():
                    if v == v2:
                        afd[i].transitions[k] = k2
                    elif not v:
                        afd[i].transitions[k] = 'estado muerto'
        return afd
    

    def simulateAFD(self, string):
        afd = self.assignStates()
        current_state = afd[0]
        for symbol in string:
            if symbol not in current_state.transitions:
                return False
            current_state = [state for key, state in afd.items() if state.name == current_state.transitions[symbol]]
            if not current_state:
                return False
            else:
                current_state = current_state[0]
        return current_state.accepting


    def draw_afd(self):
        afd = self.assignStates()

        G = nx.MultiDiGraph()

        for state in afd.values():
            for k, v in state.transitions.items():
                if state.start:
                    G.add_node(state.name, color='green', style='filled', shape='circle')                                               
                if state.accepting:
                    G.add_node(state.name, shape='doublecircle')
                else:
                    if v != 'estado muerto':
                        G.add_node(v)
                if v != 'estado muerto':
                    G.add_edge(state.name, v, label=k, dir='forward')

        dot = Digraph()
        for u, v, data in G.edges(data=True):
            dot.edge(u, v, label=data['label'], dir=data['dir'])
        for node in G.nodes:
            attrs = G.nodes[node]
            dot.node(node, **attrs)

        dot.attr(rankdir='LR')
        dot.render('afn/AfnToAfd', format='png')



    def minimizationAFD(self):
        # Creando copia del AFD
        afd = self.assignStates().copy()

        # Unir estados de aceptacion y que no son de aceptacion
        accepting_states = set(state for key, state in afd.items() if state.accepting)
        non_accepting_states = set(state for key, state in afd.items() if not state.accepting)
        state_groups = [accepting_states, non_accepting_states]

        # Repetir hasta que no se puedan unir mas estados
        while True:
            new_state_groups = []
            for group in state_groups:
                # Por cada grupo de estados, agrupar por transiciones
                transition_groups = {}
                for state in group:
                    transition = tuple(sorted(state.transitions.values()))
                    if transition not in transition_groups:
                        transition_groups[transition] = set()
                    transition_groups[transition].add(state)

                # Por cada grupo de transiciones, unir estados
                for transition_group in transition_groups.values():
                    if len(transition_group) > 1:
                        new_state_groups.append(transition_group)
                    else:
                        new_state_groups.append({transition_group.pop()})

            # Si ya no se pueden unir mas estados, terminar
            if len(new_state_groups) == len(state_groups):
                break
            state_groups = new_state_groups

        # Crear nuevo AFD
        statesI = sum(len(group) for group in state_groups)
        reps = {}
        for group in state_groups:
            if len(group) > 1:
                same = []
                for element in group:
                    same.append(element)
                reps[chr(65+statesI)] = tuple(same)
                statesI += 1


        for replacement, same in reps.items():
            check = tuple([obj.name for obj in same])
            checkAccepting = tuple([obj.accepting for obj in same])
            checkStart = tuple([obj.start for obj in same])
            for key, state in afd.items():
                for k, v in state.transitions.items():
                    if v in check:
                        state.transitions[k] = replacement
                if  checkAccepting.count(True) > 0:
                    if state.name in check:
                        state.accepting = True
                if checkStart.count(True) > 0:
                    if state.name in check:
                        state.start = True
                if state.name in check:
                    state.name = replacement

        miniAFD = {}
        index = 0
        for key, state in afd.items():
            if state.name not in [obj.name for obj in miniAFD.values()]:
                miniAFD[index] = state
                index += 1

        return miniAFD
    

    def simulateMiniAFD(self, string):
        afd = self.minimizationAFD()
        current_state = afd[0]
        for symbol in string:
            if symbol not in current_state.transitions:
                return False
            current_state = [state for key, state in afd.items() if state.name == current_state.transitions[symbol]]
            if not current_state:
                return False
            else:
                current_state = current_state[0]
        return current_state.accepting
    

    def draw_mini_afd(self):
        afd = self.minimizationAFD()

        G = nx.MultiGraph()

        # add nodes and edges to G
        for state in afd.values():
            for k, v in state.transitions.items():
                if state.start:
                    G.add_node(state.name, color='green', style='filled', shape='circle')
                if state.accepting:
                    G.add_node(state.name, shape='doublecircle')
                else:
                    if v != 'estado muerto':
                        G.add_node(v)
                if v != 'estado muerto':
                    G.add_edge(state.name, v, label=k, dir='forward')
                   
        dot = Digraph()
        for u, v, data in G.edges(data=True):
            dot.edge(u, v, label=data['label'], dir=data['dir'])
        for node in G.nodes:
            attrs = G.nodes[node]
            dot.node(node, **attrs)

        dot.attr(rankdir='LR')
        dot.render('afn/miniAFD', format='png')

            
    def AFsimulations(self, string):
        self.MYT()
        print("Simulación AFN: " + f"cadena aceptada" if self.simulateAFN(string) else "Simulación AFN: " + "cadena rechazada")
        self.toAFD()
        print("Simulación AFD: " + f"cadena aceptada" if self.simulateAFD(string) else "Simulación AFD: " + "cadena rechazada")
        print("Simulación AFD Minimizado: " + f"cadena aceptada" if self.simulateMiniAFD(string) else "Simulación AFD Minimizado: " +"cadena rechazada")

        


