def multires(x, y):
    return float(x) * float(y)

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first nunber: ')
second_number = get_number('Enter the second number:')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')




#a = input("Enter the first number: ")
#b = input("Enter the second number: ")
#c = multires(a, b)
#print(a + " * " + b + " = " + str(c))