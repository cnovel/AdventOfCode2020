import time


def find_bags(bag: str, d, found):
    bags = []
    search = []
    for k, v in d.items():
        if k not in found and bag in [b[1] for b in v]:
            bags.append(k)
            found.append(k)
            search.append(k)
    for b in search:
        bags += find_bags(b, d, found)
    return bags


def count_bags(bag: str, d):
    res = 0
    in_bags = d[bag]
    for b in in_bags:
        res += b[0] * (1 + count_bags(b[1], d))
    return res


def main():
    with open("input.txt", 'r') as f:
        rules = [line.strip() for line in f.readlines()]
        d = {}
        for rule in rules:
            parts = [p.strip() for p in rule.split("contain")]
            b = parts[0][0:-4].strip()
            c = []
            if parts[1] != "no other bags.":
                bags = [b[0:-4].strip() for b in parts[1][0:-1].split(',')]
                bags = [(int(b[0]), b[2:].strip()) for b in bags]
                c = bags
            d[b] = c
        print("Part 1:", len(find_bags("shiny gold", d, [])))
        print("Part 2:", count_bags("shiny gold", d))


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
