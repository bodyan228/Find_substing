import time
import tracemalloc


def get_hash(some_string: str) -> int:
    result = 0

    for pos, el in enumerate(some_string):
        result = (17 * result + ord(el)) % 256
    return result


def testing_rabin_carp(original_string, pattern):
    tracemalloc.start()
    start = time.time()
    str_length = len(original_string)
    pattern_length = len(pattern)
    degree = 1

    for i in range(1, pattern_length):
        degree = (degree * 17) % 256

    substring_hash = get_hash(pattern)
    string_hash = get_hash(original_string[:pattern_length])
    count = 0
    first_index = -1
    flag = False

    for i in range(str_length - pattern_length + 1):
        if string_hash == substring_hash \
                and original_string[i:i + pattern_length] == pattern:
            count += 1
            if not flag:
                first_index = i - pattern_length + 1
                flag = True
        if i < str_length - pattern_length:
            string_hash = ((string_hash - ord(original_string[i]) * degree)
                        * 17 + ord(original_string[i + pattern_length])) % 256

        if string_hash < 0:
            string_hash += 256
    end = time.time()

    with open("out.txt", "a") as out:
        out.write("Время работы алгоритма Раббина-Карпа: {}. \n"
                  "Количество вхождений: {}. \n"
                  "Максимальное количество выделяемой памяти: ""{} KB. \n\n"
                  .format(end - start, count,
                        tracemalloc.get_traced_memory()[1]/1024))

    tracemalloc.stop()
    return first_index
