from collections import Counter
n = int(input())
for _ in range(n):
    test = input()
    length = len(test)
    if len(test) % 2 != 0:
        print("-1")
    else:
        s1 = Counter(test[:length//2])
        s2 = Counter(test[length//2:])
        diff = s1 - s2
        print(sum(diff.values()))