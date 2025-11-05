#WG 1st Maze Generator
#import turtle and random as t and r
import turtle as t
import random as r
#set up the screen
screen = t.Screen()
screen.setup(1000,1000)
#list row_grid detirmines if there is a wall there
row_grid = [
    [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]
#list col_grid that detirmenes if there is a wall there
col_grid = [
    [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]
#Def is_solvable
def is_solvable(row_grid, col_grid):
    #set the size as one less then the length of row grid
    size = len(row_grid) - 1
    #Create variable visited
    visited = set()
    #create the list stack with the cordanite 0,0 in it
    stack = [(0, 0)]
    #repeat for while stack exists
    while stack:
        #remove the x, y cordinate that is last from the stack
        x, y = stack.pop()
        #Check if x and y are at the end of size
        if x == size - 1 and y == size - 1:
            #return true
            return True
        #see if x, y are visited
        if (x, y) in visited:
            #continue to next iteration of the loop
            continue
        #Add x, y to visited
        visited.add((x,y))
        #check if x is less then size and if y and x increased by one is still in the grid
        if x < size - 1 and col_grid[y][x+1] == 0:
            #add x plus one to the stack 
            stack.append((x+1,y))
        #check if x is less then size and if y and x increased by one is still in the grid
        if y < size - 1 and row_grid[y+1][x] == 0:
            #add x plus one to the stack 
            stack.append((x, y+1))
        #check if x is less then size and if y and x increased by one is still in the grid
        if x > 0 and col_grid[y][x] == 0:
            #add x plus one to the stack 
            stack.append((x-1, y))
        #check if x is less then size and if y and x increased by one is still in the grid
        if y > 0 and row_grid[y][x] == 0:
            #add x plus one to the stack 
            stack.append((x, y-1))
#if not solvable will return false
    return False
#check if is solvable is true
if is_solvable(row_grid, col_grid)==True:
    t.teleport(-400,-400)
    t.color("black")
    t.left(90)
    t.forward(800)
    t.right(90)
    t.forward(700)
    t.teleport(400,400)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(700)
    for num in row_grid:
        for i in num:
            if i==1:
                t.teleport(-500+100*i,-500+100*i)
                t.forward(100)
                continue
            else:
                continue
t.done()