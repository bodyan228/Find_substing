from init_class import Find


class KMP(Find):

    name = "Кнут-Моррис-Пратт"
    pattern = ''
    original = ''
    count = 0
    first_index = -1

    def __init__(self, original, pattern):
        super().__init__(original, pattern)

    def testing(self):
        k = 0
        pattern_index = 0
        list_of_prefix = [0] * len(self.pattern)
        j = 0
        i = 1
        while i < len(self.pattern):

            if self.pattern[i] == self.pattern[j]:
                list_of_prefix[i] = j + 1
                i += 1
                j += 1

            elif j == 0:
                list_of_prefix[i] = 0
                i += 1

            else:
                j = list_of_prefix[j - 1]

        flag = False

        while k < len(self.original):
            if self.pattern[pattern_index] == self.original[k]:
                k += 1
                pattern_index += 1

                if pattern_index == len(self.pattern):
                    self.count += 1
                    pattern_index = 0
                    if not flag:
                        self.first_index = k - 1
                        flag = True
            elif pattern_index > 0:
                pattern_index = list_of_prefix[pattern_index - 1]
            else:
                k += 1

        return self.first_index, self.count
