from init_class import Find


class RabinCarp(Find):

    name = "Рабин-Карп"
    original = ''
    pattern = ''
    first_index = -1
    count = 0

    def __init__(self, original, pattern):
        super().__init__(original, pattern)

    def get_hash(self, some_string: str) -> int:
        result = 0

        for pos, el in enumerate(some_string):
            result = (17 * result + ord(el)) % 256
        return result

    def testing(self):
        str_length = len(self.original)
        pattern_length = len(self.pattern)
        degree = 1

        for i in range(1, pattern_length):
            degree = (degree * 17) % 256

        substring_hash = self.get_hash(self.pattern)
        string_hash = self.get_hash(self.original[:pattern_length])
        flag = False

        for i in range(str_length - pattern_length + 1):
            if string_hash == substring_hash \
                    and self.original[i:i + pattern_length] == self.pattern:
                self.count += 1
                if not flag:
                    self.first_index = i - pattern_length + 1
                    flag = True
            if i < str_length - pattern_length:
                string_hash = ((string_hash - ord(self.original[i]) * degree)
                               * 17 + ord(
                            self.original[i + pattern_length])) % 256

            if string_hash < 0:
                string_hash += 256

        return self.first_index, self.count
