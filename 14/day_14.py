import time


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def get_values(i, mask):
    val = [i]
    for k in range(0, len(mask)):
        bit_nb = len(mask) - 1 - k
        if mask[k] == '0':
            continue
        if mask[k] == '1':
            val = [set_bit(v, bit_nb) for v in val]
        if mask[k] == 'X':
            val = [set_bit(v, bit_nb) for v in val] + [clear_bit(v, bit_nb) for v in val]
    return val


def main():
    with open("input.txt", 'r') as f:
        infos = [line.strip().split(' = ') for line in f.readlines()]
        d = {}
        for info in infos:
            if 'mask' in info[0]:
                mask = info[1]
                continue
            i = int(info[0][4:-1])
            nb = int(info[1])
            for k in range(0, len(mask)):
                bit_nb = len(mask) - 1 - k
                if mask[k] == '0':
                    nb = clear_bit(nb, bit_nb)
                if mask[k] == '1':
                    nb = set_bit(nb, bit_nb)
            d[i] = nb
        print(f"Part 1 = {sum(d.values())}")

        # Part 2
        d.clear()
        for info in infos:
            if 'mask' in info[0]:
                mask = info[1]
                continue
            i = int(info[0][4:-1])
            nb = int(info[1])
            val = get_values(i, mask)
            for v in val:
                d[v] = nb
        print(f"Part 2 = {sum(d.values())}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
