from Bubble import BubbleSort
from Insertion import InsertionSort
from Values import Rand

from tabulate import tabulate

class Comparator:
    def __init__(self, n):
        self.headers = ['Sort Function', 'N', 'Time']
        self.n = n
        self.values = Rand(1, 100, n)

        self.bubble = BubbleSort(self.values)
        self.insertion = InsertionSort(self.values)

        self.run()

    def run(self):
        self.bubble.sort()
        self.insertion.sort()

        self.data = [['Bubble', self.n, self.bubble.elapsed_time],
                     ['Insertion', self.n, self.insertion.elapsed_time]]
        
        self.display()

    def display(self):
        print(tabulate(self.data, headers=self.headers, tablefmt="grid"))

comp = Comparator(25)
