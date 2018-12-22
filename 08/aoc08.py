# -*- coding: utf-8 -*-

data = ''
with open('input.txt') as f:
    text = f.read()
    data = [int(n) for n in text.strip().split(' ')]

open_nodes = []
all_nodes = []

i = 0
reading_node = True
reading_metadata = False
meta_sum = 0

while i < len(data):
    if reading_node:
        node = {"c_subnodes": data[i], "c_metadata": data[i+1], 'subnodes': [], 'metadata': []}
        if len(open_nodes) > 0 and open_nodes[-1]["c_subnodes"] > 0:
            open_nodes[-1]["subnodes"].append(node)
            open_nodes[-1]["c_subnodes"] -= 1
        open_nodes.append(node)
        i += 1
    elif reading_metadata and len(open_nodes) > 0:
        for j in range(open_nodes[-1]["c_metadata"]):
            meta_sum += data[i]
            open_nodes[-1]["metadata"].append(data[i])
            i += 1
        i -= 1
        node = open_nodes.pop()
        all_nodes.append(node)
        reading_metadata = False
    
    if len(open_nodes) == 0:
        reading_node = True
        reading_metadata = False
    else:
        last_open = open_nodes[-1]
        if last_open["c_subnodes"] == 0:
            reading_node = False
            reading_metadata = True
        else:
            reading_node = True
            reading_metadata = False
        
    
    i += 1

print(meta_sum)

def Value(node):
    val = 0
    if len(node["subnodes"]) == 0:
        val = sum(node["metadata"])
    else:
        for i in node["metadata"]:
            if (i <= len(node["subnodes"])):
                sn = node["subnodes"][i-1]
                val += Value(sn)
    return val

print(Value(all_nodes[-1]))