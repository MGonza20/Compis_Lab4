
class AFD_tools:
    def __init__(self):
        pass


    get_state = lambda self, name, states: next(filter(lambda state: state.name == name, states), None)


    def epsilon_clousure(self, state, states):
        
        clousure = {state}
        if 'ε' in state.transitions:
            for target in state.transitions['ε']:
                next_state = self.get_state(target, states)
                clousure |= self.epsilon_clousure(next_state, states)

        return clousure
 

    def move(self, states_set, sym, states):
        res = set()

        for state in states_set:
            if sym in state.transitions:
                for target in state.transitions[sym]:
                    next_state = self.get_state(target, states)
                    res.add(next_state)

        return res


    def afn_simulation(self, afn, str_eval):
        current_states = set(filter(lambda s: s.start, afn))
        epsilon_states = set()

        for state in current_states:
            epsilon_states |= self.epsilon_clousure(state, afn)

        for sym in str_eval:
            next_states = set()

            for state in epsilon_states:
                next_states |= self.move({state}, sym, afn)

            epsilon_states = set()
            for state in next_states:
                epsilon_states |= self.epsilon_clousure(state, afn)

        for state in epsilon_states:
            if state.accepting:
                return True

        return False