# -*- coding: utf-8 -*-

num_recipes = 760221
#num_recipes = 9
#num_recipes = 51589

recipes = [3, 7]
elf_a = 0
elf_b = 1


def AppendAndCheck(recipes, recipe, check_source, check_data):
    recipes.append(recipe)
    check_source.append(recipe)
    while len(check_source) > len(check_data):
        check_source.pop(0)
    
    check_str = ''.join([str(r) for r in check_source])
    if check_str == check_data:
        return True
    return False
    

nr_str = str(num_recipes)
nr_l = []
task_a = False
task_b = False

while True:
    r_c = len(recipes)
    total = recipes[elf_a] + recipes[elf_b]
    to_append = []
    if total < 10:
        to_append.append(total)
    else:
        rec_b = int(total % 10)
        rec_a = int((total - rec_b) / 10)
        to_append.append(rec_a)
        to_append.append(rec_b)
    
    for recipe in to_append:    
        found_recipe = AppendAndCheck(recipes, recipe, nr_l, nr_str)
        if found_recipe:
            print('Task B:', len(recipes)-len(nr_l))
            task_b = True
    
    d_a = 1 + recipes[elf_a]
    d_b = 1 + recipes[elf_b]
    l = len(recipes)
    elf_a = (elf_a + d_a) % l
    elf_b = (elf_b + d_b) % l
    
    if l >= num_recipes + 10 and not(task_a):
        task_a = True
        r_str = ''.join([str(r) for r in recipes[num_recipes:num_recipes+10]])
        print('Task A:', r_str)
    
    if task_a and task_b:
        break
    
with open('out.txt', mode="w+") as f:
    r_str = ''.join([str(r) for r in recipes])
    f.write(r_str)
