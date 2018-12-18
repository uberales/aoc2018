# -*- coding: utf-8 -*-

import re
import numpy as np

data = ''
claims = []

pattern = '#([0-9]*) @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)'

with open('input.txt') as f:
    data = f.read()

claims = [(int(c[0]), int(c[1]), int(c[2]), int(c[3]), int(c[4])) for c in re.findall(pattern, data)]

sq_size = 2000
square = np.zeros((sq_size, sq_size), dtype='int')

for c in claims:
    for r_i in range(c[2], c[2]+c[4]):
        for c_i in range(c[1], c[1]+c[3]):
            square[r_i, c_i] += 1


count_overlap = 0
for r_i in range(sq_size):
    for c_i in range(sq_size):
        if square[r_i, c_i] > 1:
            count_overlap += 1
            
print(count_overlap)

for c in claims:
    overlaps = False
    for r_i in range(c[2], c[2]+c[4]):
        for c_i in range(c[1], c[1]+c[3]):
            if square[r_i, c_i] > 1:
                overlaps = True
                break
        if overlaps:
            break
    if not(overlaps):
        print c[0]
