# My answer. It is solution used standart algorithm with multiplycation by 2 and addition of next number. 
def binary_array_to_number(arr):
    total = arr[0]
    for num in range(len(arr) - 1):
            total = total * 2 + (arr[num + 1])
    return total

binary_array_to_number([0, 0, 0, 1])
binary_array_to_number([1, 0, 1, 1])


# But there is also solution with using of built-in function int() with base 2, which is more elegant and faster.
# This solution is obtained from a comment to the exercise

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

# In this solution uses to the map() function to convert the array elements to a str and 
# then combine them into a string using ''.join()
# The int() function interprets the resulting string into a number in binary notation.
