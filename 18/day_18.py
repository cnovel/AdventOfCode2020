import time


def find_sub_line(line, i):
    c = 1
    for k in range(i+1, len(line)):
        if line[k] == '(':
            c += 1
        if line[k] == ')':
            c -= 1
            if c == 0:
                return line[i+1:k]
    return line[i:]


def simple_maths(line):
    res = 0
    i = 0
    op = '+'
    while i < len(line):
        if line[i] == '(':
            sub_line = find_sub_line(line, i)
            res = res + simple_maths(sub_line) if op == '+' else res * simple_maths(sub_line)
            i += len(sub_line) + 2
        else:
            res = res + int(line[i]) if op == '+' else res * int(line[i])
            i += 1
        if i < len(line):
            op = line[i]
        i += 1
    return res


def advanced_maths(line):
    res = 1
    i = 0
    next_op = '+'
    while i < len(line):
        c = 0
        while next_op == '+':
            if line[i] == '(':
                sub_line = find_sub_line(line, i)
                c += advanced_maths(sub_line)
                i += len(sub_line) + 1
            else:
                c += int(line[i])
            if i+1 < len(line):
                next_op = line[i+1]
            else:
                next_op = None
            i += 2
        res *= c
        next_op = '+'
    return res


def main():
    with open("input.txt", 'r') as f:
        lines = [''.join(line.strip().split(' ')) for line in f.readlines()]
        print(f"Complete sum = {sum([simple_maths(line) for line in lines])}")
        print(f"Complete sum = {sum([advanced_maths(line) for line in lines])}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
