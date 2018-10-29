from operator import itemgetter
N, M = map(int, input().split())

lst = [[int(i) for i in input().split()] for _ in range(N)]

for i in sorted(lst, key=itemgetter(int(input()))):
    print(*i)



#2nd solution    
N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)