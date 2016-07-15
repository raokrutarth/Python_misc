#Krutarth Rao

def count(filename):
    file = open(filename,'r')
    file_lines = file.read()
    linesList = file_lines.split('\n')
    result = {}
    for word in linesList:
        wordcount = linesList.count(word)
        single_entry = {word : wordcount}
        result[word] = wordcount
    
    return result


def MaxWord(dict_inp):

   n = max(dict_inp.values())
   maxRepWord = ''
   for k in dict_inp:
       if dict_inp[k] == n:
           maxRepWord = k

   return maxRepWord, n

def main():

    filename = input('Please enter the filename: ')
    wordCounts = count(filename)
    word , number = MaxWord(wordCounts)
    print('The word that is repeated the most number of times is:', word, ' and is repeated ',number,' times.')

main()
