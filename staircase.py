# importing Python Maya commands
import maya.cmds as cmds


"""
  Attributes:
    - Coordinates that represents the position of each step.
      x(float): 
      y(float): 
      z(float): 
    - list[]: List that has the 26 duplicate steps.
  Explanation of main program:
    - cmds.polyCube(n='step', h=0.2): Creates a cube which represents the step. 
                                      With height 0.2 and the sx,sy,sz are by default equal to 1.
    - For Loops:
	- for i in range(0,26): Duplicates 26 steps and appeds it to the list.
        
        - for i in range(0,9): Moves the first 9 steps in order to create the first side of the stairs.
                               Moves every step +0,2 on y axis and +1 on the z, in respect to the previous one
        - for i in range(9,18): Moves the next 9 steps in order to create the second side of the stairs.
                               Moves every step +0,2 on y axis and -1 on the x, in respect to the previous one
        - for i in range(18,21): Moves the next 3 steps in order to create the third side of the stairs.
                               Moves every step +0,2 on y axis and -1 on the z, in respect to the previous one
        - for i in range(21,26): Moves the next 5 steps in order to create the fourth side of the stairs.
                              Moves every step +0,2 on y axis and +1 on the x, in respect to the previous one

	- Every more is  	  and say about the coordinate y that increase by 0.2 for every step...)	

"""

# create the first step
cmds.polyCube(n='step',sx=1, sy=1, sz=1, h=0.2)
# duplicate step - total 26 steps 
list=[]
for i in range(0, 26):
    clone = cmds.duplicate('step')
    list.append(clone[0])
# move steps to create the first section of staircase
x=0
y=0
z=0   
for i in range(0,9):   
    cmds.move(x, y, z, list[i])
    z+=1
    y+=0.2
# second section of staircase
x-=1
z-=1
for i in range(9, 18):
    cmds.move(x, y, z, list[i])
    x-=1
    y+=0.2
# third section of staircase
z-=1 
x+=1   
for i in range(18, 21):
    cmds.move(x, y, z, list[i])
    z-=1
    y+=0.2
# fourth section of staircase
x+=1  
z+=1  
for i in range(21, 26):
    cmds.move(x, y, z, list[i])
    x+=1
    y+=0.2

