import time


def testing_al_RabinKarp(string, substring):  # Алгоритм Раббина-Карпа
    start = time.time()
    len_string = len(string)
    len_substring = len(substring)
    hash_substring = hash(substring)
    count = 0
    flag = False
    first_index = -1

    for pos in range(len_string - len_substring + 1):
        hs = hash(string[pos: pos + len_substring])

        if hs == hash_substring:

            if string[pos:pos + len_substring] == substring:
                count += 1
                if not flag:
                    first_index = pos
                    flag = True
    end = time.time()
    print("Время работы алгоритма Раббина-Карпа: {}."
          "Количество вхождений: {}.".format(end - start, count))
    return first_index
