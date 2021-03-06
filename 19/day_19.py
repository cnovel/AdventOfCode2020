import time


def get_rules(lines):
    rules = {}
    for line in lines:
        if ":" not in line:
            continue
        parts = line.split(": ")
        r_id = int(parts[0])
        if 'a' in parts[1] or 'b' in parts[1]:
            rules[r_id] = parts[1][1]
            continue
        rules[r_id] = []
        set_rules = parts[1].split(' | ')
        for s in set_rules:
            rules[r_id].append([int(x) for x in s.split(' ')])
    return rules


def get_words(rules, i):
    rules_i = rules[i]
    if rules_i in ['a', 'b']:
        return [rules_i]

    possible_words = []
    for rule in rules_i:
        words = ['']
        for r in rule:
            new_words = []
            ws = get_words(rules, r)
            for w in words:
                for new_w in ws:
                    new_words.append(w+new_w)
            words = new_words.copy()
        possible_words += words
    return possible_words


def starts_with_any(line, patterns):
    for pattern in patterns:
        if line.startswith(pattern):
            return True
    return False


def main():
    with open("input.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        rules = get_rules(lines)
        patterns_42 = get_words(rules, 42)
        patterns_31 = get_words(rules, 31)
        s42 = len(patterns_42[0])
        s31 = len(patterns_31[0])

        matching_messages = 0
        for line in lines:
            # Format must be exactly 42 - 42 - 31
            if len(line) == 2*s42 + s31 and \
                    starts_with_any(line, patterns_42) and \
                    starts_with_any(line[s42:], patterns_42) and \
                    starts_with_any(line[2*s42:], patterns_31):
                matching_messages += 1
        print(f'{matching_messages} matching messages')

        matching_messages = 0
        for line in lines:
            sub_line = line
            c42 = 0
            c31 = 0
            # We don't exactly need to match the pattern 42-...-42-(42(42(...)31)31)
            # We can prune the 42s, then the 31s
            # then check we have at least 1 31 and more 42s than 31s and no other patterns
            while starts_with_any(sub_line, patterns_42):
                c42 += 1
                sub_line = sub_line[s42:]
            while starts_with_any(sub_line, patterns_31):
                sub_line = sub_line[s31:]
                c31 += 1
            if sub_line == '' and c42 > c31 > 0:
                matching_messages += 1
        print(f'{matching_messages} recursive matching messages')


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
