# First solution.
def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    result: list[float | int] = signature.copy()
    for _ in range(n - len(signature)):
        number = sum(signature)
        result.append(number)
        # Add the newly calculated number to the signature
        # and remove the first element.
        signature.append(number)
        signature.pop(0)
    return result

print(tribonacci([1, 1, 1], 8))

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]

# The signature contains the first three numbers,
# which are used to calculate the fourth one.

# We need to calculate the remaining numbers
# based on the current signature.

# Add the newly generated number to the signature
# and remove the first element: [1, 1, 3]

# Essentially, the signature acts as a sliding window
# containing the last three numbers used to generate
# the next value in the sequence.

# Second solution. Without sliding window.
def tribonacci(signature, n):
    result = signature[:n]
    for _ in range(n - len(signature)):
        result.append(sum(result[-3:]))
    return result

print(tribonacci([1, 1, 1], 8))
# In this solution, the user uses the last 3 numbers from the array to calculate the next number in the sequence.
# Edge cases are built into the solution without being explicitly specified.
# If n <= 3, the loop will not execute and the function will return the appropriate slice of the signature.
