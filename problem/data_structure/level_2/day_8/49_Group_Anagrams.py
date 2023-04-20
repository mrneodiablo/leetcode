from typing import List
import unittest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        for st in strs:
            hash_key = "".join(sorted(list(st)))
            if dic.get(hash_key):
                dic[hash_key].append(st)
            else:
                dic[hash_key] = [st]

        for v in dic.values():
            ans.append(v)

        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expect = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(
            str(self.solution.groupAnagrams(strs)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        strs = [""]
        expect = [[""]]
        self.assertEqual(
            str(self.solution.groupAnagrams(strs)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
