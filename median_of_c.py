## Krutarth Rao

def main():

    c_file = open('c.txt' , 'r')
    c_list = c_file.readlines()
    for i in range(len(c_list)):
        c_list[i] = int(c_list[i])
        
    c_list.sort()
    

    median = (c_list[49] + c_list[50]) / 2

    print("Median is: {0:0.1f}".format(median))

main()
