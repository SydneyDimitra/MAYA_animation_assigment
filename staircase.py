# importing Python Maya commands
import maya.cmds as cmds

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

