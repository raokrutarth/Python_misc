#Krutarth Rao
def powset(seq):
    result = []
    if len(seq) == 0:
        return [[]]
    else:
        result = []
        pw_tail = powset(seq[1:])
        
        for each_set in pw_tail:
            result+=[each_set]
            frst_el = [seq[0]]
            micro_pw_set = frst_el + each_set
            result+=[micro_pw_set]
            
    return result       
       
 
def main():
    a = [1,2,3,4]
    print("a =",a)
    print(powset(a))
 
main()
