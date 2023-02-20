def isits(s,t):
    if len(s)==0 :
        return True
    if len(t)==0 :
        return False
    if s[0]==t[0]:
        return isits(s[1:], t[1:])
    else:
        return isits(s, t[1:])

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return isits(s,t)