# -*- coding: utf-8 -*-

import numpy as np
import scipy.misc as smp
import seaborn as sns


data = ''
with open('input.txt') as f:
    lines = f.readlines()
    data = [l.strip().split(', ') for l in lines]

coords = [(int(d[0]), int(d[1])) for d in data]
limit = 10000

def Distance(origin, point):
    return abs(origin[0] - point[0]) + abs(origin[1] - point[1])

x_range = (min([c[0] for c in coords]), max([c[0] for c in coords]))
y_range = (min([c[1] for c in coords]), max([c[1] for c in coords]))

size_x = x_range[1]-x_range[0]
size_y = y_range[1]-y_range[0]

g_x = x_range[1]+1+50
g_y = y_range[1]+1+50

grid = np.full((g_x, g_y, 2), (-1, 0), dtype=int)
image_data = np.zeros((g_x, g_y, 3), dtype=np.uint8)
image_data_2 = np.zeros((g_x, g_y, 3), dtype=np.uint8)
palette = sns.color_palette('hls', len(coords))


limit_count = 0

for x in range(g_x):
    for y in range(g_y):
        distances = [(i, Distance(coords[i], (x, y))) for i in range(len(coords))]
        
        c = -1
        same_d = False
        d_min = max([d[1] for d in distances])
        total_d = 0
        for d in distances:
            total_d += d[1]
            if d[1] <= d_min:
                if (d[1] == d_min):
                    same_d = True
                else:
                    same_d = False
                c = d[0]
                d_min = d[1]
        if not(same_d):
            grid[x][y] = (c, total_d)
        else:
            grid[x][y] = (-1, total_d)
        
        if total_d < limit:
            limit_count += 1
            
        
        if (c >= 0):
            color = [256 * palette[c][0], 256 * palette[c][1], 256 * palette[c][2]]
            image_data[x, y] = color
        
        if (total_d < limit):
            image_data_2[x, y] = [255, 255, 255]

img = smp.toimage(image_data)
img.save('grid.png')

img = smp.toimage(image_data_2)
img.save('grid2.png')

infinite = set()

for x in range(g_x):
    infinite.add(grid[x][0][0])
    infinite.add(grid[x][-1][0])

for y in range(g_y):
    infinite.add(grid[0][y][0])
    infinite.add(grid[-1][y][0])

max_c = 0
max_c_i = 0


for i in range(len(coords)):
    if not(i in infinite):
        c_count = 0
        for x in range(g_x):
            for y in range(g_y):                
                if grid[x][y][0] == i:
                    c_count += 1
        if c_count > max_c:
            max_c = c_count
            max_c_i = i

print(max_c, max_c_i, coords[max_c_i])
print(limit_count)