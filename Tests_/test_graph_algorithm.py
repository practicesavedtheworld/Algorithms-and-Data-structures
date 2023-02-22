import unittest
import os
import sys

sys.path.append(os.path.join(sys.path[0], '..'))
from dijkstra import dijkstra
from Exceptions_.exceptions_graph import *
from graph_reader import graph_reader, weighted_graph_reader


class TestGraphReader(unittest.TestCase):
    def test_exceptions(self):
        """
        Not the deepest test-cases. Just for realizing everything is works.
        """
        self.assertRaises(ExcludedStart,
                          weighted_graph_reader,
                          'a', 'b', 'c', 'fin', start_a=10, a_b=20, b_c=1, c_a=1, b_fin=30)

        self.assertRaises(ExcludedFinish,
                          weighted_graph_reader,
                          'start', 'a', 'b', 'c', start_a=10, a_b=20, b_c=1, c_a=1)

        self.assertRaises((ExcludedStart, ExcludedFinish),
                          weighted_graph_reader,
                          'a', 'b', 'c', a_b=20, bc=1, c_a=1)

        self.assertRaises(NegativeWeightInGraph,
                          weighted_graph_reader,
                          'start', 'a', 'b', 'c', 'fin', start_a=10, a_b=20, b_c=-1., c_a=1, b_fin=-30)

        self.assertRaises(MissingNodeSeparator,
                          weighted_graph_reader,
                          'start', 'a', 'b', 'c', 'fin', start_a=10, a_b=20, bc=1, c_a=1)

        self.assertRaises((WrongNeighborsType, IncorrectStartingNodeName),
                          graph_reader,
                          beginning=['B'], B=('K', 'F', 'C', 'D'))

        self.assertRaises(WrongInnerType,
                          graph_reader,
                          start=['A'], A=['B', ('C', 'D')])


class TestDijkstra(unittest.TestCase):
    def test_correctness(self):
        error_message = "Wrong path. Algorithm does not work properly"
        self.assertEqual(dijkstra(weighted_graph_reader(
            'start', 'a', 'b', 'c', 'fin', start_a=10, a_b=20, b_c=1, c_a=1, b_fin=30)),
            'start ---> a ---> b ---> fin',
            error_message)

        self.assertEqual(dijkstra(weighted_graph_reader(
            'start', 'b', 'k', 'f', 'c', 'd', 'e', 'fin',
            start_b=15, b_k=3, b_f=4, b_c=6, b_d=7, d_e=8, d_start=4, e_fin=1, f_fin=3)),
            'start ---> b ---> f ---> fin',
            error_message)

        self.assertEqual(dijkstra(weighted_graph_reader(
            'start', 'O', 'K', 'T', 'Z', 'A', 'C', 'F', 'L', 'D', 'Y', 'E', 'M', 'X', 'P', 'G', 'fin',
            start_O=3, start_A=44, start_Z=24, O_A=3, O_C=2, O_K=14, Z_X=10, K_F=19, K_T=19, A_D=1, A_L=30,
            C_D=7, F_Y=17, T_fin=46, D_F=8, D_E=2, L_M=3, E_Y=23, E_G=4, Y_fin=13, X_P=25, M_P=1, P_G=4, P_fin=11)),
            'start ---> O ---> A ---> D ---> E ---> Y ---> fin',
            error_message)

        self.assertEqual(dijkstra(weighted_graph_reader(
            'start', 'fin', 'A', 'B', 'C', start_fin=100, start_A=1, start_C=50, C_fin=10, C_A=15, A_B=15, B_C=11)),
            'start ---> A ---> B ---> C ---> fin',
            error_message)


if __name__ == '__main__':
    unittest.main()
