import time
import random
import datetime

from Values import Rand

class BubbleSort():
    def __init__(self, values):
        self.values = values
        self.values_unsorted = values

    def sort(self):
        self.start_time = datetime.datetime.now()

        for i in range(len(self.values)):
            for j in range(len(self.values) - i-1):
                if self.values[j] > self.values[j+1]:
                    self.values[j], self.values[j+1] = self.values[j+1], self.values[j]

        self.end_time = datetime.datetime.now()

        # print("Bubble time: ", self.end_time-self.start_time)
        self.elapsed_time = self.end_time - self.start_time
        # print(self.values)

values = Rand(1, 10000, 5000)
# print(values)
bubble = BubbleSort(values)
bubble.sort()
