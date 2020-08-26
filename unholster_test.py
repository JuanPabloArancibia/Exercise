from fractions import Fraction
import re
import math
lst = []
# def addingFractions(fractions):
#     for fraction in fractions:
#         # print(fraction)
#         n1, n2 = fraction.split("+")
#
#         n1 = Fraction(n1)
#         n2 = Fraction(n2)
#         total = n1 + n2
#         lst.append(str(total))
#
#     print(lst)


def addingFractions(fractions):
    for fraction in fractions:
        num1, num2 = fraction.split("+")
        num1_up, num1_down = str(num1).split("/")
        num2_up, num2_down = str(num2).split("/")
        # print(num1_up, num1_down)
        sum_up = int(num1_up) + int(num2_up)
        # print(sum_up)
        div = math.gcd(sum_up, int(num1_down))

        red_sum = sum_up // div
        red_down = int(num1_down) // div

        lst.append("{}/{}".format(red_sum, red_down))
    print(lst)


addingFractions(["2/6+2/6", "7/10+13/10"])
