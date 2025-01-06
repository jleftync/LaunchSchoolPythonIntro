def find_maximum(numbers):
    if not numbers:
        return None
    max_number = 0
    #max_number = numbers[0]  Most pythonic Solution
    #max_number = float('-inf')  also interesting
    for number in numbers:
        if number > max_number or numbers.index(number) == 0:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))  