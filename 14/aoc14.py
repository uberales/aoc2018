# -*- coding: utf-8 -*-

num_recipes = 760221

recipes = [3, 7]
elf_a = 0
elf_b = 1

nr_str = str(num_recipes)
nr_l = list(nr_str)
#while len(recipes) < num_recipes + 10:
last_n = ''
while True:
    r_c = len(recipes)
    total = recipes[elf_a] + recipes[elf_b]
    if total < 10:
        recipes.append(total)
    else:
        rec_b = int(total % 10)
        rec_a = int((total - rec_b) / 10)
        recipes.append(rec_a)
        recipes.append(rec_b)
    d_a = 1 + recipes[elf_a]
    d_b = 1 + recipes[elf_b]
    l = len(recipes)
    elf_a = (elf_a + d_a) % l
    elf_b = (elf_b + d_b) % l
    
    nr_l.append(rec_a)
    nr
    if len(last_n) < len(nr_l):
        n
        
    
#    print(''.join([str(r) for r in recipes]))
#    print(elf_a, elf_b)

r_str = ''.join([str(r) for r in recipes[num_recipes:num_recipes+10]])
print(r_str)

for i in range(len(recipes) - 6):
    r_str = ''.join([str(r) for r in recipes[i:i+6]])
    if r_str == nr_str:
        print(i)
        break
    
with open('out.txt', mode="w+") as f:
    r_str = ''.join([str(r) for r in recipes])
    f.write(r_str)
