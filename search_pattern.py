import argparse
import toaster
from Algorithms.bmh import BMH
from Algorithms.kmp import KMP
from Algorithms.brute_force import Brute_Force
from Algorithms.rabin_karp import RabinCarp

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("original", help="Введите оригинальную строку")
    parser.add_argument("pattern", help="Введите подстроку")
    args = parser.parse_args()

    if args.original == "input.log":
        with open("input.log") as file:
            args.original = file.read()

    toaster.Statistics(Brute_Force(args.original, args.pattern))\
        .collecting_statistics()
    toaster.Statistics(KMP(args.original, args.pattern))\
        .collecting_statistics()
    toaster.Statistics(BMH(args.original, args.pattern))\
        .collecting_statistics()
    toaster.Statistics(RabinCarp(args.original, args.pattern))\
        .collecting_statistics()
