#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyinputplus as pyip

""" https://automatetheboringstuff.com/2e/chapter8/
https://pyinputplus.readthedocs.io/en/latest/
PyInputPlus has several functions for different kinds of input:

inputStr() Is like the built-in input() function but has the general PyInputPlus features. 
    You can also pass a custom validation function to it
inputNum() Ensures the user enters a number and returns an int or float, 
    depending on if the number has a decimal point in it
inputChoice() Ensures the user enters one of the provided choices
inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options
inputDatetime() Ensures the user enters a date and time
inputYesNo() Ensures the user enters a “yes” or “no” response
inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value
inputEmail() Ensures the user enters a valid email address
inputFilepath() Ensures the user enters a valid file path and filename, 
    and can optionally check that a file with that name exists
inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords, 
    or other sensitive information, aren’t displayed on the screen """


def adds_up_to_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbers_list)))
    return int(numbers)  # Return an int form of numbers.


response = pyip.inputCustom(adds_up_to_ten)
