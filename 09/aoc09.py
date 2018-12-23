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

circle = [0]
current_i = 0
marble = 0
player = -1
scores = [0] * players

class Link:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
    def ChainStr(self):
        vals = [str(self.val)]
        l = self.next
        while not(l == self):
            vals.append(str(l.val))
            l = l.next
        return ' '.join(vals)
    def __repr__(self):
        p = str(self.prev.val) if self.prev else '-'
        n = str(self.next.val) if self.next else '-'
        return '...{}[{}]{}...'.format(p, self.val, n)
    @staticmethod
    def Advance(link, n):
        l = link
        if n > 0:
            for i in range(n):
                l = l.next
        else:
            for i in range(abs(n)):
                l = l.prev
        return l
    @staticmethod
    def Insert(link, new_link):
        new_link.next = link.next
        new_link.prev = link
        new_link.next.prev = new_link
        link.next = new_link
        return new_link
    @staticmethod
    def Remove(link):
        ln = link.next
        lp = link.prev
        lp.next = ln
        ln.prev = lp
        return ln

        
link = Link(0)
link.next = link
link.prev = link

while True:
    player = (player + 1) % players
    marble += 1
    if marble % 23 == 0:
        link = Link.Advance(link, -7)
        removed = link.val
        link = Link.Remove(link)
        score = marble + removed
        scores[player] += score

    else:
        link = Link.Advance(link, 1)
        new_link = Link(marble)
        link = Link.Insert(link, new_link)

    if (marble >= last_worth):
        break
    elif marble % 10000 == 0:
        print(marble)


print(max(scores))