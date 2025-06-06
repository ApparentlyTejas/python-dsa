class Solution:
    def insertGreatestCommonDivisor(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcd = math.gcd(cur.val , prev.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next
        return head
#time: O( A * n )  a is math.gcd
#space: O(1)