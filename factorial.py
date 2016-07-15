## Krutarth Rao
def factorial(num):
    factorial_num = 1
    
    for i in range(1, num+1):        
        factorial_num = factorial_num * i
    return factorial_num

    

def main():
    number = eval(input('Please enter a number: '))
    result_factorial = factorial(number)
    print("the factorial of ", number, "is: ", result_factorial)
## Krutarth Rao
main()
