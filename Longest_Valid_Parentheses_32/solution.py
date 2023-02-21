class Solution:
    def longestValidParentheses(self, s: str) -> int:
        arr=[0]*len(s)
        max_arr=0
        for i in range(1,len(s)):
            if s[i]=='(':
                continue
            else:
                temp=i-arr[i-1]-1 
                if(temp>=0):
                    if(s[temp]=='('):
                        if(temp-1>=0):
                            arr[i]=arr[i-1]+2+arr[temp-1]
                        else:
                            arr[i]=arr[i-1]+2
                if arr[i]>max_arr:
                    max_arr=arr[i]
        return max_arr 