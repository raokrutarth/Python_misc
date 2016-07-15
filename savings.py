def main():
    initialamount = eval(input("Initial Deposit in Dollars? " ));
    three_monthly_interest = eval(input("Three-monthly interest (in Percentage)?" ));
    months = eval(input("Number of months " ));

    balance = initialamount
    print("Month:  0", "amount: ",initialamount)
    

    for i in range(1 , months+1):
        if( i%3 == 0):
            balance = balance - 30;
            balance = balance + (balance * (three_monthly_interest/100));            
            print("Month: ", i,"amount: $", round(balance,2)); 
        else:            
            balance = balance - 30;
            print("Month: ", i,"amount: $", round(balance,2));

main();
            
            
