def c_to_f(celsius):
    farenheit = round((celsius*9/5)+32)
    print (f'{celsius} degrees Celsius is {farenheit} Farenheit' ) 
    

def f_to_c(farenheit):
    celsius = round((farenheit - 32)*5/9)
    print (f'{farenheit} degrees Farenheit is {celsius} Celsius')
