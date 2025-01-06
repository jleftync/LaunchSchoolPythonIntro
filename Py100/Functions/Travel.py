destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora', 
                'Barcelona', 'Rio de Janeiro', 'Marrakesh', 'New York City']

def contains(a, b):
    if a in b:
        print(True)
    else:
        print(False)
    
    #print(False)
    
        
    

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False