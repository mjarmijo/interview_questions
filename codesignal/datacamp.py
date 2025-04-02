
"""
The 36 Top Python Interview Questions & Answers For 2025

https://www.datacamp.com/blog/top-python-interview-questions-and-answers

https://www.jointaro.com/interview-insights/google/coin-change-ii/

https://www.jointaro.com/interview-insights/amazon/robot-return-to-origin/


"""

"""
23. How can you replace string space with a given character in Python?
Example 1: A user has provided the string l vey u and the character o, and the output will be loveyou.
Example 2: A user has provided the string D t C mpBl ckFrid yS le and the character a, and the output will be DataCampBlackFridaySale.
"""

def string_replace(text: str, val: str=" ", replacement_val: str=" ") -> str:
    # 1.   
    # result = list(input)
    # for i, char in enumerate(result):
    #     print(i, char)
    #     if char == val:
    #         result[i] = replacement_val
    # return "".join(result)

    # 2.
    # return input.replace(val, replacement_val)

    # 3. 
    result = ""
    for char in text:
        if char == val:
            char = replacement_val
        result += char
    return result

"""
24. Given a positive integer num, write a function that returns True if num is a perfect square else False.

num = 36
result = True

num = 10
result = false
"""

def perfect_square(val: int) -> bool:
    if val > 0:
        result = int(val**(1/2))
        return result ** 2 == val
    return False

""" 
25. Given an integer n, return the number of trailing zeroes in n factorial n!

val = 7
result = 1 #
"""
def trailing_zeros(val: int) -> int:
  result=val
  for i in range(val-1, 0,-1):
     result*=i
  
  count = 0
  for num in str(result)[::-1]:
    print(num)
    if num == "0":
        count+=1
    else:
        break

  return result, count

## start here

# def coin_change(denominations, amount):
#     """https://www.datacamp.com/blog/top-python-interview-questions-and-answers

#        https://www.jointaro.com/interview-insights/google/coin-change-ii/"""
#     solution = [0] * (amount)
#     solution[0] = 1
#     for den in denominations:
#         for i in range(den, len(solution)):
#             print(f"i: {i}, den: {den} ")
#             print(f"before: {solution}")
#             solution[i] += solution[i-den]
#             print(f"after: {solution}")
#     return solution[len(solution) - 1]
    