n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


while(len(arr)):
    print(len(arr))
    arr = [x - min(arr) for x in arr if x - min(arr)>0]