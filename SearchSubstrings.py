import time
import Last_Occurrence
from memory_profiler import profile


class search_substrings:

    def RabbinKarp(self, string, substring):#Алгоритм Раббина-Карпа
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

    def BruthForce(self, string, substring):#Поиск "грубой силой"
        start = time.time()
        flag = False
        i = 0
        count = 0
        first_index = -1
        flag2 = False

        for pos in range(len(string)):

            if i == len(substring):
                i = 0
                count += 1
                if not flag2:
                    first_index = pos - i - 1
                    flag2 = True

            if string[pos] == substring[i]:
                flag = True
                i += 1

            else:
                i = 0
        end = time.time()
        print("Время работы алгоритма поиска 'грубой силой': {}."
              "Количество вхождений: {}.".format(end - start, count))
        return first_index

    def find_prefix(self, substring):#Нахождение префикса для алгоритма Кнута-Морриса-Пратта
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

    def KMP(self, string, substring):#Сам алгоритм Кнутта-Морриса-Пратта
        start = time.time()
        k = 0
        l = 0
        P = self.find_prefix(substring)
        count = 0
        first_ind = -1
        flag = False

        while k < len(string):
            if substring[l] == string[k]:
                k += 1
                l += 1

                if l == len(substring):
                    count += 1
                    l = 0
                    if not flag:
                        first_ind = k - len(substring)
                        flag = True
            elif l > 0:
                l = P[l-1]
            else:
                k += 1
        end = time.time()
        print("Время работы алгоритма Кнутта-Морриса-Пратта:{}. "
              "Количество вхождений: {}".format(end - start, count))
        return first_ind

    def BMH(self, string, substring):# Алогритм Бойера-Мура-Хорспула
        occurrence = Last_Occurrence
        start = time.time()
        alphabet = set(string)
        count = 0
        last = occurrence.last_occurrence(substring, alphabet)
        m = len(substring)
        n = len(string)
        i = m - 1  # text index
        j = m - 1  # substring index
        flag = False
        first_index = -1
        while i < n:
            if string[i] == substring[j]:
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
                l = last(string[i])
                i = i + m - min(j, 1 + l)
                j = m - 1

        end = time.time()
        print("Время работы алгоритма Бойера-Мура-Хорспула: {}. "
              "Количество вхождений: {}".format(end - start, count))
        return first_index


if __name__ == '__main__':

    with open("input.txt") as file:
        str = file.read()
    substr = "k"
    search = search_substrings()
    search.RabbinKarp(str, substr)
    search.KMP(str, substr)
    search.BruthForce(str, substr)
    search.BMH(str, substr)
