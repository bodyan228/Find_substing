import time


def find_prefix(substring):  # Нахождение префикса для алгоритма КМП

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


def testingKMP(string, substring):  # Сам алгоритм Кнутта-Морриса-Пратта
    start = time.time()
    k = 0
    pattern_index = 0
    list_of_prefix = find_prefix(substring)
    count = 0
    first_ind = -1
    flag = False

    while k < len(string):
        if substring[pattern_index] == string[k]:
            k += 1
            pattern_index += 1

            if pattern_index == len(substring):
                count += 1
                pattern_index = 0
                if not flag:
                    first_ind = k - len(substring)
                    flag = True
        elif pattern_index > 0:
            pattern_index = list_of_prefix[pattern_index - 1]
        else:
            k += 1
    end = time.time()
    print("Время работы алгоритма Кнутта-Морриса-Пратта:{}. "
          "Количество вхождений: {}".format(end - start, count))
    return first_ind
