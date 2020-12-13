import time


def in_sum(i, window):
    for j in range(0, len(window)):
        for k in range(j+1, len(window)):
            if window[j]+window[k] == i:
                return True
    return False


def get_wrong_num(numbers, buffer_size):
    moving_window = numbers[0:buffer_size]
    for i in range(buffer_size, len(numbers)):
        if not in_sum(numbers[i], moving_window):
            return numbers[i]
        moving_window.pop(0)
        moving_window.append(numbers[i])
    return -1


def get_min_max_sum(wrong_num, numbers):
    for i in range(0, len(numbers)):
        s = numbers[i]
        for j in range(i + 1, len(numbers)):
            s += numbers[j]
            if s == wrong_num:
                return min(numbers[i:j+1]) + max(numbers[i:j+1])
            if s > wrong_num:
                break
    return 0


def main():
    buffer_size = 25
    with open("input.txt", 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
        wrong_num = get_wrong_num(numbers, buffer_size)
        print(f"Wrong number is {wrong_num}")
        print(f"Weakness is {get_min_max_sum(wrong_num, numbers)}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
