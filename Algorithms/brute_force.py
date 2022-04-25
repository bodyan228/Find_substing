import time
import tracemalloc


def testing_Brute_Force(original_string, pattern):
    tracemalloc.start()
    start = time.time()
    i = 0
    count = 0
    first_index = -1
    flag = False

    for pos, el in enumerate(original_string):

        if i == len(pattern):
            i = 0
            count += 1
            if not flag:
                first_index = pos - i - 1
                flag = True

        if el == pattern[i]:
            i += 1

        else:
            i = 0
    end = time.time()

    with open("out.txt", "w") as out:
        out.write("Время работы алгоритма поиска 'грубой силой': {}. \n"
                  "Количество вхождений: {}. \n"
                  "Максимальное количество выделяемой памяти: {} KB. \n\n"
                  .format(end - start, count,
                        tracemalloc.get_traced_memory()[1]/1024))
    tracemalloc.stop()

    return first_index
