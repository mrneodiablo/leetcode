class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s.find("()") >= 0 or s.find("[]") >= 0 or s.find("{}") >= 0:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        if len(s) > 0:
            return False
        else:
            return True
