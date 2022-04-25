import time
import tracemalloc


class last_occurrence:

    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]


def testingBMH(original_string, pattern):
    tracemalloc.start()
    start = time.time()
    alphabet = set(original_string)
    count = 0
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(original_string)
    i = m - 1  # text index
    j = m - 1  # substring index
    flag = False
    first_index = -1

    while i < n:
        if original_string[i] == pattern[j]:
            if j == 0:
                if not flag:
                    first_index = i
                    flag = True
                count += 1
                i += m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            lt = last(original_string[i])
            i = i + m - min(j, 1 + lt)
            j = m - 1
    end = time.time()

    with open("out.txt", "a") as out:
        out.write("Время работы алгоритма Бойера-Мура-Хорспула: {}. \n"
                  "Количество вхождений: {}. \n"
                  "Максимальное количество выделяемой памяти: {} KB. \n\n"
                  .format(end - start, count,
                        tracemalloc.get_traced_memory()[1]/1024))

    tracemalloc.stop()
    return first_index
