def greet(a):
    match a:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af': 
            return 'Haai!'
        
def local_greet(d):
    match d:
        case 'US':
            return 'Hey!'
        case 'GB':
            return 'Hello!'
        case 'AU':
            return 'Gday!'
        #case _:
            #return greet(language)

def extract_language(b):
    return b.split('_')[0]

def extract_region(c):
    return c.split('.')[0].split('_')[1]

def locale_greet(a):
    x = extract_language(a)
    if x == "en":
         y = extract_region(a)
         z = local_greet(y)
         return z
    else:
        y = greet(x)
        return y

print(locale_greet('en_US.UTF-8'))       # Hey!
print(locale_greet('en_GB.UTF-8'))       # Hello!
print(locale_greet('en_AU.UTF-8'))       # Howdy!
print(locale_greet('fr_FR.UTF-8'))       # Salut!
print(locale_greet('fr_CA.UTF-8'))       # Salut!
print(locale_greet('fr_MA.UTF-8'))    

    




