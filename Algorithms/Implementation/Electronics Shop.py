import sys

def getMoneySpent(keyboards, drives,n,m, s):
    ans=-1
    for x in keyboards:
        for y in drives:
            if x+y<=s:
                ans=max(ans,x+y)
    return(ans)
                   
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives,n,m, s)
print(moneySpent)