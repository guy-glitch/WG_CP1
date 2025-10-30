#WG Turtle Race 1st
import turtle as t
import random as r
print("The winner will turn green")
screen = t.Screen()
screen.setup(width=1400, height=1200)
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()

t1.speed(700)

t1.color("black")
t1.teleport(600,700)
t1.right(90)
t1.forward(1400)
t1.left(90)
t1.forward(1)
t1.left(90)
t1.forward(1400)
t1.right(90)

t1.color("LightSlateBlue")
t2.color("OliveDrab1")
t3.color("OrangeRed")
t4.color("firebrick")
t5.color("MediumTurquoise")

t1.speed(110)
t2.speed(110)
t3.speed(110)
t4.speed(110)
t5.speed(110)

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")

t1.teleport(-650, 500)
t2.teleport(-650, 300)
t3.teleport(-650, 100)
t4.teleport(-650, -100)
t5.teleport(-650, -300)

winner = "none"

while winner == "none":
    t1.forward(r.randint(1,50))
    t2.forward(r.randint(1,50))
    t3.forward(r.randint(1,50))
    t4.forward(r.randint(1,50))
    t5.forward(r.randint(1,50))
    if t1.xcor() > 600:
        t1.color("green")
        winner = t1
    elif t2.xcor() > 600:
        t2.color("green")
        winner = t2
    elif t3.xcor() > 600:
        t3.color("green")
        winner = t3
    elif t4.xcor() > 600:
        t4.color("green")
        winner = t4
    elif t5.xcor() > 600:
        t5.color("green")
        winner = t5
t.done()