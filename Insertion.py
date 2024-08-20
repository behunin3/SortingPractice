from Values import Rand
import datetime

class InsertionSort():
    def __init__(self, values):
        self.values = values
        self.unsorted_values = values
    
    def sort(self):
        self.start_time = datetime.datetime.now()
        for i in range(1, len(self.values)):
            key = self.values[i]
            j = i - 1
            while (j >= 0 and self.values[j] > key):
                self.values[j + 1] = self.values[j]
                j = j - 1

            self.values[j + 1] = key


        self.end_time = datetime.datetime.now()
        self.elapsed_time = self.end_time - self.start_time

values = Rand(1,100, 10)
# print(values)
insert = InsertionSort(values)
insert.sort()
