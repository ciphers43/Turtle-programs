#Python programming to draw octagon in turtle programming
import turtle
 
t = turtle.Turtle()
for i in range(8):
   t.forward(100) #Assuming the side of a octagon is 100 units
   t.right(45) #Turning the turtle by 45 degree
