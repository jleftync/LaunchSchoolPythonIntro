def is_empty_orblank(s):
    if s == '':
        return not s
    elif s.strip() == '':
        return not s
    else:
        return True
    
#def is_empty_or_blank(s):
    #return not s.strip(' ')
#def is_empty_or_blank(str):
#   return not str or str.isspace()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))    