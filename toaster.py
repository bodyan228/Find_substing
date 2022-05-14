import tracemalloc
import time
from init_class import Find


class Statistics:

    time: float
    fat_memory_block: float
    average_memory: float
    delegate: Find

    def __init__(self, delegate):
        self.delegate = delegate

    def collecting_statistics(self):
        self.time, self.average_memory, self.fat_memory_block \
            = Toaster(self.delegate).get_measure()
        with open("out.txt", "a") as file:
            file.write("Время работы алгоритма {}: {} с.\n"
              "Количество вхождений: {}.\n"
              "Индекс первого вхождения: {}.\n"
              "Среднее количество потребляемой памяти {} KB.\n"
              "Максимально выделенный блок памяти: {} KB.\n\n"
              .format(self.delegate.name, self.time,
              self.delegate.count, self.delegate.first_index,
              self.average_memory, self.fat_memory_block))
        return self.time, self.average_memory


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
        return Statistics.time, Statistics.memory[0]/1024,\
            Statistics.memory[1]/1024
