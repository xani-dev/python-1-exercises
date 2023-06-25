def word_histogram(sentence):
    counter = dict()
    words = sentence.split()
    print(words)
    
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    
    print(counter)


