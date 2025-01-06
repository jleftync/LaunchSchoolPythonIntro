def extract_language(a):
    #return a[3:5]
    #return a.split('_')[0][0:2]
    return a.split('.')[0].split('_')[1]


print(extract_language('en_US.UTF-8'))      # en