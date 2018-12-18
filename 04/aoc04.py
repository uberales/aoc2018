# -*- coding: utf-8 -*-

from datetime import datetime
import re

data = ''
with open('input.txt') as f:
    data = f.read()

pattern_a = '\[(.*)\] falls asleep'
pattern_w = '\[(.*)\] wakes up'
pattern_g = '\[(.*)\] Guard #([0-9]*) begins shift'

time_f = '%Y-%m-%d %H:%M'
gp = re.findall(pattern_g, data)
a = [{'t': datetime.strptime(m, time_f), 'a': 'asleep'} for m in re.findall(pattern_a, data)]
w = [{'t': datetime.strptime(m, time_f), 'a': 'wakes'} for m in re.findall(pattern_w, data)]
g = [{'t': datetime.strptime(m[0], time_f), 'g': int(m[1]), 'a': 'begins'} for m in re.findall(pattern_g, data)]

actions = a
actions.extend(w)
actions.extend(g)

actions.sort(key=lambda a:a['t'])

guard = -1
guard_rec = [0] * 60
guard_records = {};
fell_asleep = -1;

for a in actions:
    if 'g' in a:
        guard = a['g']
        if guard in guard_records:
            guard_rec = guard_records[guard]
        else:
            guard_rec = [0] * 60
            guard_records[guard] = guard_rec
        fell_asleep = -1
    elif a['a'] == 'asleep':
        fell_asleep = a['t'].minute
    elif a['a'] == 'wakes':
        wakes = a['t'].minute
        for i in range(fell_asleep, wakes):
            guard_rec[i] += 1

g_max = 0
asleep_max = 0
for g in guard_records:
    guard_rec = guard_records[g]
    asleep = sum([m for m in guard_rec])
    if asleep > asleep_max:
        asleep_max = asleep
        g_max = g

rec_max = guard_records[g_max]
print(g_max, rec_max)

asleep_max = 0
min_i = -1
for i in range(len(rec_max)):
    if rec_max[i] > asleep_max:
        asleep_max = rec_max[i]        
        min_i = i

print(min_i, rec_max[min_i])        
print(min_i * g_max)

asleep_max = 0
min_i = -1
g_max = 0

for i in range(60):
    rec_m = [(guard_records[g][i], g) for g in guard_records]
  #  rec_m.sort(key = lambda r:r[0], reverse=True)
    g_max_i = 0
    m_max = 0    
    for j in range(len(rec_m)):
        gm = rec_m[j]
        if gm[0] > m_max:
            g_max_i = j
            m_max = gm[0]
    if m_max > asleep_max:
        g_max = rec_m[g_max_i][1]
        min_i = i
        asleep_max = m_max

print(g_max, min_i, guard_records[g_max][min_i])
print(g_max * min_i)
    

        