import math
def main():
    pounds = eval(input("what is the weight in pounds? "))
    hecto = (pounds * 453.59237) / 100
    print(pounds," ", "pound(s) is " , round(hecto, 2), "hectograms")

main()

