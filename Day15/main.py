from turtle import Turtle, Screen
# from module import class

objectName = Turtle()
print(objectName)
objectName.shape("turtle")
objectName.fillcolor("red") # turtle color
objectName.pencolor("green") # turtle path color

objectName.forward(100) # 100 = steps

objectName.left(90) # 90 = degrees
objectName.forward(100)

objectName.left(90)
objectName.forward(100)

objectName.left(90)
objectName.forward(100)

myScreen = Screen()
print(myScreen.canvheight)

myScreen.exitonclick()