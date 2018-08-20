import random
import numpy


def sumTest(number):
    sumNumber = 0
    for i in range(1, number+1):
        sumNumber += i
    return sumNumber


print(sumTest(10))
print(sumTest(1000))


print(random.randrange(1,7))

numberTest= [1,2,3,4,5]
avg = sum(numberTest, 0) / len(numberTest)

print(avg)

numberTest2 = numpy.array([1,2,3,4,5])
avg2 = numpy.mean(numberTest2)

print(avg2)

new_list = list(range(1, 7))
print(new_list)

avg3 = numpy.mean(new_list)

print(avg3)