class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        T=[False]*(amount+1)
        N=[float('inf')]*(amount+1)
        N[0]=0
        T[0]=True
        for i in range(1,len(T)):
            temp=False
            temp_num=float('inf')
            for j in coins:
                if (j>i):
                    continue
                else:
                    if T[i-j]==True:
                        temp=True
                        temp_num=min(temp_num,N[i-j]+1)
            T[i]=temp
            N[i]=temp_num
        if T[amount]==False:
            return -1
        else:
            return N[amount]
