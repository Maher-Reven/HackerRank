regex_pattern = r""	# Do not delete 'r'.
import re
s = input()
args = re.split("[.,]",s)
for x in args:
    if x:
        print (x)
import re
print("\n".join(re.split(regex_pattern, input())))