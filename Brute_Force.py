import time


def testing_Brute_Force(string, substring):  # Поиск "грубой силой"
    start = time.time()
    i = 0
    count = 0
    first_index = -1
    flag = False

    for pos, el in enumerate(string):

        if i == len(substring):
            i = 0
            count += 1
            if not flag:
                first_index = pos - i - 1
                flag = True

        if el == substring[i]:
            i += 1

        else:
            i = 0
    end = time.time()
    print("Время работы алгоритма поиска 'грубой силой': {}."
          "Количество вхождений: {}.".format(end - start, count))
    return first_index
