"""
time complexity: O(2^n) due to the nature of recursive nature of binary tree
space complexity: O(n) depending on the length of the array
"""


def get_nth_fibonacci(num):
    if num == 2:
        return 1
    elif num == 1:
        return 0
    else:
        return get_nth_fibonacci(num - 1) + get_nth_fibonacci(num - 2)


print(get_nth_fibonacci(4))
