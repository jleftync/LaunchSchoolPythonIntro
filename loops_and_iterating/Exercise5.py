my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    if number % 2 == 0:
        print(number)


x = 0 

while len(my_list) >= x:
    if solution[x] % 2 == 1:
        solution = my_list[x]
        print(solution)
    
    
    x +=