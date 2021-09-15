class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        return False

class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None

        newslow = head
        while slow != newslow:
            slow = slow.next
            newslow = newslow.next
        return slow