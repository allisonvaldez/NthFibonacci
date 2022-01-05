"""
time: O(2^n) due to the nature of recursive nature of fibonacci calls
space complexity: O(n) depending on the length of the array
"""


def get_nth_fibonacci(num):
    # base case to calculate second number in array
    if num == 2:
        return 1
    # base case to calculate first number in array
    elif num == 1:
        return 0
    # how to calculate remaining numbers of the array
    else:
        return get_nth_fibonacci(num - 1) + get_nth_fibonacci(num - 2)


print(get_nth_fibonacci(10))
