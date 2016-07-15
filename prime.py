#Krutarth Rao

def primeExtracter(num):
    listn = list(range(2, num+1))
    
    for i in range(2, num):
        for number in listn:
            if number%i == 0 and number != i:
                listn.remove(number)
    return listn



def main():
    n = eval(input('Please enter a number: '))
    result = primeExtracter(n)
    print('The prime numbers from 1 to ', n, ' are: \n', result)


main()
    
