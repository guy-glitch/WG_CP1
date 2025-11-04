#WG 1st Maze Generator
#import turtle and random as t and r
import turtle as t
import random as r
#set up the screen
screen = t.Screen()
screen.setup(800,800)
#list row_grid detirmines if there is a wall there
row_grid = [
    [r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]
#list col_grid that detirmenes if there is a wall there
col_grid = [[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)],[r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1)]]
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
    t.teleport(-300,-300)
    t.color("black")
    t.left(90)
    t.forward(600)
    t.right(90)
    t.forward(500)
    t.teleport(300,300)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(500)
    for num in row_grid:
        for num1 in row_grid[num]:
            t.teleport(200+num1*100,num*100+100)
            if row_grid[num][num1]==1:
                t.forward(200)
                continue
            else:
                continue

t.done()