#WG 1st Maze Generator
#import turtle and random as t and r
import turtle as t
import random as r
#hide the turtle
#t.hideturtle()
#increase speed
t.speed(1)
#set up the screen
screen = t.Screen()
screen.setup(1000,1000)
#list row_grid detirmines if there is a wall there
#loop
row_grid = []
col_grid = []
def maze_setup():
    row_grid = [
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]
    #list col_grid that detirmenes if there is a wall there
    col_grid = [
        [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]
    return row_grid, col_grid
#Def is_solvable
def is_solvable(row_grid, col_grid):
    #set the size as one less then the length of row grid
    size = len(row_grid)-1  
    #Create variable visited
    visited = set()
    #create the list stack with the coordinate 0,0 in it
    stack = [(0, 0)]
    #repeat for while stack exists
    while stack:
        #remove the x, y coordinate that is last from the stack
        x, y = stack.pop()
        #Check if x and y are at the end of size
        if x == size and y == size:
            #return true
            return True
            break
        #see if x, y are visited
        if (x, y) in visited:
            #continue to next iteration of the loop
            continue
        #Add x, y to visited
        visited.add((x,y))
        #check if x is less then size and if y and x increased by one is still in the grid
        if x < size and row_grid[x+1][y] == 0:
            #add x plus one to the stack 
                stack.append((x+1,y))
        #check if x is less than size and if y and x increased by one is still in the grid
        if y < size and col_grid[x][y+1] == 0:
            #add x plus one to the stack
                stack.append((x, y+1))
        #check if x is less then size and if y and x increased by one is still in the grid
        if x > 0 and row_grid[x-1][y] == 0:
            #add x plus one to the stack 
            stack.append((x-1, y))
        #check if x is less then size and if y and x increased by one is still in the grid
        if y > 0 and col_grid[x][y-1] == 0:
            #add y minus one to the stack 
            stack.append((x, y-1))
#if not solvable will return false
    return False
#check if is solvable is true

while True:
    row_grid, col_grid = maze_setup()
    solvable = is_solvable(row_grid, col_grid)
    if solvable==True:
        #draw maze block square
        t.teleport(-400,-400)
        t.color("black")
        t.left(90)
        t.forward(800)
        t.right(90)
        t.forward(800-800/6)
        t.teleport(400,400)
        t.right(90)
        t.forward(800)
        t.right(90)
        t.forward(800-800/6)
        t.teleport(-400,-400+800/6)
        t.right(180)
        #loop through row_grid
        for num in row_grid:
            #loop through each number in num and check if there is a wall there drawing it after it checks
            for i in range(0,len(num)):
                t.penup()
                if num[i]==1:
                    t.pendown()
                t.forward(800/6)
            #teleport to next coordinate
            t.teleport(-400,t.ycor()+800/6)
        #reset turtle position
        t.teleport(-400+800/6,-400)
        #turn the turtle to draw columns
        t.left(90)
        #loop through col_grid
        for num in col_grid:
            #loop through each number in num and check if there is a wall there drawing it after it checks
            for i in range(0,len(num)):
                t.penup()
                if num[i]==1:
                    t.pendown()
                t.forward(800/6)
            #teleport to next coordinate
            t.teleport(t.xcor()+800/6,-400)
                
        t.done()
        break