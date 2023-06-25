def slice_it(arr):
    result = ''
    for word in arr:
        x = word[0:2]
        result += ''.join(x)
    print(result)