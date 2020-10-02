# Yichen Zhou
# CS 20
# Description: custom cursor
# Date: 02/10/2020


def Circles(a, b, x):
    """draw 3 circles
    a,b is centre of the first
    x is radius of the first"""
    fill(200)
    circle(a, b, 2*x)
    fill(mouseX, mouseY, (mouseX+mouseY)/2)
    circle(a+x/2, b, x)
    fill(mouseX/2, mouseY/2, mouseX/(mouseY+1)*100)
    circle(a+x/4, b, x/4)


def setup():
    size(399, 399)
    background(0)


def draw():
    clear()
    if mouseX < 200:
        if mouseY < 200:
            Circles(mouseX+50, mouseY+50, 50)
        else:
            Circles(mouseX+50, mouseY-50, 50)
    else:
        if mouseY < 200:
            Circles(mouseX-50, mouseY+50, 50)
        else:
            Circles(mouseX-50, mouseY-50, 50)
