def SubSequence(mySequence):    
## KRUTARTH RAO
    ms_length = len(mySequence)
    result = ""
    if (ms_length >= 8):
        prefix = mySequence[:3]
        suffix = mySequence[-3:]    
        result = prefix + suffix
        a_counter = 0
        c_counter = 0

        for i in range(ms_length):
            if mySequence[i] == "A":
                a_counter = a_counter + 1
            elif mySequence[i] == "C":
                c_counter = c_counter + 1
    else:
        print("The length of the input sequence must be greater or equal to 8")
        result = 'X'
        c_counter = 0
        a_counter = 0
    return result, a_counter, c_counter

def main():
    input_str = input("Enter a string: ")
    str_r, a , b = SubSequence(input_str)

    print( "(",str_r , ",", a ,",", b, ")")

main()
            

    
