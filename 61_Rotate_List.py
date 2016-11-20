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
        # 1->2->3->4 2, 3->4->1->2

        # Original thought:
        # you have to traverse to the link where the leftover links count is K,
        # and set link.next = None, then traverse to the end of the list,
        # and set end.next = Original_head

        # Edit: First Traverse to the end of the list,
        # set end.next to Original_head,t hen traverse again to
        # the place that need to be set to None,
        # Return the next as the new head.

        if not head:
            return head
        og_head = head
        count = 1
        while head.next:
            count += 1
            head = head.next
        # End of list
        head.next = og_head
        # modulo when overtraverse
        for i in xrange(count - (k % count)):
            head = head.next
        new_head = head.next
        head.next = None
        return new_head

    def traverseLinkedList(self, input_dic, head=None):
        if head:
            cur = head
        else:
            cur = input_dic['ln1']
        while cur is not None:
            print cur.val
            cur = cur.next

    def printAllLinkValue(self, input_dic):
        for key in input_dic.keys():
            try:
                print str(input_dic[key].val) + \
                    '->' + str(input_dic[key].next.val)
            except:
                print key + "-> None"


class Inputs(object):
    '''
    This is a class that will gradually deal with all leetcode input cases.

    Usage Example:
    input_data = [1, 2, 3, 4]
    inp = Inputs(input_data, 'linkedlist')
    input_dic = inp.returnResult()
    '''
    def __init__(self, x, input_type):
        self.input_data = x
        self.input_type = input_type
        self.input_result = None
        if self.input_type == 'linkedlist':
            self.toLinkedList(self.input_data)

    def toLinkedList(self, input_data):
        '''
        Convert input list into a dic of LinkedNodes as a linkedlist.
        '''
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
        '''
        Return the result.
        '''
        return self.input_result


if __name__ == "__main__":
    input_data = [1, 2, 3, 4]
    inp = Inputs(input_data, 'linkedlist')
    input_dic = inp.returnResult()

    sol = Solution()
    print 'Original Traversal:'
    # sol.printAllLinkValue(input_dic)
    sol.traverseLinkedList(input_dic)

    print 'After Rotation:'
    new_head = sol.rotateRight(input_dic['ln1'], 3)
    sol.traverseLinkedList(input_dic, new_head)
    # sol.printAllLinkValue(input_dic)
