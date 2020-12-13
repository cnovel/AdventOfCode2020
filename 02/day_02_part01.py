import time

tic = time.perf_counter()
with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]
    valid = 0
    for line in lines:
        split_line = line.split(" ")
        password = split_line[2]
        letter = split_line[1][0]  # split_line 1 = a:, we only want a
        r = [int(x) for x in split_line[0].split("-")]
        letter_count = password.count(letter)
        if r[0] <= letter_count <= r[1]:
            valid += 1
    toc = time.perf_counter()
    print(f"{valid} valid passwords found in {toc - tic:0.3f}s")
