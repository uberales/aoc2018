# -*- coding: utf-8 -*-

data = []
with open('input.txt') as f:
    data = [int(l.strip()) for l in f.readlines()]

final_freq = sum(data)

all_freq = set()
freq = 0;
i = 0

while True:
    freq += data[i]
    
    if freq in all_freq:
        print(freq)
        break
    else:
        all_freq.add(freq)
        
    i = (i + 1) % len(data)


