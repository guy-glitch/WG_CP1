#import turtle module
import turtle as t
#define function draw_branch(length):
def draw_branch(length):
#if length > 5
    if length > 5:
#for i in range(3):
        for i in range(3):
#forward(length)
            t.forward(length)
#draw_branch(length / 3)
            draw_branch(length/3)
#backward length
            t.backward(length)
#right 60
            t.right(60)

#set up turtle
screen = t.Screen()
screen.setup(1200,1400)
t.speed(1000)
t.color("light blue")
t.teleport(0,0)

for i in range(6):
    draw_branch(100)
    t.right(60)
t.hide()
t.done()