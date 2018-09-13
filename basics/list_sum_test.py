import unittest
import list_sum

exList = [1,2,3,2,3,4,6,7,8,9,10,5]

class SumTest(unittest.TestCase):
    def test_sum_funcs(self):
        self.assertEqual(list_sum.for_loop_sum(exList), 60)
        self.assertEqual(list_sum.while_loop_sum(exList), 60)
        self.assertEqual(list_sum.recursive_sum(exList, 0), 60)

if __name__ == "__main__":
    unittest.main()
