import time


def init_cube(lines, cube_size, hyper):
    cube = [[[[0 for _ in range(0, cube_size)]
             for _ in range(0, cube_size)]
            for _ in range(0, cube_size)]
            for _ in range(0, cube_size if hyper else 1)]
    offset_z = int(cube_size / 2)
    offset_p = int(cube_size / 2) - int(len(lines) / 2)
    for i in range(0, len(lines)):
        line = lines[i]
        for j in range(0, len(line)):
            if line[j] == '#':
                cube[offset_z if hyper else 0][offset_z][offset_p+i][offset_p+j] = 1
    return cube


def get_neighs(w_n, c_w, i_n, j_n, k_n, c):
    n = []
    for w in range(w_n-1, w_n+2):
        if w < 0 or w >= c_w:
            continue
        for i in range(i_n-1, i_n+2):
            if i < 0 or i >= c:
                continue
            for j in range(j_n-1, j_n+2):
                if j < 0 or j >= c:
                    continue
                for k in range(k_n-1, k_n+2):
                    if k < 0 or k >= c:
                        continue
                    if w == w_n and i == i_n and j == j_n and k == k_n:
                        continue
                    n.append((w, i, j, k))
    return n


def cycle(cube):
    c = len(cube[0])
    c_w = len(cube)
    swap = [[[[0 for _ in range(0, c)] for _ in range(0, c)] for _ in range(0, c)] for _ in range(0, c_w)]
    for w in range(0, c_w):
        for i in range(0, c):
            for j in range(0, c):
                for k in range(0, c):
                    is_active = cube[w][i][j][k] == 1
                    neighs = get_neighs(w, c_w, i, j, k, c)
                    active_neighs = sum([cube[x[0]][x[1]][x[2]][x[3]] for x in neighs])
                    if is_active and not 2 <= active_neighs <= 3:
                        swap[w][i][j][k] = 1
                    elif not is_active and active_neighs == 3:
                        swap[w][i][j][k] = 1
    for w in range(0, c_w):
        for i in range(0, c):
            for j in range(0, c):
                for k in range(0, c):
                    if swap[w][i][j][k] == 1:
                        cube[w][i][j][k] = (cube[w][i][j][k] + 1) % 2


def count_active(cube):
    c = len(cube[0])
    c_w = len(cube)
    n = 0
    for w in range(0, c_w):
        for i in range(0, c):
            for j in range(0, c):
                for k in range(0, c):
                    n += cube[w][i][j][k]
    return n


def main():
    cycles = 6
    with open("input.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        cube_size = len(lines) + cycles * 2  # We gain 2 width every cycle or so
        cube = init_cube(lines, cube_size, False)
        for i in range(0, cycles):
            print(f"Cycle {i+1}")
            cycle(cube)
        print(f"Active nodes = {count_active(cube)}")
        cube = init_cube(lines, cube_size, True)
        for i in range(0, cycles):
            print(f"Cycle {i + 1}")
            cycle(cube)
        print(f"Active nodes = {count_active(cube)}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
