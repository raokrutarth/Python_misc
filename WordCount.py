##Krutarth Rao

def count(filename):
    my_file = open( filename, "r")
    my_file_list = my_file.read()
    
    c1 = my_file_list.split('\n')
    ##print(c1)
    resultList = []
    

    for w in c1:
        inList = False

        for sub_list in resultList:
            if sub_list[0] == w:
                inList = True
                sub_list[1] += 1
        if inList == False:
            resultList.append([w, 1])
    return resultList
        
def main():

    filename = input("Please enter filename: ")
    print(count(filename))

main()

    
