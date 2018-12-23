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

def Wrap(state):
    
    wrap = list('..')
    wrap.extend(list(state))
    wrap.extend(list('..'))
    return wrap

state = list(init)
sl = len(state)
state = Wrap(state)
offset = 2
print(''.join([' '] * offset) + "0")
print(''.join(state))

total_n = 50000000000

for i in range(total_n):
    offset += 2 
    next_state = list(state)
    
    for j in range(2,len(next_state)-2):
        next_state[j] = Next(state, j, rules)
    state = Wrap(next_state)
    if i % 10000 == 0:
        print(i)
#    print(''.join([' '] * offset) + "0")
#    print(''.join(state))

sum_n = 0
for i in range(len(state)):
    pn = i - offset
    if state[i] == "#":
        sum_n += pn

print(sum_n)