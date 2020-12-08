import time


def process(instructions, cur, acc):
    instructions[cur][2] = 1
    if instructions[cur][0] in ["acc", "nop"]:
        acc += int(instructions[cur][1]) if instructions[cur][0] == "acc" else 0
        cur += 1
    else:
        cur += int(instructions[cur][1])  # jmp
    return cur, acc


def terminates(instructions, cur, acc):
    while cur < len(instructions):
        if instructions[cur][2] == 1:
            return False, acc
        cur, acc = process(instructions, cur, acc)
    return True, acc


def main():
    with open("input.txt", 'r') as f:
        instructions = [[line.strip().split(" ")[0], line.strip().split(" ")[1], 0] for line in f.readlines()]
        ok, acc = terminates(instructions, 0, 0)
        print(f"Accumulator = {acc}")

        instructions = [[a[0], a[1], 0] for a in instructions]
        cur = 0
        acc = 0
        swp = 0
        while cur < len(instructions):
            cur_instr = instructions[cur][0]
            if cur_instr in ["nop", "jmp"]:
                swp += 1
                copy_instructions = [a.copy() for a in instructions]
                copy_instructions[cur][0] = "jmp" if cur_instr == "nop" else "nop"
                ok, res = terminates(copy_instructions, cur, acc)
                if ok:
                    print(f"Accumulator fixed = {res} at line {cur+1} after {swp} swaps")
                    break
            cur, acc = process(instructions, cur, acc)


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
