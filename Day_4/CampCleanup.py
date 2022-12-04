""" 
Advent of Code - HÍ 2022 - Day 4
@Author Halldór Jens Vilhjálmsson
"""

# Misc
pairs = []
fullyOverlapped = 0
overlap = 0

# Read input file
with open('input.txt', 'r', encoding='utf-8') as inpf:
    lines = inpf.readlines()

# Data cleanup
for line in lines:
    x,y = line.strip().split(",")
    a,b = x.split("-")
    c,d = y.split("-")
    pairs.append(((int(a), int(b)), (int(c), int(d))))

# Solving
for p in pairs:
    if (p[1][0] <= p[0][0] and p[0][1] <= p[1][1]) or p[0][0] <= p[1][0] and p[1][1] <= p[0][1]:
        fullyOverlapped += 1
    if max(p[0][0], p[1][0]) <= min(p[0][1], p[1][1]):
        overlap += 1

print('Tasks that fully overlap:', fullyOverlapped)
print('Tasks that overlap at all:', overlap)