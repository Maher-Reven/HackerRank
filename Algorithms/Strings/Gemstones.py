import sys

def rstripped(fh):
    for line in fh:
        yield line.rstrip()

next(sys.stdin) # Ignore first line
clean_stdin = rstripped(sys.stdin)
gemstones = set(next(clean_stdin))
for line in clean_stdin:
    gemstones.intersection_update(list(line))
print(len(gemstones))