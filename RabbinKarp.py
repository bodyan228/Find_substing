import time


def RabbinKarp(string, substring: str):#Алгоритм Раббина-Карпа
    start = time.time()
    len_string = len(string)
    len_substring = len(substring)
    hash_substring = hash(substring)

    for pos in range(len_string - len_substring + 1):
        hs = hash(string[pos: pos + len_substring])

        if hs == hash_substring:

            if string[pos:pos + len_substring] == substring:
                end = time.time()
                print("Время работы алгоритма Раббина-Карпа :{}".format(
                    end - start))
                return pos

    end = time.time()
    print("Время работы алгоритма Раббина-Карпа :{}".format(end-start))
    return -1


def BruthForce(string, substring: str):#Поиск "грубой силой"
    start = time.time()
    flag = 0
    i = 0

    for pos in range(len(string)):

        if i == len(substring):
            end = time.time()
            print("Время работы алгоритма поиска 'грубой силой': {}".
                  format(end - start))
            return pos - i

        if string[pos] == substring[i]:
            flag = 1
            i += 1

        else:
            i = 0

    if flag == 1:
        end = time.time()
        print("Время работы алгоритма поиска 'грубой силой': {}".
              format(end - start))
        return -1


def find_prefix(substring):#Нахождение префикса для алгоритма Кнута-Морриса-Пратта
    p = [0]*len(substring)
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
            j = p[j-1]
    return p


def KMP(string, substring):#Сам алгоритм Кнутта-Морриса-Пратта
    start = time.time()
    k = 0
    l = 0
    P = find_prefix(substring)

    while k < len(string):
        if substring[l] == string[k]:
            k += 1
            l += 1

            if l == len(substring):
                end = time.time()
                print("Время работы алгоритма Кнутта-Морриса-Пратта: {}".
                    format(end - start))
                return k - len(substring)
        elif l > 0:
            l = P[l-1]
        else:
            k += 1
    end = time.time()
    print("Время работы алгоритма Кнутта-Морриса-Пратта:{}".
        format(end - start))
    return -1


def BMH(string, substring):# Алогритм Бойера-Мура-Хорспула
    start = time.time()
    unique_symbols = set()
    m = len(substring)
    dict_offset = {}

    for i in range(m-2, -1, -1):
        if substring[i] not in unique_symbols:
            dict_offset[substring[i]] = m - i - 1
            unique_symbols.add(substring[i])

    if substring[m-1] not in unique_symbols:
        dict_offset[substring[m-1]] = m
    dict_offset['*'] = m

    n = len(string)

    if n >= m:
        i = m - 1

        while i < n:
            k = 0
            for j in range(m-1, -1, -1):

                if string[i-k] != substring[j]:

                    if j == m-1:

                        offset = dict_offset[string[i]] \
                            if dict_offset.get(string[i], False) \
                            else dict_offset['*']

                    else:
                        offset = dict_offset[substring[j]]
                    i += offset
                    break

                k += 1

            if j == 0:
                end = time.time()
                print("Время работы алгоритма Бойера-Мура_Хорспула: {}".
                    format(end - start))
                return i - k + 1

    else:
        end = time.time()
        print("Время работы алгоритма Бойера-Мура-Хорспула: {}".
              format(end - start))
        return -1


if __name__ == '__main__':

    with open("input.txt") as file:
        str = file.read()
    substr = input("Введите подстроку:")
    print(KMP(str, substr))
    print(BruthForce(str, substr))
    print(RabbinKarp(str, substr))
    print(BMH(str, substr))
