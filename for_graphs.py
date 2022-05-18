import toaster
from Algorithms.bmh import BMH
from Algorithms.kmp import KMP
from Algorithms.brute_force import Brute_Force
from Algorithms.rabin_karp import RabinCarp


def get_data():
    res_brute_time = []
    res_rk_time = []
    res_bmh_time = []
    res_kmp_time = []
    res_brute_mem = []
    res_rk_mem = []
    res_bmh_mem = []
    res_kmp_mem = []
    word_list = ["Веретена", "с", "разных", "сторон", "равномерно", "и", "не",
                "умолкая",  "шумели", "."]
    with open("for_graphs.txt") as file:
        original = file.read()

    for i in range(10):
        pattern = ' '.join(word_list[:i+1])
        res = toaster.Statistics(
            Brute_Force(original, pattern))\
            .collecting_statistics()
        res_brute_time.append(res[0])
        res_brute_mem.append(res[1])
    for i in range(10):
        pattern = ' '.join(word_list[:i+1])
        res = toaster.Statistics(RabinCarp(original, pattern))\
            .collecting_statistics()
        res_rk_time.append(res[0])
        res_rk_mem.append(res[1])
    for i in range(10):
        pattern = ' '.join(word_list[:i+1])
        res = toaster.Statistics(KMP(original, pattern))\
            .collecting_statistics()
        res_kmp_time.append(res[0])
        res_kmp_mem.append(res[1])
    for i in range(10):
        pattern = ' '.join(word_list[:i+1])
        res = toaster.Statistics(BMH(original, pattern))\
            .collecting_statistics()
        res_bmh_time.append(res[0])
        res_bmh_mem.append(res[1])
    return res_brute_time, res_rk_time, res_bmh_time, res_kmp_time,\
        res_brute_mem, res_rk_mem, res_bmh_mem, res_kmp_mem


a = "asdas"
a.find()