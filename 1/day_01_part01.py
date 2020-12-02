import time


def process():
    with open("input.txt", 'r') as f:
        lines = [int(x.strip()) for x in f.readlines()]
        for i in range(0, len(lines)):
            for j in range(i+1, len(lines)):
                if lines[i]+lines[j] == 2020:
                    print(lines[i]*lines[j])
                    return


tic = time.perf_counter()
process()
toc = time.perf_counter()
print(f"Found in {toc - tic:0.3f}s")
