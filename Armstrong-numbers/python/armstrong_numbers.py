# turn input number into an array
# count array and save to variable
# save number of the index as a variable to keep track of it
# calculate the exponents
# add the answers together and return the total
# loop through array from 0 to 999 to check for armstrong numbers within and output those numbers to an array


import math
# this function determines if a number is an armstrong number or not.


def is_armstrong_number(num):
    exponent_list = []
    num_of_digits = len(str(num))

    sum_of_exponent_list = 0
    string = str(num)
    arr = [int(x) for x in str(num)]

    for i in arr:
        exponent_list.append(i ** num_of_digits)

    for j in exponent_list:
        sum_of_exponent_list += j

    if sum_of_exponent_list == num:
        return True


def find_armstrong_numbers(numbers):
    new_arr = []

    for i in numbers:
        if is_armstrong_number(i) == True:
            new_arr.append(i)

    return new_arr
