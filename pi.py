import math
# Krutarth Rao
def pi_estimator(n):
    c = 1
    fractions = 0
    for i in range (1, (2*n)+1, 2):
        fractions = fractions + 4/(c*i)
        c = -1*c        
    return fractions

def main():
    print("Program that estimates pi")
    times = eval(input("Number of terms? "))
    estimated_pi = pi_estimator(times)
    print("Approximation of pi = ", round(estimated_pi, 11))

main()



    
        
        
    
