# Definition for a node in linked list.
class ListNode(object):
    def __init__(self, x, link):
        self.val = x
        self.next = link


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
        self.supported_data_structure = \
            {"array": self.toArray(self.input_data),
             "linkedlist": self.toLinkedList(self.input_data)
             }
        if self.input_type in self.supported_data_structure.keys():
            self.supported_data_structure[self.input_type]

    def toArray(self, input_data):
        self.input_result = input_data

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
