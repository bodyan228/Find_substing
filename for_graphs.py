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
    with open("for_graphs.txt") as file:
        original = file.read()

    for i in range(10):
        res = toaster.Statistics(
            Brute_Force(original, "необычный случай был"))\
            .collecting_statistics()
        res_brute_time.append(res[0])
        res_brute_mem.append(res[1])
        original.join("a")
    for i in range(10):
        res = toaster.Statistics(RabinCarp(original, "необычный случай был"))\
            .collecting_statistics()
        res_rk_time.append(res[0])
        res_rk_mem.append(res[1])
        original.join("a")
    for i in range(10):
        res = toaster.Statistics(KMP(original, "необычный случай был"))\
            .collecting_statistics()
        res_kmp_time.append(res[0])
        res_kmp_mem.append(res[1])
        original.join("a")
    for i in range(10):
        res = toaster.Statistics(BMH(original, "необычный случай был"))\
            .collecting_statistics()
        res_bmh_time.append(res[0])
        res_bmh_mem.append(res[1])
        original.join("a")
    return res_brute_time, res_rk_time, res_bmh_time, res_kmp_time,\
        res_brute_mem, res_rk_mem, res_bmh_mem, res_kmp_mem
