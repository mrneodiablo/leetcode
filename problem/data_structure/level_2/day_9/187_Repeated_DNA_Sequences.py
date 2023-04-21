from typing import List
import unittest


class Solution:
    def findRepeatedDnaSequences(self, c: str) -> List[str]:
        dic = {}
        for i in range(0, len(c)-9):
            dic[c[i:i+10]] = dic.get(c[i:i+10], 0) + 1

        return [substring for substring, value in dic.items() if value > 1]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expect = ["AAAAACCCCC", "CCCCCAAAAA"]
        self.assertEqual(
            str(self.solution.findRepeatedDnaSequences(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        s = "AAAAAAAAAAA"
        expect = ["AAAAAAAAAA"]
        self.assertEqual(
            str(self.solution.findRepeatedDnaSequences(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
