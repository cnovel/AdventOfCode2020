import time


def main():
    with open("input.txt", 'r') as f:
        joltages = sorted([int(line.strip()) for line in f.readlines()])
        diff_1 = 0
        diff_3 = 1
        jolt = 0
        for j in joltages:
            if j-jolt == 1:
                diff_1 += 1
            elif j-jolt == 3:
                diff_3 += 1
            jolt = j
        jolt += 3
        print(f"Diff 1 = {diff_1}, diff 3 = {diff_3}, product = {diff_1*diff_3}, max joltage = {jolt}")

        count = [[j, 0] for j in joltages]
        count.append([jolt, 1])
        count.insert(0, [0, 0])
        for j in range(len(count) - 2, -1, -1):
            s = sum([x[1] for x in count if 0 <= x[0] - count[j][0] <= 3])
            count[j][1] = s
        print(f"Arrangements = {count[0][1]}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")