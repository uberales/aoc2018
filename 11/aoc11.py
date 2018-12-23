# -*- coding: utf-8 -*-

import numpy as np

data = 5719

serial_number = data

n_g = 300
grid = np.zeros((n_g, n_g))

def CellPower(x, y, sn):
    rack_id = x + 10
    pl = rack_id * y
    pl += sn
    pl *= rack_id
    pl = int(pl/100)%10
    pl -= 5
    return pl

for x in range(n_x):
    for y in range(n_y):
        grid[y][x] = CellPower(x, y, serial_number)
        pass

max_pl = 0
max_x = 0
max_y = 0
for s in range(n_g):
    for x in range(n_g-s+1):
        for y in range(n_g-s+1):
            sq = grid[y:y+s,x:x+s]
            pl = np.sum(sq)
            if pl > max_pl:
                max_pl = pl
                max_x = x
                max_y = y
    
                print(max_x, max_y, s, max_pl)

print('result', max_x, max_y, max_pl)
        