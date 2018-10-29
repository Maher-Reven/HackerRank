s = input().strip()
s = [i for i in s]

dicty = dict((i, 0) for i in s)

for item in s:
    dicty[item] += 1

s = [(i, dicty[i]) for i in dicty]

s.sort(key = lambda x: x[1], reverse = True)

index = 0
sub = []

for count in range(3): 
    sublist = [i for i in s if (i[1] == s[index][1])]
    sublist.sort(key = lambda x:x[0])
    sub.append(sublist)        

    index += len(sublist)

    if(index >= len(s)):
        break

sub = [j for i in sub for j in i]

for i in sub[:3]:
    print(i[0], i[1])