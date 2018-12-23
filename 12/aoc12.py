# -*- coding: utf-8 -*-

import re

data = ''
with open('input.txt') as f:
    data = f.read().strip()

pattern = 'initial state: ([\#\.]*)'
matches = re.findall(pattern, data)

init = matches[0]
               
pattern = '([\#\.]{5}) => ([\#\.]{1})'

matches = re.findall(pattern, data)
rules = {}
for m in matches:
    rules[m[0]] = m[1]

def Next(state, i, rules):    
    surr = ''.join(state[i-2:i+3])
    n = '.'
    if surr in rules:
        n = rules[surr]
    return n

def Wrap(state, offset):
    offset += 5
    wrap = list('.....')
    wrap.extend(list(state))
    wrap.extend(list('.....'))
    while wrap[4] == '.':
        wrap.pop(0)
        offset -= 1
    while wrap[-5] == '.':
        wrap.pop()
    return wrap, offset

state = list(init)
sl = len(state)
state, offset = Wrap(state, 0)
print(''.join([' '] * offset) + "0")
print(''.join(state))

total_n = 50000000000
#total_n = 20

def SumPots(state, offset):
    sum_n = 0
    for i in range(len(state)):
        pn = i - offset
        if state[i] == "#":
            sum_n += pn
    return sum_n

for i in range(1, total_n + 1):
    next_state = list(state)
    for j in range(2,len(next_state)-2):
        next_state[j] = Next(state, j, rules)
    state, offset = Wrap(next_state, offset)
    sum_n = SumPots(state, offset)
    print(i, sum_n, sum_n / i)
#    print(''.join([' '] * offset) + "0")
#    print(''.join(state))
sum_n = SumPots(state, offset)
print(sum_n)