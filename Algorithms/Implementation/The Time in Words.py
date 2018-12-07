h, m = int(input()), int(input())
if m > 30:
    h += 1
    m = m - 60
nums = ('~!@#', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', '*&^%$')
w = {0 : "%s minutes"%nums[abs(m)], 1 : "one minute", 15 : "quarter", 30 : "half"}
_ = '' if m == 0 else "past" if m > 0 else "to"
if m == 0:
    print(nums[h], "o' clock")
else:
    print(w[abs(m) * int(abs(m) in (1, 15, 30))], _, nums[h])