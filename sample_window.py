from graphics import *
import time


def main():
    win = GraphWin("Lab04", 400, 400)
    win.setCoords(0.0,0.0,400.0,400.0)

    

    circle_red = Circle( Point(100, 50) , 40)
    circle_red.setFill('red')
    circle_red.draw(win)

    square_blue = Rectangle( Point(300,300) , Point(350,350))
    square_blue.setFill('blue')
    square_blue.draw(win)

    while (circle_red.getCenter().getX() < 400 or square_blue.getCenter().getX() > 0):
        circle_red.move(10 , 0)
        square_blue.move(-10 , 0)
        time.sleep(0.02)
        
        
        
        
    


    
    win.getMouse()
    win.close()

main()
    
    
