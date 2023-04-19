from sara_compis1_tools.StateAFD import StateAFD
from sara_compis1_tools.Visualizer import Visualizer

mega = [StateAFD(name='init',transitions={'949': 'A'},accepting=False,start=True),StateAFD(name='A',transitions={'032': 'B', '009': 'B', '010': 'B'},accepting=False,start=False),StateAFD(name='B',transitions={},accepting=True,start=False),StateAFD(name='init',transitions={'949': 'C'},accepting=False,start=True),StateAFD(name='C',transitions={'032': 'D', '009': 'D', '010': 'D'},accepting=False,start=False),StateAFD(name='D',transitions={'032': 'D', '009': 'D', '010': 'D'},accepting=True,start=False),StateAFD(name='init',transitions={'949': 'E'},accepting=False,start=True),StateAFD(name='E',transitions={'048': 'F', '049': 'F', '050': 'F', '051': 'F'},accepting=False,start=False),StateAFD(name='F',transitions={},accepting=True,start=False),StateAFD(name='init',transitions={'949': 'G'},accepting=False,start=True),StateAFD(name='G',transitions={'045': 'H', '048': 'I', '049': 'I', '050': 'I', '051': 'I'},accepting=False,start=False),StateAFD(name='H',transitions={'048': 'I', '049': 'I', '050': 'I', '051': 'I'},accepting=False,start=False),StateAFD(name='I',transitions={'048': 'I', '049': 'I', '050': 'I', '051': 'I'},accepting=True,start=False),StateAFD(name='init',transitions={'949': 'J'},accepting=False,start=True),StateAFD(name='J',transitions={'097': 'K', '098': 'K', '099': 'K', '065': 'K', '066': 'K', '067': 'K'},accepting=False,start=False),StateAFD(name='K',transitions={},accepting=True,start=False),StateAFD(name='init',transitions={'949': 'L'},accepting=False,start=True),StateAFD(name='L',transitions={'097': 'M', '098': 'M', '099': 'M', '065': 'M', '066': 'M', '067': 'M'},accepting=False,start=False),StateAFD(name='M',transitions={'097': 'M', '098': 'M', '099': 'M', '065': 'M', '066': 'M', '067': 'M', '048': 'M', '049': 'M', '050': 'M', '051': 'M'},accepting=True,start=False)]

visual = Visualizer()
visual.draw_mega_afd(mega)