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


    # result = []
    # val = list(val)
    # for _ in range(len(val)):
    #     result.append(val.pop())

    # return "".join(result)

    temp = []
    for char in val:
        temp.append(char)

    result = []
    for _ in range(len(temp)):
        result.append(temp.pop())

    return "".join(result)


def is_palindrome(val: str) -> bool:
    # return val == val[::-1]

    if val != "":  # if string is not empty
        temp = []
        for char in val:  # for each char in val, append to temp
            temp.append(char)
        
        rev_val = []
        for _ in range(len(temp)):  # for the items in temp, pop the last item and append to rev_temp  --> reverses the order
            rev_val.append(temp.pop())
        if "".join(rev_val) == "".join(val):  # join into a string and compare to original value, return true
            return True

    return False

def has_palindrome_substring(val: str) -> int:
    count = 0
    if val ==  "":
        return count
    # temp = []
    # for char in val:
    #     temp.append(char)
    # print(f"val: {val}, length: {len(val)}")
    # for i in range(len(val)):
    #     for j in range(i, len(val)):
    #       print(f"i:{i}, j:{j}")
    #       print(f"{val[i:j+1]}", is_palindrome(val[i:j+1]))
    #       if is_palindrome(val[i:j+1]):
    #           count += 1
    # return count
    # count = 0
    for i in range(len(val)):
        for j in range(i, len(val)):
            if val[i:j+1] == val[i:j+1][::-1]:
                count += 1
    return count
