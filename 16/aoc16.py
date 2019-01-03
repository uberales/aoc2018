#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:57:23 2019

@author: ales
"""

import re

def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]

def addi(reg, a, b, c):
    reg[c] = reg[a] + b

def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]

def muli(reg, a, b, c):
    reg[c] = reg[a] * b

def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]

def bani(reg, a, b, c):
    reg[c] = reg[a] & b

def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]

def bori(reg, a, b, c):
    reg[c] = reg[a] | b

def setr(reg, a, b, c):
    reg[c] = reg[a]

def seti(reg, a, b, c):
    reg[c] = a

def gtir(reg, a, b, c):
    reg[c] = 1 if a > reg[b] else 0

def gtri(reg, a, b, c):
    reg[c] = 1 if reg[a] > b else 0

def gtrr(reg, a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0

def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0

def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0

def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0

def Equals(reg_a, reg_b):
    if len(reg_a) == len(reg_b):
        for i in range(len(reg_a)):
            if reg_a[i] != reg_b[i]:
                return False
        return True
    return False

opcodes = ['addr', 'addi', 
           'mulr', 'muli', 
           'banr', 'bani', 
           'borr', 'bori', 
           'setr', 'seti',  
           'gtir', 'gtri', 'gtrr', 
           'eqir', 'eqri', 'eqrr'
           ]

samples = []
program = []

with open('input.txt') as f:
    text = f.read()
    
    pattern = 'Before: \[([0-9]*), ([0-9]*), ([0-9]*), ([0-9]*)\]\n([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*)\nAfter:  \[([0-9]*), ([0-9]*), ([0-9]*), ([0-9]*)\]'
    matches = re.findall(pattern, text)
    for m in matches:
        m = [int(i) for i in m]
        before = m[0:4]
        instruction = m[4:8]
        after = m[8:12]
        samples.append((before, instruction, after))
    
    part_2 = text.split('\n\n\n\n')[-1]
    pattern = '([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*)'
    matches = re.findall(pattern, part_2)
    for m in matches:
        m = [int(i) for i in m]
        program.append(m)

candidates = []
for i in range(len(samples)):
    candidates.append([])

three_or_more = 0

for s_i in range(len(samples)):
    s = samples[s_i]
    opcode_n = s[1][0]
    a = s[1][1]
    b = s[1][2]
    c = s[1][3]
    after = list(s[2])
    
    for opcode_str in opcodes:
        before = list(s[0])
        globals()[opcode_str](before, a, b, c)
        if Equals(before, after):
            candidates[s_i].append((opcode_str, opcode_n))
        
    if len(candidates[s_i]) >= 3:
        three_or_more += 1

known = {}

while len(known) < len(opcodes):
    new_info = []
    codes_found = set()
    for i in range(len(candidates)):
        if len(candidates[i]) == 1:
            if not(candidates[i][0][0] in codes_found):
                new_info.append(candidates[i][0])
                codes_found.add(candidates[i][0][0])
    
    for i in range(len(candidates)):
        remove = set()
        for c in candidates[i]:
            for n_i in new_info:
                if c[0] == n_i[0]:
                    remove.add(c)
        for c in remove:
            candidates[i].remove(c)
    if len(new_info) > 0:
        for n_i in new_info:
            known[n_i[1]] = n_i[0]
    else:
        break

print(known)


    
reg = [0, 0, 0, 0]

for instruction in program:
    opcode_str = known[instruction[0]]
    a = instruction[1]
    b = instruction[2]
    c = instruction[3]
    globals()[opcode_str](reg, a, b, c)

print(three_or_more)
print(reg)
