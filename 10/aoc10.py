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


a_prev = -1
c = 0
while True:
    c += 1
    r = np.add(r, v)
    d_x = abs(np.max(r[:,0])-np.min(r[:,0]))
    d_y = abs(np.max(r[:,1])-np.min(r[:,1]))
    a = d_x * d_y
    print(c, d_x, d_y, a)
    
    if (a_prev > 0 and a_prev < a) or d_y <= 9:
        break
    a_prev = a
    
f = plt.figure()
plt.plot(r[:,0], -r[:,1], 'o')
