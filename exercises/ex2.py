# Create a Python function named `array_to_string` that accepts an array of `ints` and returns a string.
# The function must use a for loop and must cast the `ints` to `strings`.

def arr_to_str(s):
    listToStr = ''.join([str(elem) for elem in s])
    print(listToStr)