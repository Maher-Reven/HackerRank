# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
array = list(map(int, input().split()))
array = list(filter(lambda data: array.count(data) == 1, array))
print(array[0])