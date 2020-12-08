# -*- coding: utf-8 -*-

import re
import numpy as np
from matplotlib import pyplot as plt

data = ''
with open('input.txt') as f:
    data = f.read().strip()

pattern = 'position=<([ \-0-9]*), ([ \-0-9]*)> velocity=<([ \-0-9]*), ([ \-0-9]*)>'
players = 0
last_worth = 0

matches = re.findall(pattern, data)
r_0 = [(int(m[0].strip()), int(m[1].strip())) for m in matches]
v = [(int(m[2].strip()), int(m[3].strip())) for m in matches]

r_0 = np.array(r_0)
r = np.array(r_0)
v = np.array(v)


d_y_prev = abs(np.max(r[:,1])-np.min(r[:,1]))
c = 0
while True:
    c += 1
    r = np.add(r, v)
    d_y = abs(np.max(r[:,1])-np.min(r[:,1]))
    
    if d_y >= d_y_prev:
        r = np.add(r, -v)
        break
    d_y_prev = d_y
    
f = plt.figure()
plt.plot(r[:,0], -r[:,1], 'o')
