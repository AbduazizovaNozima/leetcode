class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        result1 = []
        result2 = []

        while l1:
            result1.append(l1.val)
            l1 = l1.next
        while l2:
            result2.append(l2.val)
            l2 = l2.next

        num1 = int(''.join(map(str, result1[::-1])))
        num2 = int(''.join(map(str, result2[::-1])))
        total = num1 + num2

        result_digits = list(str(total))[::-1]

        dummy = ListNode()
        tail = dummy
        for digit in result_digits:
            tail.next = ListNode(int(digit))
            tail = tail.next

        return dummy.next
