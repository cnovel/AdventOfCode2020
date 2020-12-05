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
        max_seat = 0
        list_seat = []
        for code in codes:
            s = code_to_int(code[0:7]) * 8 + code_to_int(code[-3:])
            list_seat.append(s)
            max_seat = max(max_seat, s)
        print(f"Max seat id is {max_seat}")
        list_seat.sort()
        for i in range(0, len(list_seat) - 1):
            if list_seat[i+1] - list_seat[i] == 2:  # There's the gap!
                print(f"My seat id is {list_seat[i] + 1}")
                break


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
