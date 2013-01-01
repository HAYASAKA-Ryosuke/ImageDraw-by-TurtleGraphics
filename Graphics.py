#! /usr/local/bin/python
#-*-coding:utf-8-*-
import Image
import ImageFilter
import turtle
#This function draw loaded image using TurtleGraphics
def TurtlePainting(Image,filtervalue):
    pix=Image.load()
    #turtle.speed(0)
    turtle.tracer(0)
    turtle.penup()
    width=Image.size[0]
    height=Image.size[1]
    turtle.setup(width,height+30,-turtle.window_width(),-turtle.window_height())
    for i in range(height):
        for j in range(width):
            if pix[j,i][0]<=filtervalue:
                turtle.setpos(j-turtle.window_width()/2,-i+turtle.window_height()/2-10)
                turtle.dot(8)

image=Image.open('./pythonLogo.png')

image_filtering=image.filter(ImageFilter.CONTOUR)
TurtlePainting(image_filtering,100)
turtle.exitonclick()
