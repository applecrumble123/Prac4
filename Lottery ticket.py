import random
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44]

random.shuffle(NUMBERS)
offer = int(input("How many quick picks? "))
for i in range(offer):
    output = NUMBERS
    print("{:>2}, {:>2}, {:>2}, {:>2}, {:>2}, {:>2}".format(output.pop(),output.pop(),output.pop(),output.pop(),output.pop(),output.pop() ))