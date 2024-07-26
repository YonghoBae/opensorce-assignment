import threading
import time

class SumCalculator:
    total = 0
    def __init__(self, num):
        self.num = num


    def calculate_sum(self):
        self.total = sum(range(self.num + 1))
        print(f"1+2+3+......+ {self.num} = {self.total}")

sum1 = SumCalculator(1000)
sum2 = SumCalculator(100000)
sum3 = SumCalculator(10000000)

th1 = threading.Thread(target=sum1.calculate_sum)
th2 = threading.Thread(target=sum2.calculate_sum)
th3 = threading.Thread(target=sum3.calculate_sum)

th1.start()
th2.start()
th3.start()
