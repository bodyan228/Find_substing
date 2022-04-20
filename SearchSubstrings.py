from BMH import testingBMH
from KMP import testingKMP
from Brute_Force import testing_Brute_Force
from Rabin_Karp import testing_al_RabinKarp


if __name__ == '__main__':

    with open("input.txt") as file:
        original = file.read()
    pattern = "k"
    testingBMH(original, pattern)
    testingKMP(original, pattern)
    testing_Brute_Force(original, pattern)
    testing_al_RabinKarp(original, pattern)
