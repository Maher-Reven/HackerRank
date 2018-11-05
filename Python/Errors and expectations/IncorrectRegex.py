import re as r
for _ in range(int(input())):
    try:
        print(bool(r.compile(input())))
    except:
        print('False')