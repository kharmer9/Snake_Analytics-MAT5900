# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:50:31 2021

@author: Kevin

Kevin Harmer
"""

import numpy as np #numerics
import matplotlib.pyplot as plt #graphics
import random as rd #random number generation
from matplotlib import cm #color sets from matplotlib

colorset = cm.get_cmap('Dark2', 4) #color used in graphics

'''
Part 0: Sensitivity Analysis
Change movements to diagonal, starting point, dimensions, snake length
(including apple gets 2), look for new algorithms, etc.

Sources: Primarily algorithms and related papers
'''


'''
Part 1: Setting the Playing Field
Note: Setup for shortest path is different than snakesetup 1 and 2 in order to
cooperate with simulation loop. Recommended for Hamiltonian
'''

#dimensions: x = horizontal, y = vertical; 20x11 dimensions for phone game
lenx = 7
leny = 5

#snake starting length; starts at 9 on phone game
sl = 1

#apple
def apple(field, lenx, leny):
    '''
    Randomly generates an apple (value 2) at a random point in the field (with
    dimensions lenx and leny) with a magnitdue of 0. Snake has value 1 and
    walls have value 3, so apple cannot be generated at these points.
    '''
    while True:
        #random x and y coordinates inside box
        x = rd.randint(1,lenx)
        y = rd.randint(1,leny)
        if field[y, x] == 0: #if space is not occupied, place apple
            field[y, x] = 2
            food = np.array([y,x])
            return field, food
        else: #if space is occupied, rerun without placing apple
            True

def reset(lenx,leny,sl):
    #field for snake
    field = np.array([[0]*(lenx+2)]*(leny+2))
    #surrounding area for snake by 3
    field[0,] = 3
    field[leny+1,] = 3
    field[:,0] = 3
    field[:,lenx+1] = 3
    field[1,1:sl+1] = 1 #labeling the snake as 1
    body = np.array([[1,1]]) #parameterizing the body from where movement takes place
    for x in range(2,sl+1): #creates starting body based on snake length
        body = np.append(body,[[1,x]],0)
    field, food = apple(field, lenx, leny) #reseting field with apple
    w = 0
    am = 0
    length = sl
    return(body,field,food,w,am,length)

'''
Part 2: Game Logistics
'''
#defining movement: u = "up", r = "right", d = "down", l = "left"
def move(m, body, length, field, food, am): #m: head move, n: tail move
    movements = [6, 7, 8, 9] #(up, right, down, left)
    (u,r,d,l) = movements
    #zip function goes through a function, x+y in this case, that two
    #multidimensional arrays go through. So, the head is being shifted slightly
    if m == u:
        spot = [[x + y for x, y in zip(body[-1], [1,0])]]
    elif m == r:
        spot = [[x + y for x, y in zip(body[-1], [0,1])]]
    elif m == d:
        spot = [[x + y for x, y in zip(body[-1], [-1,0])]]
    elif m == l:
        spot = [[x + y for x, y in zip(body[-1], [0,-1])]]
    body = np.append(body, spot, 0) #head movement
    
    w = 0 #variable for loop continuity; 0 = keep playing, 4 = lose, 5 = win
    if field[spot[0][0],spot[0][1]] == 2: #apple
        length = length + 1 #snake length; adding 1 if apple is eaten
        field[spot[0][0],spot[0][1]] = 1 #head moves to spot; tail stays the same
        if np.min(field) == 0:
            field, food = apple(field, lenx, leny)
        else:
            w = 5
    else:
        field[body[0][0],body[0][1]] = 0 #sets most recent tail point to 0
        body = np.delete(body, 0, 0) #deleting tail point
        if field[spot[0][0],spot[0][1]] == 1: #1: snake body
            #print("You Hit your body! Please Reset") #comment for simulation
            w = 4
        elif field[spot[0][0],spot[0][1]] == 3: #3: wall
            #print("You Hit the wall! Please Reset") #comment for simulation
            w = 4
        field[spot[0][0],spot[0][1]] = 1 #sets head spot to 1)
    am = am + 1
    return(body, length, field, food, w, am)

#when using, command must be: "body, length, field, w, am = move(6,body,length,field,am)"
'''
Part 3: Game Setup: Graphics
'''
'''
2 Dimensional Plots can improve the intake of data and part 5's simulations.
With graphics linked to program, data can be observed while taking data,
specifically improving the program commands.
'''

'''
body,field,food = reset(lenx,leny,sl)
#General commands found in other parts of code
plt.figure("SPF")
plt.title("Snake Playing Field")
plt.axis("off") #turns off array axes
#Using the color code at beginning, we create a color contour
plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3)
plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #places red dot where head is
plt.show("SPF") #opens new figure
'''

'''
Part 5: Game Simulation
'''
'''
Reprogram move function to avoid losing. This can provide completely random
set ups. This will likely lead to snake being trapped and forcing a loss.
Statisitcs and Probabililty can be obtained using this method. WARNING:
WITH NO LOSING FACTOR, MAKE SURE THERE IS SOMETHING THAT STOPS WHILE LOOP TO
AVOID PROGRAM DAMAGE.
'''

#Specific dimensions with starting length of 1!

#NOTE: This method is not a Hamiltonian, it is a variation due to the inability
#to create a closed loop. It is still marked hamiltonian for the rest of the code


#set 1 with 1 open spot
ham = np.zeros(2*lenx*leny-2)

ham[0:2] = 7
ham[2:5] = 6
ham[5] = 7
ham[6:9] = 8
ham[9] = 7
ham[10:13] = 6
ham[13] = 7
ham[14:17] = 8
ham[17] = 7
ham[18:22] = 6
ham[22:28] = 9
ham[28] = 8
ham[29] = 7
ham[30] = 8
ham[31] = 9
ham[32:34] = 8

ham[34:36] = 7
ham[36:39] = 6
ham[39] = 7
ham[40:43] = 8
ham[43] = 7
ham[44:47] = 6
ham[47] = 7
ham[48:51] = 8
ham[51] = 7
ham[52:56] = 6
ham[56:62] = 9
ham[62] = 8
ham[63] = 7
ham[64:66] = 8
ham[66] = 9
ham[67] = 8

'''
#set 2: branch loop
ham = np.zeros(54)
ham[0:2] = 7
ham[2:4] = 6
ham[4] = 7
ham[5:7] = 8
ham[7] = 7
ham[8:10] = 6
ham[10] = 7
ham[11:13] = 8
ham[13] = 7
ham[14:17] = 6
ham[17:22] = 9
ham[22:24] = 8
ham[24] = 9
ham[25] = 8
ham[26:28] = 7
ham[28:30] = 6
ham[30] = 7
ham[31:33] = 8
ham[33] = 7
ham[34:36] = 6
ham[36] = 7
ham[37:39] = 8
ham[39] = 7
ham[40:44] = 6
ham[44:50] = 9
ham[50:54] = 8
'''

'''
body,field,food,w,am,length = reset(lenx,leny,sl)
#single rotation
if w == 0:
    plt.ion()
    plt.pause(3)
    for i in range(len(ham)): #full length of movements
        m = ham[i] #Hamiltonian Cycle for one rotation
        body, sl, field, food, w, am = move(m,body,sl,field,food,am) #movement command
        if w == 0:
            plt.figure("SPF")
            plt.title("Snake Playing Field")
            plt.axis("off") #turns off array axes
            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
            plt.pause(.1) #pauses code for .05 seconds to refresh figure
            pass
        elif w == 4: #occurs when move goes into snake body or wall
            print("You Lose! Better Luck Next Time")
            break
        elif w == 5: #occurs when entire board is filled
            print("Congradulations! You won!")
            break
    plt.ioff()
'''      

def Hamiltonian(ham,lenx,leny,sl):
    body,field,food,w,am,length = reset(lenx,leny,sl)
    
    plt.ion()
    plt.figure("SPF")
    plt.title("Snake Playing Field")
    plt.axis("off") #turns off array axes
    plt.pause(3)
    
    while True:
        #plt.close("SPF")
        for i in range(len(ham)): #full length of movements
            m = ham[i] #Hamiltonian Cycle for one rotation
            body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
            if w == 0:
                #uncomment if you want to watch what is happening; WARNING may be a long time
                plt.figure("SPF")
                plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                plt.pause(.02) #pauses code for .05 seconds to refresh figure
                pass
            elif w == 4: #occurs when move goes into snake body or wall
                #print("You Lose! Better Luck Next Time") #comment for simulation
                break
            elif w == 5: #occurs when entire board is filled
                #print("Congradulations! You won!") #comment for simulation
                break
        if w != 0:
            break
    plt.ioff()
    return(body,length,field,food,w,am)

body,length,field,food,w,am = Hamiltonian(ham,lenx,leny,sl) #1 trial
'''
runs = 10000
score = np.array([])
movesreq = np.array([])

for n in range(runs):
    body,field,food,w,am,length = reset(lenx,leny,sl)
    body, length, field, food, w, am = Hamiltonian(ham,lenx,leny,sl)
    score = np.append(score, length)
    movesreq = np.append(movesreq, am)

np.savetxt("AM5x7BranchSimScoreNew.txt",score)
np.savetxt("AM5x7BranchSimMovesNew.txt",movesreq)
'''
'''
plt.figure("SPF") #opens new figure
plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
plt.show("SPF") #shows new plot    
'''

'''
#Hamiltonian Map
plt.figure("HamMap")
plt.title("Almighty Move Branch")
plt.xlim([0,8])
plt.ylim([0,6])
plt.axis("off")
body,field,food,w,am,length = reset(lenx,leny,sl)

for i in range(0,len(ham)): #full length of movements
    m = ham[i] #Hamiltonian Cycle for one rotation
    
    plt.figure("HamMap")
    if m == 6:
        plt.arrow(body[-1][1], body[-1][0], dx = 0, dy = 1, head_width = 0.2)
    elif m == 7:
        plt.arrow(body[-1][1], body[-1][0], dx = 1, dy = 0, head_width = 0.2)
    elif m == 8:
        plt.arrow(body[-1][1], body[-1][0], dx = 0, dy = -1, head_width = 0.2)
    elif m ==9:
        plt.arrow(body[-1][1], body[-1][0], dx = -1, dy = 0, head_width = 0.2)
    body,sl,field,food, w, am = move(m,body,sl,field,food, am) #movement command
plt.show("HamMap")
'''

