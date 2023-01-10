cars = [ 
        'safari', 
        'creta',
        'polo',
        'm3',
        'supra',
        'gls',
        'tavera',
        'x1',
        'glc',
        'fortuner',
        'thar',
        'octavia',
        'swift',
        'ambassador',
        'alto',
        'nexon',
        'xuv'
        ]

my_car = input("Please enter car name :")

def lookup(s, l):
    availability = "Car is not available"
    for car in l:
        # print(car)
        if (car==s):
            availability = "Car is available"
            return availability
        else:
            availability = "Car is not available"

    return availability


print(lookup(my_car, cars))







