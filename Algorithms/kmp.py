import time
import tracemalloc


def find_prefix(substring):

    p = [0] * len(substring)
    j = 0
    i = 1
    while i < len(substring):

        if substring[i] == substring[j]:
            p[i] = j + 1
            i += 1
            j += 1

        elif j == 0:
            p[i] = 0
            i += 1

        else:
            j = p[j - 1]
    return p


def testingKMP(original_string, pattern):
    tracemalloc.start()
    start = time.time()
    k = 0
    pattern_index = 0
    list_of_prefix = find_prefix(pattern)
    count = 0
    first_ind = -1
    flag = False

    while k < len(original_string):
        if pattern[pattern_index] == original_string[k]:
            k += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                count += 1
                pattern_index = 0
                if not flag:
                    first_ind = k - 1
                    flag = True
        elif pattern_index > 0:
            pattern_index = list_of_prefix[pattern_index - 1]
        else:
            k += 1
    end = time.time()

    with open("out.txt", "a") as out:
        out.write("Время работы алгоритма Кнутта-Морриса-Пратта: {}. \n"
                  "Количество вхождений: {}. \n"
                  "Максимальное количество выделяемой памяти: {} KB. \n\n"
                  .format(end - start, count,
                        tracemalloc.get_traced_memory()[1]/1024))
    tracemalloc.stop()

    return first_ind
