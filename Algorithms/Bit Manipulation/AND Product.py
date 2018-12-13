t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    bin_a = bin(a)[2:]
    ans = ['0'] * len(bin_a)
    for i in range(len(bin_a)):
        if bin_a[i] == '0':
            continue

        biggest_before_zero = bin_a[:i] + '1' * (len(bin_a) - i)

        if int(biggest_before_zero, 2) >= b:
            ans[i] = '1';
    print(int("".join(ans), 2))