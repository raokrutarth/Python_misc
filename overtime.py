def wageCalc(hours, rate):
    if hours <= 40:
        pay = hours * float(rate)
        return pay
    elif hours >40:
        basePay = 40 * float(rate)
        overtime = (hours-40) * float(rate*1.5)
        pay = basePay + overtime
        return pay
def main():
    hours = eval(input('Number of hours worked during the week: '))
    rate = eval(input('Dls. per hour: '))
    payment = wageCalc(hours, rate)
    print('Payment: ', payment)
main()

    
  ##Krutarth Rao##Krutarth Rao      
