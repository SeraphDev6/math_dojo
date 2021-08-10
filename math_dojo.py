from random import randint
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self,num, *nums):
        self.result += num
        self.result += sum(nums)
        return self
    def subtract(self,num, *nums):
        self.result -= num
        self.result -= sum(nums)
        return self
    def print_res(self):
        print(self)
    def __str__(self):
        return str(self.result)

m=MathDojo()
m.add(1).add(2,3,5,6).add(87,43,18,19,19,29,19,19,25,300).subtract(23,1).subtract(99,123,123,4).subtract(9,9,9,9,9,9,99).print_res()