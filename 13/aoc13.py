# -*- coding: utf-8 -*-

data = ''
with open('input.txt') as f:
    data = [l.replace('\n', '').replace('\r', '') for l in f.readlines()]

mine = [list(l) for l in data]

n_rows = len(mine)
n_cols = len(mine[0])

directions = {'>': '-', '<': '-', 'v': '|', '^': '|'}

carts = [];

c_i = 0
for r in range(n_rows):
    for c in range(n_cols):
        if mine[r][c] in directions:
            cart = {"r": r, "c": c, "o": mine[r][c], "rot": 0, 'i': c_i}
            c_i += 1
            mine[r][c] = directions[mine[r][c]]
            carts.append(cart)
            print(cart)

def PrintMine(mine, carts):
    for r in range(len(mine)):
        row = mine[r]
        row_s = ''
        for c in range(len(row)):
            c_found = 0
            o_found = row[c]
            for cart in carts:
                if cart['c'] == c and cart['r'] == r:
                    o_found = cart['o']
                    c_found += 1
            if c_found > 1:
                o_found = 'X'
            row_s += o_found
        print(row_s)

collided, c_1, c_2 = DetectCollisions(carts)

turns = list('lsr');
rotation = '^>v<';

crashed = list()


while True:
    crashed_now = list()
    for cart in carts:
        if not(cart in crashed) or not(cart in crashed_now):
            d_c = 0
            d_r = 0
            
            r_base = cart["r"]
            
            if cart["o"] == "^":
                d_r = -1
            elif cart["o"] == ">":
                d_c = 1
            elif cart["o"] == "v":
                d_r = 1
            elif cart["o"] == "<":
                d_c = -1
            cart["r"] += d_r
            cart["c"] += d_c
            
            for oc in carts:
                if not(oc["i"] == cart["i"]):
                    if oc["c"] == cart["c"] and oc["r"] == cart["r"]:
                        print('collision', oc["c"], oc["r"])
                        crashed_now.append(oc)
                        crashed_now.append(cart)
                    
            
    #        print(d_r, d_c)
            m = mine[cart["r"]][cart["c"]]
            
            if m == '+':
                turn = turns[cart["rot"]]
                cart["rot"] = (cart["rot"] + 1) % len(turns)
                if turn == 'l':
                    i_r = (rotation.index(cart["o"]) - 1) % len(rotation)
                    cart["o"] = rotation[i_r]
                elif turn == 'r':
                    i_r = (rotation.index(cart["o"]) + 1) % len(rotation)
                    cart["o"] = rotation[i_r]
                elif turn == 's':
                    pass
            elif m == '|' or m == '-':
                pass
            elif m == '/':
                if cart["o"] == '^':
                    cart["o"] = '>'
                elif cart["o"] == '>':
                    cart["o"] = '^'
                elif cart["o"] == 'v':
                    cart["o"] = '<'
                elif cart["o"] == '<':
                    cart["o"] = 'v'
                else:
                    print('error 1')
            elif m == '\\':
                if cart["o"] == '^':
                    cart["o"] = '<'
                elif cart["o"] == '>':
                    cart["o"] = 'v'
                elif cart["o"] == 'v':
                    cart["o"] = '>'
                elif cart["o"] == '<':
                    cart["o"] = '^'
                else:
                    print('error 2')        
    #    print()
    #    PrintMine(mine, carts)
    crashed.extend(crashed_now)
    for c in crashed_now:
        carts.remove(c)
    carts.sort(key=lambda c:(c["r"], c["c"]))
    if len(carts) == 1:
        print(carts[0]['c'], carts[0]['r'],)
        break
        
#PrintMine(mine, carts)

    