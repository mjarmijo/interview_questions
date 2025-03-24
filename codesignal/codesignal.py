"""
Python interview questions (and answers) from basic to senior level

https://codesignal.com/blog/interview-prep/key-python-interview-questions-and-answers-from-basic-to-senior-level/

"""

from typing import Tuple

# Prompt: Write a Python function that takes a list of numbers and returns the sum of all elements in the list. For example, for the list [1, 2, 3, 4], the function should return 10.


def sum_it(nums: list[int]) -> int | None:
    if nums:
        sum = 0
        for i in nums:
            sum += i
        return sum
    return None

# Prompt: Build on your previous function to return the largest number in the list, in addition to the sum. For the list [1, 2, 3, 4], the function should return the sum 10 and the maximum number 4.

def sum_and_max(nums: list[int]) -> Tuple[int, int] | None:
#   if nums:
#     print(f"my input: {nums}")
#     sum = sum_it(nums)
#     max = nums[0]
#     for i in nums:
#         if i > max:
#             max = i
#     return (sum, max)
#   return None

    if nums:
        sum = 0
        max = nums[0]
        for i in nums:
            sum += i
            if i > max:
                max = i
        return (sum, max)
    return None

# Prompt: Write a function that takes a list and a target number, and returns the count of occurrences of the target number in the list. For instance, in the list [1, 2, 3, 2, 2, 4] and target number 2, the function should return 3.

def count_occurences(nums: list[int], target: int) -> int | None:
   if nums:
    count = 0
    for i in nums:
        if i == target:
          count += 1
    return count   
   return None


# Prompt: Write a Python function to reverse a given string. For example, if the input string is “hello”, the output should be “olleh”.

def reverse_string(val: str) -> str:
#    return val[::-1]
    temp = []
    for char in val:
        temp.append(char)
    
    result = []
    for char in range(len(temp)):
        result.append(temp.pop())

    return "".join(result)

"""
Python interview questions (and answers) from basic to senior level

https://codesignal.com/blog/interview-prep/key-python-interview-questions-and-answers-from-basic-to-senior-level/

"""

from typing import Tuple

# Prompt: Write a Python function that takes a list of numbers and returns the sum of all elements in the list. For example, for the list [1, 2, 3, 4], the function should return 10.


def sum_it(nums: list[int]) -> int | None:
    if nums:
        sum = 0
        for i in nums:
            sum += i
        return sum
    return None

# Prompt: Build on your previous function to return the largest number in the list, in addition to the sum. For the list [1, 2, 3, 4], the function should return the sum 10 and the maximum number 4.

def sum_and_max(nums: list[int]) -> Tuple[int, int] | None:
#   if nums:
#     print(f"my input: {nums}")
#     sum = sum_it(nums)
#     max = nums[0]
#     for i in nums:
#         if i > max:
#             max = i
#     return (sum, max)
#   return None

    if nums:
        sum = 0
        max = nums[0]
        for i in nums:
            sum += i
            if i > max:
                max = i
        return (sum, max)
    return None

# Prompt: Write a function that takes a list and a target number, and returns the count of occurrences of the target number in the list. For instance, in the list [1, 2, 3, 2, 2, 4] and target number 2, the function should return 3.

def count_occurences(nums: list[int], target: int) -> int | None:
   if nums:
    count = 0
    for i in nums:
        if i == target:
          count += 1
    return count   
   return None


# Prompt: Write a Python function to reverse a given string. For example, if the input string is “hello”, the output should be “olleh”.

def reverse_string(val: str) -> str:
#    return val[::-1]

    # temp = []
    # for char in val:
    #     temp.append(char)
    
    # result = []
    # for char in range(len(temp)):
    #     result.append(temp.pop())

    # return "".join(result)

    result = []
    val = list(val)
    for _ in range(len(val)):
        result.append(val.pop())

    return "".join(result)