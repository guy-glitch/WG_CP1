#WG 1st Libraries and built-in functions notes
import turtle as t
import random
t.shape("turtle")
t.speed(120)
while True:
    colors =["orange", "green", "#E6E6FA", "gold"]
    t.color(random.choice(colors))


    t.fillcolor(random.choice(colors))
    t.begin_fill()
    for x in range(1,5):
        t.forward(90)
        t.right(90)
    t.end_fill()

    t.teleport(random.randint(1,100),random.randint(1,100))

    t.fillcolor(random.choice(colors))
    t.begin_fill()
    for x in range(1,5):
        t.forward(90)
        t.right(90)
    t.end_fill()

t.done()