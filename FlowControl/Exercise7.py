def number_range(number):
    return ('the value is between 0 and 50 (inclusive)' if (number >= 0 and number <= 50) else 'the value is between 51 and 100 (inclusive)' if (number >= 51 and number <= 100) else 'the value is greater than 100' if (number >= 101) else 'the value is less than 0')
print(number_range(0))