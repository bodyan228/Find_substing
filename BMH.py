import time


class last_occurrence:

    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]


def testingBMH(string, substring):  # Алогритм Бойера-Мура-Хорспула
    start = time.time()
    alphabet = set(string)
    count = 0
    last = last_occurrence(substring, alphabet)
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
            lt = last(string[i])
            i = i + m - min(j, 1 + lt)
            j = m - 1

    end = time.time()
    print("Время работы алгоритма Бойера-Мура-Хорспула: {}. "
          "Количество вхождений: {}".format(end - start, count))
    return first_index
