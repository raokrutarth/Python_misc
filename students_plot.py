import matplotlib.pyplot as pyplot

def PlotBarGraph(data_list):
    pos1 = [1, 3.5, 6, 8.5 ]
    pos2 = [2, 4.5, 7, 9.5]
    pos3 = [1.5, 4, 6.5, 9]
    
    data_male = [data_list[0][1], data_list[1][1], data_list[2][1],
                 data_list[3][1] ]
    data_female = [data_list[0][2], data_list[1][2], data_list[2][2],
             data_list[3][2]]
     
    names = [data_list[0][0], data_list[1][0],
             data_list[2][0], data_list[3][0]] 
     
    bar1 = pyplot.bar(pos1, data_male, width=1, color='blue', align='center')
    bar2 = pyplot.bar(pos2, data_female, width=1, color='pink', align='center')
        
    pyplot.legend((bar1, bar2), ('Male Student Number',
                                 'Female Student Number'), loc=2)
    pyplot.xticks(pos3, names)
     
    pyplot.ylabel('Number of Students')
    pyplot.setp(pyplot.xticks()[1], rotation=15)
    pyplot.axis([0, 11, 0, 50])
    pyplot.show()

def main():
    studentslist = [['Play Sports', 27, 20], ['Talk on Phone',18,22], ['Visit Friends', 38, 47],
            ['School Clubs', 17, 11]]
    PlotBarGraph(studentslist)
main()
