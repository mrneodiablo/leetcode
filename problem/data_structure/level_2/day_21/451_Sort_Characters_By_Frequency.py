from collections import Counter
import unittest


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        count = Counter(s)
        frequencies = sorted(
            [[k, sequent] for k, sequent in count.items()],
            key=lambda x: x[1],
            reverse=True
        )

        for frequency in frequencies:
            ans += frequency[0]*frequency[1]

        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        s = "tree"
        expect = "eetr"
        self.assertEqual(
            str(self.solution.frequencySort(s)),
            str(expect),
            "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        s = "cccaaa"
        expect = "cccaaa"
        self.assertEqual(
            str(self.solution.frequencySort(s)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
