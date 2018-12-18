# -*- coding: utf-8 -*-

data = []
with open('input.txt') as f:
    data = [l.strip() for l in f.readlines()]

def CountsAs(s):
    letters = set(s)
    counts_2 = 0
    let_2 = ''
    counts_3 = 0
    
    for l in letters:
        n = 0
        for c in s:
            if c == l:
                n += 1
        if n == 2:
            counts_2 = 1
        elif n == 3:
            if let_2 == l:
                counts_2 = 0
            counts_3 = 1

    return (counts_2, counts_3)

def DiffPos(label_1, label_2):
    diffs = []
    for i in range(len(label_1)):
        if not(label_1[i] == label_2[i]):
            diffs.append(i)
    if len(diffs) == 1:
        return diffs[0]

    return -1
    
counts_2 = 0
counts_3 = 0

for label in data:
    (c2, c3) = CountsAs(label)
    counts_2 += c2
    counts_3 += c3

print(counts_2 * counts_3)

data = sorted(data)

label_prev = data[0]
for i in range(1, len(data)):
    label_this = data[i]
    d_i = DiffPos(label_prev, label_this)

    if d_i >= 0:
        common = ''
        for i in range(len(label_this)):
            if i != d_i:
                common += label_this[i]
        print(common)

    label_prev = label_this    
    