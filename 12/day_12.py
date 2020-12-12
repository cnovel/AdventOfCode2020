import time


def h_to_l(h):
    if h == 0:
        return 'N'
    if h == 1:
        return 'E'
    if h == 2:
        return 'S'
    return 'W'


def advance(h, dist, e, n):
    if h == 'N':
        return e, n+dist
    if h == 'E':
        return e+dist, n
    if h == 'S':
        return e, n-dist
    if h == 'W':
        return e-dist, n
    return e, n


def rotate_wp(wp, delta):
    wp0 = wp[0]
    wp1 = wp[1]
    if delta == 1:
        wp0 = wp[1]
        wp1 = -wp[0]
    elif delta == 2:
        wp0 = -wp[0]
        wp1 = -wp[1]
    elif delta == 3:
        wp0 = -wp[1]
        wp1 = wp[0]
    wp[0] = wp0
    wp[1] = wp1


def main():
    with open("input.txt", 'r') as f:
        commands = [(line.strip()[0], int(line.strip()[1:])) for line in f.readlines()]
        east = 0
        north = 0
        heading = 1  # North = 0, East = 1, South = 2, West = 3
        for cmd in commands:
            if cmd[0] in 'RL':
                delta = cmd[1] / 90 * (-1 if cmd[0] == 'L' else 1)
                heading = (heading+delta) % 4
                continue
            east, north = advance(cmd[0] if cmd[0] != 'F' else h_to_l(heading), cmd[1], east, north)
        print(f"East = {east}, North = {north}, MD = {abs(east)+abs(north)}")

        wp = [10, 1]
        east = 0
        north = 0
        for cmd in commands:
            if cmd[0] in 'NESW':
                wp[0], wp[1] = advance(cmd[0], cmd[1], wp[0], wp[1])
                continue
            if cmd[0] in 'RL':
                delta = cmd[1] / 90 * (-1 if cmd[0] == 'L' else 1) % 4
                rotate_wp(wp, delta)
                continue
            east += wp[0]*cmd[1]
            north += wp[1]*cmd[1]
        print(f"East = {east}, North = {north}, MD = {abs(east) + abs(north)}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
