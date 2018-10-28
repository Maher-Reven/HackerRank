from collections import OrderedDict
dic = OrderedDict()
for x in range(int(input())):
    word = input()
    dic[word] = dic.setdefault(word, 0) + 1
print(len(dic))
for item in dic:
    print(dic[item], end=' ')