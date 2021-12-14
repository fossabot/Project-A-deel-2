import cursorPos as cP

scherm = 1

color1 = "#E535E5"
color2 = "#FF0000"
color3 = "#0000FF"
color4 = "#00FF00"
color5 = "#FF00B7"
color6 = "#FF9100"
text_color = 255
line_color = 255

titel = 'Instellingen'
back = "Hoofdmenu"
spelMenu = "Speel menu"
zwart_wit = "Zwart-Wit achtergrond"
achtergrond = "Achtergronden"
kleurenkiezer = "Kleuren"

bright = 127.5

height= 720
width = 1280
x = width/2

def scherm0():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()

def scherm1():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm2():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()

def scherm0():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()    
            
def scherm3():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm4():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm5():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm6():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm7():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm8():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm9():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm10():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm11():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm12():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm13():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm14():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm15():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    
def scherm16():
    global img1, img2, img3, img4, img5, img6
    img1 = loadImage("macock1.jpeg")
    img2 = loadImage("ricardo.jpeg")
    img3 = loadImage("minecraft.JPEG")
    img4 = loadImage("coolbg.jpeg")
    img5 = loadImage("bg1.jpeg")
    img6 = loadImage("bglight.jpeg")
    font = createFont("fortnite.otf", 30, True)
    textFont(font)
    imageMode(CORNER)
    image(img1, width/64, height/9.5, 75, 75)
    image(img2, width/10, height/9.5, 75, 75)
    image(img3, width/64, height/4, 75, 75)
    image(img4, width/10, height/4, 75, 75)
    image(img5, width/64, height/2.55, 75, 75)
    image(img6, width/10, height/2.55, 75, 75)
    noStroke()
    fill(text_color)
    textAlign(LEFT)
    text(back, width/64, 24)
    text(achtergrond, width/64, height/11)
    textAlign(RIGHT)
    text(spelMenu, width/1.01, 24)
    text(kleurenkiezer, width/1.01, height/11)
    textAlign(CENTER)
    text(zwart_wit, width/2, height/11)
    textAlign(CENTER)
    textSize(33)
    text(titel, width/2 , 26)
    
    stroke(0)
    fill(color1)
    rect(1180, 75, 90, 25)
    fill(color2)
    rect(1180, 110, 90, 25)
    fill(color3)
    rect(1180, 145, 90, 25)
    fill(color4)
    rect(1180, 180, 90, 25)
    fill(color5)
    rect(1180, 215, 90, 25)
    fill(color6)
    rect(1180, 250, 90, 25)
    
    stroke(0)
    fill(bright)
    rect(width/2.24, height/8, 150, 25, 3)
    
    fill(bright/2)
    rect(width/2.24, height/6, 150, 25, 3)
    
    fill(bright*1.5)
    rect(width/2.24, height/4.8, 150, 25, 3)
    
    fill(255)
    rect(width/2.24, height/4, 150, 25, 3)
    
    stroke(line_color)
    line(0, 35, width, 35)
    
    noLoop()
    cP.mouseCursor()
    loop()
    

    