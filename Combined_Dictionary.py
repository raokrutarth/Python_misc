#Krutarth Rao

def combiner(dict1, dict2):

    dict3 = {}

    for v in dict1:
        if v in dict2 and v in dict2:
            dict3[v] = dict1[v] + dict2[v]
        else:
            dict3[v] = dict1[v]

    for k in dict2:
        if (k in dict3) == False:
            dict3[k] = dict2[k]
    return dict3


def main():

    dictA = {'a':1, 'b':4, 'c':9}
    dictB = {'b':3, 'c':1, 'd':5}
    combined_dict = combiner(dictA, dictB)
    print('Dictionary A = ',dictA)
    print('Dictionary B = ', dictB)
    print('The combined dictionary is: \n', combined_dict)

main()

    
    
