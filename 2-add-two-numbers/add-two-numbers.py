class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        result_current = dummy

        current = l1
        current_l2 = l2
        carry = 0

        while current is not None or current_l2 is not None or carry != 0:

            val1 = current.val if current is not None else 0
            val2 = current_l2.val if current_l2 is not None else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            result_current.next = ListNode(digit)
            result_current = result_current.next

            if current is not None:
                current = current.next

            if current_l2 is not None:
                current_l2 = current_l2.next

        return dummy.next