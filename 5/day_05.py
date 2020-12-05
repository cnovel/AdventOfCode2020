import time


def code_to_int(code: str):
    r = 0
    for i in range(0, len(code)):
        if code[i] in ['B', 'R']:
            r += 2**(len(code) - 1 - i)
    return r


def main():
    with open("input.txt", 'r') as f:
        codes = [line.strip() for line in f.readlines()]
        seats = sorted([code_to_int(code[0:7]) * 8 + code_to_int(code[-3:]) for code in codes])
        print(f"Max seat id is {max(seats)}")
        free_seats = [seats[i] + 1 for i in range(0, len(seats) - 1) if seats[i+1] - seats[i] == 2]
        print(f"My seat id is {free_seats[0]}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
