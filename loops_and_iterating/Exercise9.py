def factorial(inputs):
    results = 1
    while inputs >1:
        results *= inputs
        inputs -= 1
    return results

def factorials(inputz):
    resultz = 1
    for number in range(inputz, 0, -1):
        resultz *= number
    return resultz
