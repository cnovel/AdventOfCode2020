import time

tic = time.perf_counter()
with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]
    valid = 0
    for line in lines:
        split_line = line.split(" ")
        password = split_line[2]
        letter = split_line[1][0]  # split_line 1 = a:, we only want a
        pos = [int(x) - 1 for x in split_line[0].split("-")]
        if (password[pos[0]] == letter and password[pos[1]] != letter) or \
                (password[pos[0]] != letter and password[pos[1]] == letter):
            valid += 1
    toc = time.perf_counter()
    print(f"{valid} valid passwords found in {toc - tic:0.3f}s")
