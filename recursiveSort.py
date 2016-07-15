
##Krutarth Rao
def sort(list1, sortedlist):
    
    if len(list1)== 0:
        return sortedlist
    else:
        min_v = list1[0]
        for each_val in list1:
            if each_val < min_v:
                min_v = each_val
        list1.remove(min_v)
        sortedlist.append(min_v)
        sort(list1, sortedlist)
        return sortedlist
                
 
def main():
    a = [-1,7,5,32,1,0,-9,6,-8]
    sortedlist = []
    print(sort(a,sortedlist))
 
main() 
