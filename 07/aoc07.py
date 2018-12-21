# -*- coding: utf-8 -*-

import re

data = ''
with open('input.txt') as f:
    data = f.read()

pattern = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'

edges = [(m[0], m[1]) for m in re.findall(pattern, data)]

steps = set()
steps = steps.union(set([e[0] for e in edges]))
steps = steps.union(set([e[1] for e in edges]))

steps = sorted(list(steps))

graph = {}
times = {}
dependencies = {}
init_step = '*'

for step in steps:
    graph[step] = []
    times[step] = ord(step) - 4
    dependencies[step] = []

for edge in edges:
    graph[edge[0]].append(edge[1])
    dependencies[edge[1]].append(edge[0])

def Task_A(graph):
    step_order = ''
    step_avail = {}
    
    prev_candidate = init_step
    
    while len(steps) > 0:
        candidates = []
        for s in steps:
            count = 0
            for n in graph:
                e = graph[n]
                count += 1 if s in e else 0
            if count == 0:
                candidates.append(s)
        candidates.sort()
    
    
        step_avail[prev_candidate] = candidates
        prev_candidate = candidates[0]
    
        print(prev_candidate, candidates)
        step_order += prev_candidate
        steps.remove(prev_candidate)
        graph.pop(prev_candidate)
        
    print(step_order)
    return (step_order, step_avail)

step_order, step_avail = Task_A(dict(graph))

av_b = step_avail

m = 0;
w_count = 5;
workers = ['-'] * w_count;
counter = [0] * w_count
candidates = step_avail.pop('*')
done = set()

def DoneDependencies(done, dependencies, step):
    step_dep = dependencies[step]
    done_dep = True
    for d in step_dep:
        if not(d in done):
            done_dep = False
            break
    return done_dep

while True:
    for i in range(w_count):
        if workers[i] == '-':
            for c_i in range(len(candidates)):
                if DoneDependencies(done, dependencies, candidates[c_i]):
                    workers[i] = candidates.pop(c_i)
                    counter[i] = times[workers[i]]
                    break
                
    print('{:04d}'.format(m), ''.join(workers), ''.join(candidates))
    
    done_now = []
    for i in range(w_count):
        if workers[i] != '-':
            counter[i] -= 1
            if counter[i] == 0:
                done_now.append(workers[i])
                workers[i] = '-'
                counter[i] = 0
    
    done.update(done_now)
        
    for d in done_now:
        if d != step_order[-1]:
            candidates_now = step_avail.pop(d)
            for c in candidates_now:
                if not(c in done) and not(c in candidates) and not(c in workers):
                    candidates.append(c)
    
    m += 1
    if len(done) == len(times):
        break

print('{:03d}'.format(m), ''.join(workers), ''.join(candidates))
print(m)
    
        
        