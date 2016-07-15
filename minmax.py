def helperMinMax (x, y) :
    if x < y :
        return x, y, 1 #the third value means one comparison was performed
    else :
        return y, x, 2 #the third value means two comparison were performed
 
def fastMinMax (inputList) :
    totalComparisons = 0
 
    if (len(inputList) % 2 == 0) :
        i = 2
        minVal, maxVal, c1 = helperMinMax(inputList[0], inputList[1])
    else :
        i = 1
        minVal, maxVal, c1 = helperMinMax(inputList[0], inputList[0])
 
    while i < len(inputList) :
 
        mini, maxi, c1 = helperMinMax(inputList[i], inputList[i+1])
        totalComparisons = totalComparisons + c1
 
        if mini < minVal :
            minVal = mini
            totalComparisons = totalComparisons + 1
 
        if maxi > maxVal :
            maxVal = maxi
            totalComparisons = totalComparisons + 1
 
        i = i + 2
 
 
    return minVal, maxVal,totalComparisons


inputList = [2,1,4,-1,5,7]
list1 = [1,20,2,3,4,5,6,8,9,10,11,12]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
list3 = [12,11,10,9,8,7,6,5,4,3,2,1]
list_l = [1,0,0,0,0,0,0,0,0,0,0,12]
minimum, maximum, count = fastMinMax(list_l)
print('min: ', minimum,'max: ', maximum,'comp: ', count)
