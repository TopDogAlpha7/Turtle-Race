from secrets import choice
from tkinter import Y
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?(Red, Orange, Yellow, Green, Blue, Indigo or Violet) Enter a colour: ").lower()
colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo"]
y_coordinates = [0, 50, 100, -50, -100, -150]
new_turtles = []

for turtle in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colours[turtle])
    t.penup()
    t.goto(x=-755, y=y_coordinates[turtle])
    new_turtles.append(t)

if bet:
    race_on = True

while race_on:
    for turtle in new_turtles:
        if turtle.xcor() > 715:
            race_on = False
            winning = turtle.pencolor()
            if winning == bet:
                print(f"You've won! The {winning} turtle is the winner")
                break
            else:
                print(f"You've lost! The {winning} turtle is the winner")
                break
            
        distance = random.randint(0,10)
        turtle.fd(distance)
    
    












screen.exitonclick()

