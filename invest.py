##Krutarth Rao
def DoubleChecker():
    percent = eval(input('Annual interest (%): '))
    invest_amt = 1
    total = 1
    years_counter = 0
    
    while total < (invest_amt*2):
        total += (total*(percent/100))
        years_counter +=1
        
    return years_counter
def main():
    print('Determine how long it takes for an investment to double...')
    answer = 'yes'
    
    while answer == 'yes':
        print('It takes ', DoubleChecker(), 'years for the investment to double.')        
        answer = input('Do you want to continue (yes/no)?')
        
main()
        
  ##Krutarth Rao      
