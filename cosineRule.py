import math

def main(): 
    a = eval(input("Enter length of side a: "))
    b = eval(input("Enter length of side b: "))
    c = eval(input("Enter length of side c: "))

    print ("Value of a =", a)
    print ("Value of b =", b)
    print ("Value of c =", c)

    a_angle = math.acos((math.pow(c,2) + math.pow(b,2) - math.pow(a,2))/(2*c*b))
    b_angle = math.acos((math.pow(a,2) + math.pow(c,2) - math.pow(b,2))/(2*a*c))
    c_angle = math.acos((math.pow(a,2) + math.pow(b,2) - math.pow(c,2))/(2*a*b))
 

    print("The angle between a and b is: ", round(math.degrees(c_angle),2), "degrees")
    print("The angle between b and c is: ", round(math.degrees(a_angle),2), "degrees")
    print("The angle between c and a is: ", round(math.degrees(b_angle),2), "degrees")
    
main()
    
    
