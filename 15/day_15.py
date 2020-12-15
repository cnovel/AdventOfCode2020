import time


def get_nth_number(in_data, n):
    spoken = {}
    last_spoken = 0
    # We will store in d the last 2 indexes of when the key was spoken
    for k in range(0, len(in_data)):
        spoken[in_data[k]] = (k, k)
        last_spoken = in_data[k]
    for i in range(len(in_data), n):
        new_spoken = spoken[last_spoken][1] - spoken[last_spoken][0]
        if new_spoken in spoken.keys():
            spoken[new_spoken] = (spoken[new_spoken][1], i)
        else:
            spoken[new_spoken] = (i, i)
        last_spoken = new_spoken

    print(f"{n}th number spoken is {last_spoken}")


def main():
    in_data = [16, 11, 15, 0, 1, 7]
    get_nth_number(in_data, 2020)
    get_nth_number(in_data, 30000000)


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
