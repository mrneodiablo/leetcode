import unittest


class MyHashMap:

    def __init__(self):
        self.__hash = {}

    def put(self, key: int, value: int) -> None:
        self.__hash[key] = value

    def get(self, key: int) -> int:
        return self.__hash.get(key) if self.__hash.get(key) is not None else -1

    def remove(self, key: int) -> None:
        if self.__hash.get(key):
            self.__hash.pop(key)


class TestFunctions(unittest.TestCase):

    def test_run_1(self):
        a = MyHashMap()
        a.remove(2)
        a.put(3, 11)
        a.put(4, 13)
        a.put(15, 6)
        a.put(6, 15)
        a.put(11, 0)
        a.get(11)

        expect = 0
        self.assertEqual(
            str(a.get(11)),
            str(expect),
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
