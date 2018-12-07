import sys
def grow(zeit):
    if zeit == 0:
        return 1
    if zeit % 2 == 0:
        return 2 **((zeit/2) + 1) - 1
    else:
        return 2 **((zeit+3) /2) - 2

for a0 in range(int(input().strip())):
    print(int(grow(int(input().strip()))))