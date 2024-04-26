###
### http://anh.cs.luc.edu/handsonPythonTutorial/index.html
###

###
### http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
###

from graphics import *
import random

### Instantiate Graphics Window
win = GraphWin('my window', 1000, 1000)
win.setBackground('black')
message = Text(Point(win.getWidth()/1.5, 350), 'HELLO CLASS')
message.setFace('times roman')
message.setTextColor('white')
message.setStyle('bold')
message.setSize(20)
message.draw(win)

#Start your nested loops here
for x in range(10):

    for y in range(15):

        ### First pick a center point for the circle
        pt = Point(30 + 100 * x/2, y * 60)

        # Set the color
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, b)
        cir = Circle(pt, 15)
        cir.setFill(color)
        cir.setOutline('white')
        cir.setWidth(4)

        # Then render
        cir.draw(win)







### end your loop here

# Wait for a mouse click to close the Graphics window
win.getMouse()
message.setText('CLICK ANYWHERE TO QUIT.')
message.move(70, 300)
message.setStyle('bold italic')
aColor = color_rgb(90, 0, 250)
message.setFill(aColor)
win.getMouse()



# Failed code:
#    p1 = win.getMouse()
#    p1.draw(win)
#    p2 = win.getMouse()
#    p2.draw(win)
#    p3 = win.getMouse()
#    p3.draw(win)
#    vertices = [p1, p2, p3]
#for x in range(10):

#    for y in range(15):
#       r = random.randrange(256)
#       b = random.randrange(256)
#       g = random.randrange(256)
#       triangle = Polygon(vertices)
#       color = color_rgb(r, g, b)
#       triangle.setFill(color)
#       triangle.setOutline(color)
#       triangle.setWidth(2)
#       triangle.draw(win)