import time
import re

field_names = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
field_integers = {'byr', 'iyr', 'eyr'}
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


class Passport:
    def __init__(self, fields):
        self.info = {}
        for field in fields:
            p = field.split(":")
            self.info[p[0]] = p[1] if p[0] not in field_integers else int(p[1])

    def is_valid(self, strict: bool):
        if not field_names.issubset(set(self.info.keys())):
            return False
        if not strict:
            return True

        if not 1920 <= self.info["byr"] <= 2002 \
                or not 2010 <= self.info["iyr"] <= 2020 \
                or not 2020 <= self.info["eyr"] <= 2030:
            return False

        if self.info["hgt"].endswith("cm"):
            if not 150 <= int(self.info["hgt"][:-2]) <= 193:
                return False
        elif self.info["hgt"].endswith("in"):
            if not 59 <= int(self.info["hgt"][:-2]) <= 76:
                return False
        else:
            return False

        if not re.search(r'^#(?:[0-9a-fA-F]{6})$', self.info['hcl']):
            return False

        if self.info["ecl"] not in eye_colors:
            return False

        if not re.search(r'^(?:[0-9]{9})$', self.info['pid']):
            return False
        return True


def main():
    with open("input.txt", 'r') as f:
        passports = [line.replace("\n", " ").strip().split(" ") for line in f.read().split("\n\n")]
        print(f"{sum(map(lambda p: Passport(p).is_valid(False), passports))} loosely valid passports")
        print(f"{sum(map(lambda p: Passport(p).is_valid(True), passports))} strictly valid passports")


if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.3f}s")
