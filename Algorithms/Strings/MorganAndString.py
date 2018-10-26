'''
26 OCT, 2018
@author: Graves88si(Maher Krde)

'''
n = int(input().strip())
for loop in range(n) :
    strA = input().strip()
    strB = input().strip()
    lenA = len(strA)
    lenB = len(strB)
    
    # since ord('[') > ord('Z')
    strA1 = strA+'['
    strB1 = strB+'['
    
    indxA = 0
    indxB = 0
    result = []
    for i in range(lenA+lenB) :
        if indxA == lenA or indxB == lenB : break
        elif (strA1[indxA:] < strB1[indxB:]) : 
            result.append(strA[indxA])
            indxA+=1
        else :
            result.append(strB[indxB])
            indxB+=1
    res = "".join(result)+strA[indxA:]+strB[indxB:]
    print(res)