import time
import re

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


class Passport:
    def __init__(self, fields):
        self.info = {}
        for field in fields:
            p = field.split(":")
            self.info[p[0]] = p[1]

    def is_valid(self, strict: bool):
        ks = self.info.keys()
        if not ("byr" in ks and "iyr" in ks and "eyr" in ks and "hgt" in ks and
                "hcl" in ks and "ecl" in ks and "pid" in ks):
            return False
        if not strict:
            return True

        if not 1920 <= int(self.info["byr"]) <= 2002:
            return False

        if not 2010 <= int(self.info["iyr"]) <= 2020:
            return False

        if not 2020 <= int(self.info["eyr"]) <= 2030:
            return False

        if self.info["hgt"].endswith("cm"):
            if not 150 <= int(self.info["hgt"][:-2]) <= 193:
                return False
        elif self.info["hgt"].endswith("in"):
            if not 59 <= int(self.info["hgt"][:-2]) <= 76:
                return False
        else:
            return False

        if not re.search(r'^#(?:[0-9a-fA-F]{3}){2}$', self.info['hcl']):
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
