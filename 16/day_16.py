import time
from functools import reduce


def is_valid_somewhere(rules, i):
    for ranges in rules.values():
        for r in ranges:
            if r[0] <= i <= r[1]:
                return True
    return False


def column_match_rule(c, ranges, valid_tickets):
    for ticket in valid_tickets:
        valid = False
        for r in ranges:
            if r[0] <= ticket[c] <= r[1]:
                valid = True
        if not valid:
            return False
    return True


def main():
    with open("input.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        rules = {}
        for i in range(0, len(lines)):
            if lines[i] == '':
                ticket = i+2
                nearby_tickets = ticket + 3
                break
            s = lines[i].split(': ')
            ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in s[1].split(" or ")]
            rules[s[0]] = ranges

        my_ticket = [int(x) for x in lines[ticket].split(',')]
        error_rate = 0
        valid_tickets = []
        for i in range(nearby_tickets, len(lines)):
            to_check = [int(x) for x in lines[i].split(',')]
            error = sum([x for x in to_check if not is_valid_somewhere(rules, x)])
            if error == 0:
                valid_tickets.append(to_check)
            error_rate += error
        print(f"Error rate is {error_rate}")

        found = set()
        rules_pair = {}
        work = [(k, v) for k, v in rules.items()]
        while len(work) > 0:
            field, ranges = work.pop(0)
            columns_to_check = [i for i in range(0, len(valid_tickets[0])) if i not in found]
            matching_col = [c for c in columns_to_check if column_match_rule(c, ranges, valid_tickets)]
            if len(matching_col) == 1:
                rules_pair[field] = matching_col[0]
                found.add(matching_col[0])
            else:
                work.append((field, ranges))

        departures = [my_ticket[x] for k, x in rules_pair.items() if 'departure' in k]
        if departures:
            print(f"Departure product = {reduce((lambda x, y: x * y), departures)}")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
