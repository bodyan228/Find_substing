from init_class import Find


class BMH(Find):

    name = "Бойер-Мур-Хорспулл"
    original = ''
    pattern = ''
    count = 0
    first_index = -1

    def __init__(self, original, pattern):
        super().__init__(original, pattern)

    def testing(self):
        alphabet = set(self.original)
        occurrences = dict()

        for letter in alphabet:
            occurrences[letter] = self.pattern.rfind(letter)

        m = len(self.pattern)
        n = len(self.original)
        i = m - 1  # text index
        j = m - 1  # substring index
        flag = False

        while i < n:
            if self.original[i] == self.pattern[j]:
                if j == 0:
                    if not flag:
                        self.first_index = i
                        flag = True
                    self.count += 1
                    i += m
                    j = m - 1
                else:
                    i -= 1
                    j -= 1
            else:
                last = occurrences[self.original[i]]
                i = i + m - min(j, 1 + last)
                j = m - 1

        return self.first_index, self.count
