import math


def geometricSum(a, r, n):
    g_sum = 0
    i_term= 0
    for i in range(1, n+1):
        i_term = a * math.pow(r,(i-1))
        print("Term ",i, "=", i_term)        
        g_sum = g_sum + i_term 

    return g_sum

def main():
    print("Calculate the sum of geometric series")

    a = eval(input("a? "))
    r = eval(input("r? "))
    n = eval(input("n? "))

    final_g_sum = geometricSum(a, r, n)

    print("sum = ", (int)(final_g_sum))


main()
   


    
        
    
