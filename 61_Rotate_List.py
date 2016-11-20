# Definition for a node in linked list.
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
        if not head:
            return head

        for i in xrange(k):
            # print i
            print head.val
            head = head.next

    def traverseLinkedList(self, input_dic):
        cur = input_dic['ln1']
        while cur is not None:
            print cur.val
            cur = cur.next


class Inputs(object):
    def __init__(self, x, input_type):
        self.input_data = x
        self.input_type = input_type
        self.input_result = None
        if self.input_type == 'linkedlist':
            self.toLinkedList(self.input_data)

    def toLinkedList(self, input_data):
        input_dic = {}
        for i in reversed(input_data):
            if i != len(input_data):
                cur_node = 'ln%s' % i
                nex_node = 'ln%s' % (i + 1)
                input_dic[cur_node] = ListNode(i, input_dic[nex_node])
            else:
                cur_node = 'ln%s' % i
                input_dic[cur_node] = ListNode(i, None)
        self.input_result = input_dic

    def returnResult(self):
        return self.input_result


if __name__ == "__main__":
    input_data = [1, 2, 3, 4]
    inp = Inputs(input_data, 'linkedlist')
    input_dic = inp.returnResult()

    sol = Solution()
    # sol.traverseLinkedList(input_dic)

    sol.rotateRight(input_dic['ln1'], 3)
