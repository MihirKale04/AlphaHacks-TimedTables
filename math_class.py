import random


class Math():
    def __init__(self):
        self.firstNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.secondNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def getnums(self):
        num1 = self.firstNum[random.randrange(0, len(self.firstNum))]
        num2 = self.secondNum[random.randrange(0, len(self.secondNum))]
        return [num1, num2]
