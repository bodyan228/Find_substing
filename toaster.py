import tracemalloc
import time
from init_class import Find


class Statistics:

    time: float
    memory: float
    delegate: Find

    def __init__(self, delegate):
        self.delegate = delegate

    def collecting_statistics(self):
        self.time, self.memory = Toaster(self.delegate).get_measure()
        with open("out.txt", "a") as out:
            out.write("Время работы алгоритма {}: {} с.\n"
                      "Количество вхождений: {}.\n"
                      "Индекс первого вхождения: {}.\n"
                      "Среднее количество потребляемой памяти {} KB.\n\n"
                      .format(self.delegate.name, self.time,
                              self.delegate.count, self.delegate.first_index,
                              self.memory))


class Toaster:

    delegate = Find

    def __init__(self, delegate):
        self.delegate = delegate

    def get_measure(self):
        start = time.time()
        tracemalloc.start()
        self.delegate.testing()
        Statistics.memory = tracemalloc.get_traced_memory()
        end = time.time()
        Statistics.time = end - start
        return Statistics.time, Statistics.memory[0]/1024
