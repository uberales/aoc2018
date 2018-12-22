# -*- coding: utf-8 -*-

import re

data = ''
with open('input.txt') as f:
    data = f.read().strip()

pattern = '([0-9]*) players; last marble is worth ([0-9]*) points'

players = 0
last_worth = 0

matches = re.findall(pattern, data)


players = int(matches[0][0])
last_worth = int(matches[0][1]) * 100

#players = 9
#last_worth = 32
#players = 10
#last_worth = 1618
#players = 17
#last_worth = 1104
#players = 13
#last_worth = 7999

circle = [0]
current_i = 0
marble = 0
player = -1
scores = [0] * players

while True:
    player = (player + 1) % players
    marble += 1
    if marble % 23 == 0:
        current_i = (current_i - 7) % len(circle)
        removed = circle.pop(current_i)
        current_i = (current_i) % len(circle)
        score = marble + removed
        scores[player] += score
#        print('scoring', marble, removed, score)
#        if score >= last_worth:
#            break
    else:
        current_i = (current_i + 1) % len(circle) + 1
        circle.insert(current_i, marble)
        
        
#    print(player, marble, circle[current_i], circle)
    if (marble >= last_worth):
        break
    elif marble % 10000 == 0:
        print(marble)

print(max(scores))