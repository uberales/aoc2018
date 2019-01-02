# -*- coding: utf-8 -*-



directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def GetDistance(maze, r_0, c_0):
    n_rows = len(maze)
    n_cols = len(maze[0])
    
    d_grid = []
    for i in range(n_rows):
        d_grid.append([-1] * n_cols)
        
    def Distance(d_grid, curr_distance, grid_coords): 
        next_coords = set()
        for g in grid_coords:
            d_grid[g[0]][g[1]] = curr_distance
            
            for d in directions:
                r = g[0] + d[0]
                c = g[1] + d[1]
                if c >= 0 and r >= 0 and r < n_rows and c < n_cols:
                    if d_grid[r][c] < 0 and maze[r][c] == ".":
                        next_coords.add((r, c))
                        
        if len(next_coords) > 0:
            Distance(d_grid, curr_distance + 1, next_coords)
    
    Distance(d_grid, 0, set([(r_0, c_0)]))

    return d_grid

def ShortestPath(d_grid, r_0, c_0):
    
    path = [[(r_0, c_0)]]
    
    def AppendSegment(d_grid, distance, points):
        new_points = set()
        for p in points:
            for d in directions:
                r = p[0] + d[0]
                c = p[1] + d[1]
                if d_grid[r][c] == distance - 1:
                    new_points.add((r, c))
        path.append(list(new_points))
        if distance - 1 > 0:
            AppendSegment(d_grid, distance - 1, new_points)
    
    AppendSegment(d_grid, d_grid[r_0][c_0], set([(r_0, c_0)]))
    
    return path

def CoverMaze(maze, units, dead):
    for u in units:
        if not(u in dead):
            maze[u["pos"][0]][u["pos"][1]] = u["type"]
    return maze

def ClearMaze(maze):
    for r_i in range(len(maze)):
        for c_i in range(len(maze[r_i])):
            cell = maze[r_i][c_i]
            if cell == 'E' or cell == 'G':
                maze[r_i][c_i] = "."

def PrintMaze(maze, separator = '', units = None):
    for r_i in range(len(maze)):
        r_str = separator.join([str(c) for c in maze[r_i]])
        if units:
            u_row = [u for u in units if u["pos"][0] == r_i]
            u_row.sort(key = lambda u: u["pos"][1])
            u_str = ", ".join([u["type"] + "(" + str(u["hp"]) + ")" for u in u_row])
            r_str += separator + " " + u_str
        print(r_str)



attack_power = 3
outcome = {}

while True:
    
    maze = []
    
    with open('input.txt') as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip().split(' ')
            l = l[0]
            row = list(l)
            maze.append(row)
                
    units = []      
    dead = []
    
    n_rows = len(maze)
    n_cols = len(maze[0])
    
    for r_i in range(n_rows):
        row = maze[r_i]
        for c_i in range(n_cols):
            cell = row[c_i]
            if cell == 'E':
                u = {'type': cell, 'pos': (r_i, c_i), "power": attack_power, "hp": 200}
                units.append(u)
            elif cell == 'G':
                u = {'type': cell, 'pos': (r_i, c_i), "power": 3, "hp": 200}
                units.append(u)
    
    ClearMaze(maze)
    CoverMaze(maze, units, dead)
    
    round_no = 0
    
#    print("Initial")
#    PrintMaze(maze, units=units)    
#    print()
    
    dead = list()
    
    while True:
        round_no += 1
        units.sort(key = lambda u: (u["pos"][0], u["pos"][1]))
        
        finished = False
        complete_round = True
        died = list()
        for u_i in range(len(units)):
            u = units[u_i]
            
            if not(u in dead):
                ClearMaze(maze)
                CoverMaze(maze, units, dead)
                targets = []
                for t in units:
                    if t != u and t["type"] != u["type"] and not(t in dead):
                        targets.append(t)
                
                if len(targets) == 0:
                    finished = True
                    complete_round = False
                else:
                    open_squares = []
                    in_range = []
                    d_grid = GetDistance(maze, u["pos"][0], u["pos"][1])
                    
                    for t in targets:
                        for d in directions:
                            r = t["pos"][0] + d[0]
                            c = t["pos"][1] + d[1]
                            if maze[r][c] == "." and d_grid[r][c] > 0:
                                open_squares.append((d_grid[r][c], r, c))
                            if r == u["pos"][0] and c == u["pos"][1]:
                                in_range.append(t)
                    
                    if len(in_range) == 0 and len(open_squares) > 0:
                        open_squares.sort(key=lambda s: (s[0], s[1], s[2]))
                        path = ShortestPath(d_grid, open_squares[0][1], open_squares[0][2])
                        first_steps = path[-2]
                        first_steps.sort(key=lambda s: (s[0], s[1]))
                        u["pos"] = first_steps[0]
                    
                        for t in targets:
                            for d in directions:
                                r = t["pos"][0] + d[0]
                                c = t["pos"][1] + d[1]
                                if r == u["pos"][0] and c == u["pos"][1]:
                                    in_range.append(t)
                    
                    if len(in_range) > 0:
                        in_range.sort(key=lambda t: (t["hp"], t["pos"][0], t["pos"][1]))
                        target = in_range[0]
                        target["hp"] -= u["power"]
                        
                        if target["hp"] <= 0:
                            dead.append(target)
                            died.append(target)
                    
    
        for u in died:
            units.remove(u)
    
        if finished:
            if not(complete_round):
#                print('Finished in incomplete round')
                round_no -= 1   
            break
    
        ClearMaze(maze)
        CoverMaze(maze, units, dead)
#        print("Round", round_no)
#        PrintMaze(maze, units=units)    
#        print()
    
    ClearMaze(maze)
    CoverMaze(maze, units, dead)
    print("Final, rounds:", round_no)
    PrintMaze(maze, units=units)   
    
    remaining_hp = 0
    for u in units:
        remaining_hp += u["hp"]
    
    
    outcome[attack_power] = (units[0]["type"], round_no * remaining_hp)
    print("Outcome:", attack_power, outcome[attack_power])
    print()
    if units[0]["type"] == "E":
        elves_alive = True
        for u in dead:
            if u["type"] == "E":
                elves_alive = False
        if elves_alive:
            break
    attack_power += 1

print('Task 1:', outcome[3])
print('Task 2:', outcome[attack_power])