# helloworld.py
# A program that prints strings and numbers
# EECS388
# 9/6/2019
# by: Yixian Jia

import random
import statistics

print("Yixian (Adina) Jia")
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
resultSum = num1 + num2
resultAvg = statistics.mean([num1, num2])
print(num1)
print(num2)
print("Sum =", resultSum)
print("Average =", resultAvg)

