import re

fname = 'regex_sum_72118.txt'
file = open(fname)

numlst = list()
sum = 0

for line in file:
    line = line.rstrip()
    numlst = re.findall('[0-9]+', line)
    if len(numlst) == 0: continue

    for item in numlst:
        num = int(item)
        sum += num

print(sum)
