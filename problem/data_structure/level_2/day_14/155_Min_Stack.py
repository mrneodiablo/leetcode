import unittest


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


class TestFunctions(unittest.TestCase):

    def test_run_1(self):
        # test case

        obj = MinStack()
        obj.push(1)
        obj.push(2)
        obj.pop()
        self.assertEqual(obj.getMin(), 1,
                         "incorrect, expect is " + str(1)
                         )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
