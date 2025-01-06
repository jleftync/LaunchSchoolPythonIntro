vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]
#y = [c for c in vocabulary]
#x =  [a for a in y]
#print(x)
#for synonyms in vocabulary:
   #for word in synonyms:
       #print(word)

all_words = sum(vocabulary, [])

for word in all_words:
    print(word)