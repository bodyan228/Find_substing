import argparse
from Algorithms.bmh import testingBMH
from Algorithms.kmp import testingKMP
from Algorithms.brute_force import testing_Brute_Force
from Algorithms.rabin_karp import testing_rabin_carp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("original", help="Введите оригинальную строку")
    parser.add_argument("pattern", help="Введите подстроку")
    args = parser.parse_args()

    if args.original == "input.txt":
        with open("input.txt") as file:
            args.original = file.read()

    testing_Brute_Force(args.original, args.pattern)
    testingKMP(args.original, args.pattern)
    testingBMH(args.original, args.pattern)
    testing_rabin_carp(args.original, args.pattern)
