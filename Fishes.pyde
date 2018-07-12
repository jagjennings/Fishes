def setup():
    global xCoordinate, yCoordinate, rectLength, red, green, xCoordinate2, yCoordinate2, xCoordinate3, yCoordinate3
    size(400, 400)
    red = 152
    green = 245
    background(152,245,255)
    rectLength = 399
    noStroke()
    while rectLength > 0:
        red -= .4
        green -= .4
        fill(red, green, 255)
        rect(0, 400-rectLength, 400, rectLength)
        rectLength -=.5
    #fish(225, 145, 176, 70, 120, 350)
    #fish(25, 145, 176, 20, 230, 50)
    #fish(225, 45, 176, 50, 43, 25)
    #fish(225, 145, 76, 40, 300, 290)
    #fish(22, 15, 176, 60, 200, 150)
    #fish(22, 215, 16, 90, 60, 230)
    xCoordinate = 280
    yCoordinate = 155
    xCoordinate2 = 405
    yCoordinate2 = 270
    xCoordinate3 = 305
    yCoordinate3 = 70
    
def fish(r, g, b, size, x, y):
    noStroke()
    fill(r, g, b)
    ellipse(x, y, size, size/2)
    triangle(x+(size/3), y, x+(size/1.5), y-(size/4), x+(size/1.5), y+(size/4))
    fill(0, 0, 0)
    ellipse(x-(size/3), y-(size/10), size/20, size/20)
    
def draw():
    global xCoordinate, yCoordinate, rectLength, red, green, xCoordinate2, yCoordinate2, xCoordinate3, yCoordinate3
    rectLength = 399
    red = 152
    green = 245
    while rectLength > 0:
        red -= .4
        green -= .4
        fill(red, green, 255)
        rect(0, 400-rectLength, 400, rectLength)
        rectLength -=.5
    fish(0, 255, 0, 60, xCoordinate, yCoordinate)
    xCoordinate -= .5
    yCoordinate += .3
    fish(255, 182, 194, 40, xCoordinate2, yCoordinate2)
    xCoordinate2 -= 1
    yCoordinate2 -= .2
    fish(255 , 236, 140, 50, xCoordinate3, yCoordinate3)
    xCoordinate3 -= .75
    yCoordinate3 += .15
