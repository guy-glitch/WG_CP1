#WG 1st Maze Generator
#import turtle and random as t and r
import turtle as t
import random as r
#list row_grid
row_grid = 
#list col_grid
col_grid = 
#def of maze_design
def maze_design():

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
        visited.add(x, y)
        #check if x is less then size and if y and x increased by one is still in the grid
        if x < size - 1 and col_grid[y][x+1] == 0:
            #add x plus one to the stack 
            stack.append((x+1, y))
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