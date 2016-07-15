## Krutarth Rao

def ispalindrome():
    word = input('Please enter a word to test for a palindrome: ')
    for i in range(int(len(word) / 2)):
        
        if word[i] != word[(-1*i)-1]:
            print (word, " is NOT a palindrome!")
            return
    
    print(word, " is a palindrome!")          


    
        

ispalindrome()
            
            
