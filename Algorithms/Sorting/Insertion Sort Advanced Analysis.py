#py2
def mergesort(ar):
    ic=0
    if len(ar)>1:
        mid=len(ar)/2
        left,right=ar[:mid],ar[mid:]
        ic+=mergesort(left)
        ic+=mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                ar[k]=left[i]
                i+=1
            else:
                ar[k]=right[j]
                j+=1
                ic+=mid-i
            k+=1
        while i<len(left):
            ar[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            ar[k]=right[j]
            j+=1
            k+=1
    return ic
n = input()
for iterate in range( n ):
    x = input()
    a = [ int( i ) for i in raw_input().strip().split() ]
    answer = mergesort(a)
    # Write code to compute answer using x, a and answer
    print answer