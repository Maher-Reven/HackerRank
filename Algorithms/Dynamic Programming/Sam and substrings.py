s = input().strip()
size = len(s)
prev = int(s[0])
total = prev
for i in range (1, size):
    total= (total*10+int(s[i])*(i+1))%(10**9+7)
    prev = (total+prev)%(10**9+7)
print(prev)