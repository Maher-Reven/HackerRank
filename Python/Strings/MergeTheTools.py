string = input()
k = int(input())
n = len(string)
increment = int(n/k)
unique = []
for i in range(0, n, increment):
    subsegment = string[i:i + increment]
    for j in range(len(subsegment)):
        if subsegment.count(subsegment[j])>1:
            templist = sorted(set(subsegment), key=subsegment.index)
            finalstr = ''.join(templist)
        
    print(finalstr)