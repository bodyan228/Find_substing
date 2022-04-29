from init_class import Find


class Brute_Force(Find):

    name = "'грубая сила'"
    original = ''
    pattern = ''
    first_index = -1
    count = 0

    def __init__(self, original, pattern):
        super().__init__(original, pattern)

    def testing(self):
        i = 0
        flag = False

        for pos, el in enumerate(self.original):

            if i == len(self.pattern):
                i = 0
                self.count += 1
                if not flag:
                    self.first_index = pos - i - 1
                    flag = True

            if el == self.pattern[i]:
                i += 1

            else:
                i = 0

        return self.first_index, self.count
