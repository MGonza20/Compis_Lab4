from sara_compis1_tools.StateAFD import StateAFD
from sara_compis1_tools.Visualizer import Visualizer

mega = [StateAFD(name='init',transitions={'949': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={'032': 'B', '009': 'B', '010': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={'032': 'B', '009': 'B', '010': 'B'},accepting=True,start=False, value=''),StateAFD(name='init',transitions={'949': 'C'},accepting=False,start=True, value=None),StateAFD(name='C',transitions={'097': 'D', '098': 'D', '099': 'D', '065': 'D', '066': 'D', '067': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'097': 'D', '098': 'D', '099': 'D', '065': 'D', '066': 'D', '067': 'D', '048': 'D', '049': 'D', '050': 'D', '051': 'D'},accepting=True,start=False, value="print('Identificador\n')")StateAFD(name='init',transitions={'949': 'E'},accepting=False,start=True, value=None),StateAFD(name='E',transitions={'043': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={},accepting=True,start=False, value="print('Operador de suma\n')"),StateAFD(name='init',transitions={'949': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'042': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={},accepting=True,start=False, value="print('Operador de multiplicación\n')"),StateAFD(name='init',transitions={'949': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={'061': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value="print('Operador de asignación\n')"),]

visual = Visualizer()
visual.draw_mega_afd(mega)