""" 
Advent of Code - HÍ 2022 - Day 5
@Author Halldór Jens Vilhjálmsson
"""

from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()

stackArray = [[] for _ in range(10)]

for i in range(8):
    lines[i] = lines[i].replace('[', '')
    lines[i] = lines[i].replace(']', '')
    lines[i] = lines[i].replace('    ', '0')
    lines[i] = lines[i].replace(' ', '')
    cntr = 0
    for char in lines[i]:
        cntr += 1
        if char != '0' and char != '\n':
            stackArray[cntr].append(char)

for subStack in stackArray:
    subStack = subStack.reverse()

stackArrayII = deepcopy(stackArray)

for line in lines[10:]:
    _,amount,_,prev,_,new = line.split()

    for _ in range(int(amount)):
        if stackArray[int(prev)]:
            stackArray[int(new)].append(stackArray[int(prev)].pop())

reval = 'Solution 1: '

for subStack in stackArray:
    if not subStack: continue
    reval += subStack.pop()

print(reval)

for line in lines[10:]:
    _,amount,_,prev,_,new = line.split()
    tmp = []

    for _ in range(int(amount)):
        if stackArrayII[int(prev)]:
            tmp.append(stackArrayII[int(prev)].pop())

    while tmp:
        stackArrayII[int(new)].append(tmp.pop())

reval = 'Solution 2: '

for subStack in stackArrayII:
    if not subStack: continue
    reval += subStack.pop()

print(reval)