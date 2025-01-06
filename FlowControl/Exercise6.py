def caps_long(string):
    return (string.upper() if len(string) > 10 else string)

print(caps_long("Sue Smith"))
print(caps_long("Sue Roberts"))
print(caps_long("Joe Shea"))
print(caps_long("Joe Stevens"))