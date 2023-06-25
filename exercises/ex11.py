def diagonal_printer(text):
    words = text.split()
    for word in words:
        for i in range(len(word)):
            print(' '*i, word[i])
    