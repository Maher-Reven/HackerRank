ui = input().split()
x = int(ui[0])
print(eval(input()) == int(ui[1]))



#2nd solution
print(eval(__import__('re').sub(r'(\d+)\s*(\d+)\s*(.*)', r'[\2] == [\3 for x in [\1]]', __import__('sys').stdin.read())))