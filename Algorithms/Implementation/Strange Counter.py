t = int(input())
print((1 << ((t + 2) // 3).bit_length()) * 3 - 2 - t)