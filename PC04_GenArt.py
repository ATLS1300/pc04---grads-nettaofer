#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 12:32:14 2021

@author: nettaofer

I created a script that generate 2 shapes - one small (violet, smallShape) 
which has a random # of sides from 3 to 10, and a large shape(fuchsia, 
largeShape) which has double the amount of sides than the small shape.
I based the original triangle shape I experiemented with from Kevin Ecke's 
pseudocode (lines 29-45).

"""

import turtle, random

panel = turtle.Screen().bgcolor('black')
turtle.speed(3) 
turtle.up() 
turtle.goto(0,0)


smallShape = turtle.Turtle()
largeShape = turtle.Turtle()

smallShape.color('violet')
largeShape.color('fuchsia')

### classmate's code ###
"""
Set triangle lengths
Set triangle angles
For loop to make triangles(8):
For loop to make individual triangle(3):
Turtle forward(length)
Turtle right(angle)
Turtle right (180-angle)
Turtle forward(length)
Turtle left (angle)
"""

sideLength = 30
sides = 3           # will change to: random.randint(3, 9)
angle = 120         #was not in use
### classmate's code ###

sides = random.randint(3, 10)   # this is the random code - the small shape will have a random (from 3-10) # of sides


for iteration in range(sides):  # draws the small shape with a random # of sides (range 3-10)
    smallShape.down()
    smallShape.forward(sideLength)
    smallShape.right(360/sides)
    print(sides)
    smallShape.up()
    
largeShape.up()
largeShape.goto(0,sides*10)


for iteration in range(2*sides): # draws the large shape with double the amount of sides of the smaller shape
    largeShape.down()
    largeShape.forward(2*sideLength)
    largeShape.right(360/(2*sides))
    print(2*sides)


turtle.done()