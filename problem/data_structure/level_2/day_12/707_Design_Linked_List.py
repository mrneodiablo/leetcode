
import unittest


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.lenn = 0

    def get(self, index: int) -> int:
        if index >= self.lenn or index < 0:
            return -1

        cur = self.head
        i = 0
        while i <= index:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        cur = self.head
        self.head = Node(val, cur)
        self.lenn += 1

    def addAtTail(self, val: int) -> None:

        if self.head:
            cur = self.head
            while cur:
                if cur.next:
                    cur = cur.next
                else:
                    cur.next = Node(val, None)
                    break
        else:
            self.head = Node(val)

        self.lenn += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.lenn:
            return

        if index == 0:
            self.addAtHead(val)

        elif index == self.lenn:
            self.addAtTail(val)

        else:
            cur = self.head
            i = 0
            while cur:
                if i == (index-1):
                    new = Node(val)
                    new.next = cur.next
                    cur.next = new
                    break
                i += 1
                cur = cur.next
            self.lenn += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.lenn:
            return

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            i = index - 1
            while i:
                cur = cur.next
                i -= 1

            cur.next = cur.next.next

        self.lenn -= 1
        if self.lenn == 0:
            self.head = None


class TestFunctions(unittest.TestCase):

    def test_run_1(self):
        # test case

        obj = MyLinkedList()
        obj.addAtHead(1)
        obj.addAtTail(3)
        obj.addAtIndex(1, 2)
        obj.get(1)
        obj.deleteAtIndex(1)
        self.assertEqual(obj.get(1), 3,
                         "incorrect, expect is " + str(1)
                         )

    def test_run_2(self):
        # test case

        obj = MyLinkedList()
        obj.addAtTail(1)
        self.assertEqual(obj.get(0), 1,
                         "incorrect, expect is " + str(1)
                         )

    def test_run_3(self):
        # test case

        obj = MyLinkedList()
        obj.addAtIndex(1, 0)
        self.assertEqual(obj.get(0), -1,
                         "incorrect, expect is " + str(1)
                         )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
