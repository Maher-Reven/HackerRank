n,c = input().split()
li = [int(i) for i in input().split()]
brian_charged = int(input())

anna_price = li.pop(int(c))

total = 0
for i in range(0,len(li)):
    total+=li[i]
total = total//2

if(brian_charged>total):
    print(brian_charged-total)
elif(brian_charged==total):
    print("Bon Appetit")