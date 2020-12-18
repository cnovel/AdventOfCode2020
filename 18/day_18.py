import time


def simple_math(line):
    res = [0]
    operator = ['+']
    for c in line:
        if c not in ['+', '*', '(', ')']:
            res[-1] = res[-1]+int(c) if operator[-1] == '+' else res[-1]*int(c)
            operator.pop()
            continue
        if c in ['+', '*']:
            operator.append(c)
        elif c == '(':
            res.append(0)
            operator.append('+')
        elif c == ')':
            res[-2] = res[-2]+res[-1] if operator[-1] == '+' else res[-2]*res[-1]
            operator.pop()
            res.pop()
    return res[0]


def find_subline(line, i):
    c = 1
    for k in range(i+1, len(line)):
        if line[k] == '(':
            c += 1
        if line[k] == ')':
            c -= 1
            if c == 0:
                return line[i+1:k]
    return line[i:]


def advanced_maths(line):
    res = 1
    i = 0
    while i < len(line):
        if line[i] == '(':
            sub_line = find_subline(line, i)
            c = advanced_maths(sub_line)
            i += len(sub_line) + 1
        else:
            c = int(line[i])
        next_op = line[i+1] if i+1 < len(line) else None
        end_i = i
        while next_op == '+' and end_i+2 < len(line):
            end_i += 2
            if line[end_i] == '(':
                sub_line = find_subline(line, end_i)
                c += advanced_maths(sub_line)
                end_i += len(sub_line) + 1
            else:
                c += int(line[end_i])
            if end_i+1 < len(line):
                next_op = line[end_i+1]
            else:
                next_op = None
        res *= c
        i = end_i+2
    return res


def main():
    with open("input.txt", 'r') as f:
        lines = [''.join(line.strip().split(' ')) for line in f.readlines()]
        print(f"Complete sum = {sum([simple_math(line) for line in lines])}")
        print(f"Complete sum = {sum([advanced_maths(line) for line in lines])}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
