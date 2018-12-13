import sys

def abbreviation(a, b):
    if len(a) == 0:
        return len(b) == 0
    if len(b) == 0:
        return all(x.islower() for x in a)
    if a[0] == b[0]:
        return abbreviation(a[1:], b[1:])
    if a[0].isupper():
        return False
    if b[0].isupper() and a[0] == b[0].lower():
        return abbreviation(a[1:], b[1:]) or abbreviation(a[1:], b)
    else:
        return abbreviation(a[1:], b)

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        a = raw_input().strip()
        b = raw_input().strip()
        result = abbreviation(a, b)
        print "YES" if result else "NO"