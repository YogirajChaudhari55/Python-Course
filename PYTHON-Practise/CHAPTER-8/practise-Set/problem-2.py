#Program using function to convert Celsius to Fahrenheit
# Formula c = 5 * (f-32)/9


f= int(input("Enter temperature in F: "))


def CtoF(f):
    c = 5 * (f-32)/9
    print(c)

CtoF(f)