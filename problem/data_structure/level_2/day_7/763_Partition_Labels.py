from typing import List
import unittest


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        ans = []
        for i, c in enumerate(s):
            if dic.get(c):
                dic[c][1] = i
            else:
                dic[c] = [i, i]

        i = 0
        leng = len(s) - 1
        index_partition = s[0]
        while i <= leng:
            if dic[s[i]][0] not in range(dic[index_partition][0],
                                         dic[index_partition][1]+1
                                         ):
                ans.append(dic[index_partition][1]-dic[index_partition][0]+1)
                index_partition = s[i]
            else:
                dic[index_partition][1] = max(
                    dic[index_partition][1], dic[s[i]][1])

            if i == leng:
                ans.append(dic[index_partition][1]-dic[index_partition][0]+1)

            i += 1
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "ababcbacadefegdehijhklij"
        expect = [9, 7, 8]
        self.assertEqual(
            str(self.solution.partitionLabels(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_2(self):
        # test case
        s = "eccbbbbdec"
        expect = [10]
        self.assertEqual(
            str(self.solution.partitionLabels(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_3(self):
        # test case
        s = "caedbdedda"
        expect = [1, 9]
        self.assertEqual(
            str(self.solution.partitionLabels(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )

    def test_run_4(self):
        # test case
        s = "qiejxqfnqceocmy"
        expect = [13, 1, 1]
        self.assertEqual(
            str(self.solution.partitionLabels(s)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
