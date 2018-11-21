if __name__ == '__main__':
    final = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        final.append([score,name])
final.sort()
k = 0
for x in range(n):
    if final[x][0] > final[0][0]:
        k = x
        break
for x in range(n):
    if final[k][0] == final[x][0]:
        print(final[x][1])