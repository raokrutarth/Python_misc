#Krutarth Rao

def SubstitutePairs(string, pairList):
    newstring = ''
    for i in range(len(string)):        
        if(string[i] == pairList[0][0]):            
            newstring = newstring + pairList[0][1]
        elif (string[i] == pairList[1][0]):
            newstring = newstring + pairList[1][1]
        else:
            newstring = newstring + string[i]
    print('Output: ', newstring)           
def main():
    st = input('Enter string: ')
    testlist = [['P', '$'], [ 'o' , '*']]
    SubstitutePairs(st, testlist)
    
main()
            
            
            
    
