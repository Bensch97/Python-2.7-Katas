sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712, 71, 456, 21, 398, 339, 882, 848, 179, 535, 940, 472]

def question_one():
    print("Question One")
    for i in range(1, 21):
        print(i)

question_one()

def question_two():
    print("Question Two")
    for i in range(1,21):
        if (i % 2 == 0):
            print(i)

question_two()

def question_three():
    print("Question Three")
    for i in range(1,21):
        if(i % 2 != 0):
            print(i)

question_three()

def question_four():
    print("Question Four")
    for i in range (5, 101, 5):
        print(i)

question_four()

import math

def question_five():
    print("Question Five")
    for i in range(1,101):
        if (math.sqrt(i) == round(math.sqrt(i))):
            print(i)

question_five()

def question_six():
    print("Question Six")
    for i in reversed(range(1, 21)):
        print(i)

question_six()

def question_seven():
    print("Question Seven")
    for i in reversed(range(1,21)):
        if (i % 2 == 0):
            print(i)

question_seven()

def question_eight():
    print("Question Eight")
    for i in reversed(range(1,21)):
        if (i % 2 != 0):
            print(i)

question_eight()

def question_nine():
    print("Question Nine")
    for i in reversed(range(5, 101, 5)):
        print(i)

question_nine()

def question_ten():
    print("Question Ten")
    for i in reversed(range(1,101)):
        if (math.sqrt(i) == round(math.sqrt(i))):
            print(i)

question_ten()

def question_eleven():
    print("Question Eleven")
    for i in sampleArray:
        print(i)

question_eleven()

def question_twelve():
    print("Question Twelve")
    for i in sampleArray:
        if(i % 2 == 0):
            print(i)

question_twelve()

def question_thirteen():
    print("Question Thirteen")
    for i in sampleArray:
        if(i % 2 != 0):
            print(i)

question_thirteen()

def question_fourteen():
    print("Question Fourteen")
    for i in sampleArray:
        print(i ** 2)

question_fourteen()

def question_fifteen():
    print("Question Fifteen")
    sum = 0
    for i in range(1, 21):
        sum = sum + i
    print(sum)

question_fifteen()

def question_sixteen():
    print("Question Sixteen")
    sum = 0
    for i in sampleArray:
        sum = sum + i
    print(sum)

question_sixteen()

def question_seventeen():
    print("Question Seventeen")
    min = 10000
    for i in sampleArray:
        if (i < min):
            min = i
    print(min)

question_seventeen()

def question_eightteen():
    print("Question Eightteen")
    max = 0
    for i in sampleArray:
        if (i > max):
            max = i
    print(max)

question_eightteen()