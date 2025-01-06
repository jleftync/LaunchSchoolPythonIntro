c = 0
d = ''
def starts_with(a,b):
    c = len(b) 
    return b == a[0:c]

#string.startswith(b)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
