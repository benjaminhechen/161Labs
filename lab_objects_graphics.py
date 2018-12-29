from graphics import GraphWin, Rectangle, Polygon, Point

def main():
    win = GraphWin();    
    click1 = win.getMouse()
    click1.draw(win)
    click2 = win.getMouse()
    click2.draw(win)
    
    walls = Rectangle(click1, click2)
    walls.draw(win)
    
    fifthOfFloor = abs(click1.getX()-click2.getX())/5
    print(fifthOfFloor)
    
    click3 = win.getMouse()
    click3.draw(win)
    
    doorFrameTopLeft = Point(click3.getX()-fifthOfFloor/2, click3.getY())
    doorFrameTopRight = Point(click3.getX()+fifthOfFloor/2, click3.getY())
    doorFrameTopLeft.draw(win)
    doorFrameTopRight.draw(win)
    
    doorFrameBottomLeft = Point(click3.getX()-fifthOfFloor/2, click1.getY())
    doorFrameBottomRight = Point(click3.getX()+fifthOfFloor/2, click1.getY())
    
    door = Polygon(doorFrameTopLeft, doorFrameTopRight, doorFrameBottomRight, doorFrameBottomLeft)
    door.draw(win)
    
    
    click4 = win.getMouse()
    
    windowSide = 3*fifthOfFloor/4
    windowZ = windowSide/2
    
    windowCenterX = click4.getX()
    windowCenterY = click4.getY()
    
    windowTopLeft = Point(windowCenterX-windowZ, windowCenterY-windowZ)
    windowBottomRight = Point(windowCenterX+windowZ, windowCenterY+windowZ)
    
    window = Rectangle(windowTopLeft, windowBottomRight)
    window.draw(win)
    
    click5 = win.getMouse()
    click5.draw(win)
    
    leftCeilingX = click1.getX()
    leftCeilingY = click2.getY()
    
    leftCeilingPoint = Point(leftCeilingX, leftCeilingY)
    
    roof = Polygon(click2, leftCeilingPoint, click5)
    roof.draw(win)
    
main()
