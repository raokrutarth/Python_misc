## Krutarth Rao

def main():
    
    file_a = open('a.txt', 'r')
    a_list = file_a.readlines()
    
    file_b = open('b.txt', 'r')
    b_list = file_b.readlines()
    
    c_file = open('c.txt', 'w')
    
    for i in range(100):
        a_plus_b = eval(a_list[i]) + eval(b_list[i])
        c_file.write(str(a_plus_b) + '\n')    

        
    file_a.close()
    file_b.close()
    c_file.close()

    
main()

    

    
