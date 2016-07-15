#Krutarth Rao
def notsohatchi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        return notsohatchi(n-1) + notsohatchi(n-3)
 
 
def main():
    print("We are going to find the nth number in the Notsohatchi Series")
    n = eval(input("n? "))
    print(notsohatchi(n-2), notsohatchi(n-1), notsohatchi(n))
 
 
main()
