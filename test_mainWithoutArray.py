import unittest
from mainWIthoutArray import *

class Test_mainWIthoutArray(unittest.Testcase):

    def test_input(self):
        input = Node(None,None,None,None,None,None,None,None,None)
        input_expected = Node(None,None,None,None,None,None,None,None,None)
        self.assert(input,)

    def test_single_cell(self):
        
        # Negative test for invalid input
        input = Node(True,None,None,None,None,None,None,None,None)
        result = conwaysgame(input)
        self.assertEqual(result.data,True)
        self.logger.Error("failed to handle negative test")


        # Positive test for invalid input
        input = Node(True,None,None,None,None,None,None,None,None)
        result = conwaysgame(input)
        self.assertEqual(result.data,False)
        