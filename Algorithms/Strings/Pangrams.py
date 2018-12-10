from collections import Counter
print("pangram" if len(Counter(input().lower())) == 27 else "not pangram")



#2nd solution

import string
s = input().strip().lower()
for i in string.whitespace + string.punctuation:
    if i in s:
        s = s.replace(i, '')
if len(set(s)) == 26:
    print ("pangram")
else:
    print ("not pangram")