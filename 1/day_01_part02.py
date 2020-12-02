import time


def process():
    with open("input.txt", 'r') as f:
        lines = sorted([int(x.strip()) for x in f.readlines()])
        for i in range(0, len(lines)):
            for j in range(i + 1, len(lines)):
                # List is sorted, if number are already higher than 2020, no need to continue
                if lines[i]+lines[j] > 2020:
                    break
                for k in range(j + 1, len(lines)):
                    # No need to continue
                    if lines[i] + lines[j] + lines[k] > 2020:
                        break
                    if lines[i] + lines[j] + lines[k] == 2020:
                        print(lines[i] * lines[j] * lines[k])
                        return


tic = time.perf_counter()
process()
toc = time.perf_counter()
print(f"Found in {toc - tic:0.4f}s")