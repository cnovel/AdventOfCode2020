import time
from collections import Counter
from functools import reduce


def main():
    with open("input.txt", 'r') as f:
        groups_answers = [group.strip().split("\n") for group in f.read().split("\n\n")]

        fused_answers = [reduce(lambda x, y: x+y, g) for g in groups_answers]
        print(f"Answer count is {sum([len(set(g)) for g in fused_answers])}")

        res = 0
        for i in range(0, len(groups_answers)):
            d = Counter(fused_answers[i])  # Count occurrences of each letter
            res += sum([1 if v == len(groups_answers[i]) else 0 for v in d.values()])
        print(f"Common answer count is {res}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
