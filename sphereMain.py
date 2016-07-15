#Krutarth Rao

from sphere import *

def main():

    user_rad = eval(input('Please enter radius: '))
    s = Sphere(user_rad)
    print('sphere s radius = ',s.getRadius())
    print('surface area = ',s.surfaceArea())
    print('volume = ', s.volume())

main()
