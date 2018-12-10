n=int(input())
for _ in range(n):
    st=[str(x) for x in input().strip()]
    diff=[abs(ord(a)-ord(b)) for a,b in zip(st,st[1:])]
    print("Funny" if (diff==diff[::-1]) else "Not Funny")