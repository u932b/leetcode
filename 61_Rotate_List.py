# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, link):
        self.val = x
        self.next = link


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1->2->3->4 1, 4->1->2->3
        tmp2 = head
        if not head:
            return head
        for i in xrange(k):
            head = head.next
        tmp = head.next
        if not tmp:
            tmp = tmp2
        else:
            new_head = tmp
            head.next = None

            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = tmp2
        return new_head

if __name__ == "__main__":
    ln3 = ListNode(3, None)
    ln2 = ListNode(2, ln3)
    ln1 = ListNode(1, ln2)
    sol = Solution()

    # print sol.rotateRight(ln1, 1)
    cur = ln1
    while cur is not None:
        print cur.val
        cur = cur.next
