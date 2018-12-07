def minimum_distance(n, A):
    for d in range(1, n):
        for i in range(n - d):
            if A[i] == A[i+d]:
                return d
    return -1

print(minimum_distance(int(input()), [int(x) for x in input().split()]))