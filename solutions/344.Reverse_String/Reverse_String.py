class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        return self.reverseString(s[len(s)/2:]) + \
            self.reverseString(s[:len(s)/2])

    def reverseStringClassic(self, s):
        # classic shit
        i = 0
        j = len(s) - 1
        s = list(s)
        # for i in xrange(len(s)):
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return ''.join(s)

    def idontknowwtfiwrote(self, s):
        # result = ""
        # length = len(s)
        # for i in xrange(1,length+1):
        #     result += s[length-i]

        # for i in reversed(s):
        #     result += i
        # return result
        pass

    def reverseStringPythonic(self, s):
        return s[::-1]
