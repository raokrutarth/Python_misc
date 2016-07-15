def leapYear(year):
    if (year%400 == 0):
        print('Year: ', year,'\nLeap year')
    if (year%4 == 0) and (year%100 != 0):
        print( 'Year: ', year, '\nLeap year')
    elif (year%400 != 0) or (year%4 != 0) :
              print('Year: ', year, '\nNOT a leap year.')
def main():
              year = eval(input('Please enter year: '))
              leapYear(year)
main()
 ##Krutarth Rao##Krutarth Rao             
        
    
