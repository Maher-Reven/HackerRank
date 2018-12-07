m = [2]
for i in range(int(input())-1):
    m.append(int(3*m[i]/2))
print(sum(m))




#2nd solution

# n = int(input().strip())
# total = 2;
# liked = 2;
# for _ in range(n-1):
#     liked = liked * 3//2
#     total += liked
# print(total)