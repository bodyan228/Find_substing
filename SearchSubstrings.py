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

        for pos in range(len_string - len_substring + 1):
            hs = hash(string[pos: pos + len_substring])

            if hs == hash_substring:

                if string[pos:pos + len_substring] == substring:
                    count += 1
                    # end = time.time()
                    # print("Время работы алгоритма Раббина-Карпа :{}".format(
                    #     end - start))
                    # return pos

        end = time.time()
        print("Время работы алгоритма Раббина-Карпа: {}."
              "Количество вхождений: {}.".format(end - start, count))

    def BruthForce(self, string, substring):#Поиск "грубой силой"
        start = time.time()
        flag = 0
        i = 0
        count = 0

        for pos in range(len(string)):

            if i == len(substring):
                i = 0
                count += 1
                # return pos - i

            if string[pos] == substring[i]:
                flag = 1
                i += 1

            else:
                i = 0

        # if flag == 1:
        #     end = time.time()
        #     print("Время работы алгоритма поиска 'грубой силой': {}".
        #         format(end - start))
        end = time.time()
        print("Время работы алгоритма поиска 'грубой силой': {}."
              "Количество вхождений: {}.".format(end - start, count))

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
        # first_ind = 0

        while k < len(string):
            if substring[l] == string[k]:
                k += 1
                l += 1

                if l == len(substring):
                    count += 1
                    l = 0
                    # end = time.time()
                    # print("Время работы алгоритма Кнутта-Морриса-Пратта: {}".
                    #     format(end - start))
                    # first_ind = k - len(substring)
            elif l > 0:
                l = P[l-1]
            else:
                k += 1
        end = time.time()
        print("Время работы алгоритма Кнутта-Морриса-Пратта:{}. "
              "Количество вхождений: {}".format(end - start, count))
        return -1

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
        while i < n:
            if string[i] == substring[j]:
                if j == 0:
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


if __name__ == '__main__':

    with open("input.txt") as file:
        str = file.read()
    substr = "хороший вид"
    search = search_substrings()
    search.RabbinKarp(str, substr)
    search.KMP(str, substr)
    search.BruthForce(str, substr)
    search.BMH(str, substr)
