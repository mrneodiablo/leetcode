import unittest


class MyQueue:

    def __init__(self):
        self.myqueue = []

    def push(self, x: int) -> None:
        self.myqueue.insert(0, x)

    def pop(self) -> int:
        return self.myqueue.pop()

    def peek(self) -> int:
        return self.myqueue[-1]

    def empty(self) -> bool:
        if len(self.myqueue) == 0:
            return True
        return False


class TestFunctions(unittest.TestCase):

    def test_run_1(self):
        # test case
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.peek()
        expect = 1

        expect = True
        self.assertEqual(queue.peek(),
                         expect,
                         "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
