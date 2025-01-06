def extract_language(a):
    #return a[:2]
    return a.split('_')[0]


print(extract_language('en_US.UTF-8'))      # en