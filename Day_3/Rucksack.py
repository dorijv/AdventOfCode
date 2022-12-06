""" 
Advent of Code - HÍ 2022 - Day 3
@Author Halldór Jens Vilhjálmsson
"""

total_priority = 0

with open('input.txt', 'r', encoding='utf-8') as inpf:
    lines = inpf.readlines()

for line in lines:
	first = line[:len(line)//2]
	second = line[len(line)//2:]
	common = (set(first)&set(second)).pop()
	if common.isupper():
		total_priority += ord(common)-64+26
	else:
		total_priority += ord(common)-96

print('Solution 1:', total_priority)

total_priority = 0

for i in range(0, len(lines), 3):
	print(i)
	first = lines[i].replace('\n', '')
	second = lines[i+1].replace('\n', '')
	third = lines[i+2].replace('\n', '')
	common = (set(first)&set(second)&set(third)).pop()

	if common.isupper():
		total_priority += ord(common)-64+26
	else:
		total_priority += ord(common)-96

print('Solution 2:', total_priority)