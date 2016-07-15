#Krutarth Rao

def SumOfDigits(num):
    num_str = str(num)
    num_length = len(num_str)
    total = 0
    for i in range(num_length):
        total = total + eval(num_str[i])
    return total

def main():
    number = input('value = ')
    print( 'output: ',SumOfDigits(number))
main()
    
        
        
