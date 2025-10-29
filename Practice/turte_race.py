#WG Turtle Race 1st
import turtle as t
import random as r
print("The winner will turn green")
screen = t.Screen()
screen.setup(width=5858, height=4000)
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()

t1.color("black")
t1.teleport(5000,4000)
t1.right(90)
t1.forward(4000)

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

t1.teleport(-5857, 3800)
t2.teleport(-5857, 3600)
t3.teleport(-5857, 3400)
t4.teleport(-5857, 3200)
t5.teleport(-5857, 3000)

winner = "none"

while winner == "none":
    t1.forward(r.randint(1,500))
    t2.forward(r.randint(1,500))
    t3.forward(r.randint(1,500))
    t4.forward(r.randint(1,500))
    t5.forward(r.randint(1,500))
    if t1.xcor() > 5000:
        t.color("green")
        winner = t1
    elif t2.xcor() > 5000:
        t.color("green")
        winner = t2
    elif t3.xcor() > 5000:
        t.color("green")
        winner = t3
    elif t4.xcor() > 5000:
        t.color("green")
        winner = t4
    elif t5.xcor() > 5000:
        t.color("green")
        winner = t5
t.done()