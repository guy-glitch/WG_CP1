#WG Turtle Race 1st
import turtle as t
import random as r
print("The winner will turn green")
screen = t.Screen()
screen.setup(width=1200, height=1100)
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()

t1.teleport(1, 900)
t2.teleport(1, 700)
t3.teleport(1, 500)
t4.teleport(1, 300)
t5.teleport(1, 100)

t1.color("black")
t1.teleport(1000,1000)
t1.right(90)
t1.forward(1000)
t1.left(90)

t1.color("LightSlateBlue")
t2.color("OliveDrab1")
t3.color("OrangeRed")
t4.color("firebrick")
t5.color("MediumTurquoise")

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")

winner = "none"

while winner == "none":
    t1.forward(r.randint(1,200))
    t2.forward(r.randint(1,200))
    t3.forward(r.randint(1,200))
    t4.forward(r.randint(1,200))
    t5.forward(r.randint(1,200))
    if t1.xcor() > 1100:
        t1.color("green")
        winner = t1
    elif t2.xcor() > 1100:
        t2.color("green")
        winner = t2
    elif t3.xcor() > 1100:
        t3.color("green")
        winner = t3
    elif t4.xcor() > 1100:
        t4.color("green")
        winner = t4
    elif t5.xcor() > 1100:
        t5.color("green")
        winner = t5
t.done()