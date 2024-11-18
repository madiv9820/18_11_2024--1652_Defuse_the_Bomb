from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([5,7,1,4], 3, [12,10,16,13]), 2: ([1,2,3,4], 0, [0,0,0,0]), 3: ([2,4,9,3], 2, [12,5,6,13])}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        code, k, output = self.__testCases[1]
        result = self.__obj.decrypt(code = code, k = k)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_2(self):
        code, k, output = self.__testCases[2]
        result = self.__obj.decrypt(code = code, k = k)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_3(self):
        code, k, output = self.__testCases[3]
        result = self.__obj.decrypt(code = code, k = k)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

if __name__ == '__main__':
    unittest.main()