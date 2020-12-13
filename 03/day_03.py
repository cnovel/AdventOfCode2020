import time
from functools import reduce

tic = time.perf_counter()


def trees(lines, s):
    bottom = len(lines)
    width = len(lines[0])
    t = 0
    x = 0
    y = 0
    while y + s[1] < bottom:
        x = (x + s[0]) % width
        y += s[1]
        if lines[y][x] == '#':
            t += 1
    return t


with open("input.txt", 'r') as f:
    forest = [x.strip() for x in f.readlines() if x.strip()]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    l_trees = [trees(forest, s) for s in slopes]
    for i in range(0, len(slopes)):
        print(f"{l_trees[i]} trees for slope {slopes[i]}")
    print(f"{reduce(lambda x, y: x*y, l_trees)} multiplied trees")

toc = time.perf_counter()
print(f"Done in {toc - tic:0.4f}s")
