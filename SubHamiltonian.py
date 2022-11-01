# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:00:52 2021

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
lenx = 20
leny = 11

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



#when using, command must be: "body, length, field, food, w, am = move(6,body,length,field,food,am)"
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
#need to define 4 separate sub-Hamiltonians with 4 starting points


#Specific dimensions with starting length of 1!
cycle = int((lenx*(leny-1))/2)

hama = np.zeros(cycle) #bottom left starting point
hamb = np.zeros(cycle) #bottom right starting point
hamc = np.zeros(lenx+1) #right movement across center
hamd = np.zeros(lenx+1) #left movement across center

hama[0:9] = 6
hama[9] = 7
hama[10:18] = 8
hama[18] = 7
hama[19:27] = 6
hama[27] = 7
hama[28:36] = 8
hama[36] = 7
hama[37:45] = 6
hama[45] = 7
hama[46:54] = 8
hama[54] = 7
hama[55:63] = 6
hama[63] = 7
hama[64:72] = 8
hama[72] = 7
hama[73:81] = 6
hama[81] = 7
hama[82:91] = 8
hama[91:100] = 9

hamb[0:9] = 6
hamb[9] = 9
hamb[10:18] = 8
hamb[18] = 9
hamb[19:27] = 6
hamb[27] = 9
hamb[28:36] = 8
hamb[36] = 9
hamb[37:45] = 6
hamb[45] = 9
hamb[46:54] = 8
hamb[54] = 9
hamb[55:63] = 6
hamb[63] = 9
hamb[64:72] = 8
hamb[72] = 9
hamb[73:81] = 6
hamb[81] = 9
hamb[82:91] = 8
hamb[91:100] = 7

hamc[0] = 8
hamc[1:20] = 7
hamc[20] = 6

hamd[0] = 8
hamd[1:20] = 9
hamd[20] = 6

#final hamiltonian initial conditions
hame = np.zeros(112)

hame[0] = 8
hame[1:11] = 9
hame[11:21] = 6
hame[21] = 9
hame[22:31] = 8
hame[31] = 9
hame[32:41] = 6
hame[41] = 9
hame[42:51] = 8
hame[51] = 9
hame[52:61] = 6
hame[61] = 9
hame[62:71] = 8
hame[71] = 9
hame[72:81] = 6
hame[81] = 9
hame[82:91] = 8
hame[91] = 9
hame[92:101] = 6
hame[101] = 9
hame[102:112] = 8

#final hamiltonain
ham = np.zeros(lenx*leny)

ham[0:19] = 7
ham[19:29] = 6
ham[29] = 9
ham[30:39] = 8
ham[39] = 9
ham[40:49] = 6
ham[49] = 9
ham[50:59] = 8
ham[59] = 9
ham[60:69] = 6
ham[69] = 9
ham[70:79] = 8
ham[79] = 9
ham[80:89] = 6
ham[89] = 9
ham[90:99] = 8
ham[99] = 9
ham[100:109] = 6
ham[109] = 9
ham[110:119] = 8
ham[119] = 9
ham[120:129] = 6
ham[129] = 9
ham[130:139] = 8
ham[139] = 9
ham[140:149] = 6
ham[149] = 9
ham[150:159] = 8
ham[159] = 9
ham[160:169] = 6
ham[169] = 9
ham[170:179] = 8
ham[179] = 9
ham[180:189] = 6
ham[189] = 9
ham[190:199] = 8
ham[199] = 9
ham[200:209] = 6
ham[209] = 9
ham[210:220] = 8

'''
#single rotation
if w == 0:
    for i in range(len(ham)): #full length of movements
        m = ham[i] #Hamiltonian Cycle for one rotation
        body,sl,field, w, am = move(m,body,sl,field, am) #movement command
        if w == 0:
            plt.figure("SPF")
            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
            plt.pause(.01) #pauses code for .05 seconds to refresh figure
            pass
        elif w == 4: #occurs when move goes into snake body or wall
            print("You Lose! Better Luck Next Time")
            break
        elif w == 5: #occurs when entire board is filled
            print("Congradulations! You won!")
            break
'''
#body,field,food,w,am,length = reset(lenx,leny,sl)
def subHamiltonian(ham,hama,hamb,hamc,hamd,hame,lenx,leny,sl):
    body,field,food,w,am,length = reset(lenx,leny,sl)
    cycle = int((lenx*(leny-1))/2)
    cl = cycle - 15
    plt.ion()
    plt.figure("SPF")
    plt.title("Snake Playing Field")
    plt.axis("off") #turns off array axes
    
    #initial conditions
    if food[0] > 1 and food[1] < 11:
        body, length, field, food, w, am = move(6, body, length, field, food, am)
        for i in range(len(hama)): #full length of movements
            m = hama[i] #Hamiltonian Cycle for one rotation
            body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
            if w == 0:
                #uncomment if you want to watch what is happening; WARNING may be a long time
                plt.figure("SPF")
                plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                plt.pause(.01) #pauses code for .05 seconds to refresh figure
                pass
            elif w == 4: #occurs when move goes into snake body or wall
                #print("You Lose! Better Luck Next Time") #comment for simulation
                break
            elif w == 5: #occurs when entire board is filled
                #print("Congradulations! You won!") #comment for simulation
                break
    else:
        for i in range(lenx-1):
            body, length, field, food, w, am = move(7, body, length, field, food, am)
        body, length, field, food, w, am = move(6, body, length, field, food, am)
        for i in range(len(hamb)): #full length of movements
            m = hamb[i] #Hamiltonian Cycle for one rotation
            body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
            if w == 0:
                #uncomment if you want to watch what is happening; WARNING may be a long time
                plt.figure("SPF")
                plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                plt.pause(.01) #pauses code for .05 seconds to refresh figure
                pass
            elif w == 4: #occurs when move goes into snake body or wall
                #print("You Lose! Better Luck Next Time") #comment for simulation
                break
            elif w == 5: #occurs when entire board is filled
                #print("Congradulations! You won!") #comment for simulation
                break    
    while True:
        #plt.close("SPF")
        plt.figure("SPF")
        plt.title("Snake Playing Field")
        plt.axis("off") #turns off array axes
        if length < cl:
            if body[-1][1] == 1: #if location is bottom left
                if food[0] > 1 and food[1] < 11: #food region consistent
                    for i in range(len(hama)): #full length of movements
                        m = hama[i] #Hamiltonian Cycle for one rotation
                        body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                        if w == 0:
                            #uncomment if you want to watch what is happening; WARNING may be a long time
                            plt.figure("SPF")
                            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                            plt.pause(.01) #pauses code for .05 seconds to refresh figure
                            pass
                        elif w == 4: #occurs when move goes into snake body or wall
                            #print("You Lose! Better Luck Next Time") #comment for simulation
                            break
                        elif w == 5: #occurs when entire board is filled
                            #print("Congradulations! You won!") #comment for simulation
                            break
                else: #food region inconsistent
                    for i in range(len(hamc)): #full length of movements
                        m = hamc[i] #Hamiltonian Cycle for one rotation
                        body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                        if w == 0:
                            #uncomment if you want to watch what is happening; WARNING may be a long time
                            plt.figure("SPF")
                            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                            plt.pause(.01) #pauses code for .05 seconds to refresh figure
                            pass
                        elif w == 4: #occurs when move goes into snake body or wall
                            #print("You Lose! Better Luck Next Time") #comment for simulation
                            break
                        elif w == 5: #occurs when entire board is filled
                            #print("Congradulations! You won!") #comment for simulation
                            break
                    for i in range(len(hamb)): #full length of movements
                        m = hamb[i] #Hamiltonian Cycle for one rotation
                        body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                        if w == 0:
                            #uncomment if you want to watch what is happening; WARNING may be a long time
                            plt.figure("SPF")
                            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                            plt.pause(.01) #pauses code for .05 seconds to refresh figure
                            pass
                        elif w == 4: #occurs when move goes into snake body or wall
                            #print("You Lose! Better Luck Next Time") #comment for simulation
                            break
                        elif w == 5: #occurs when entire board is filled
                            #print("Congradulations! You won!") #comment for simulation
                            break
                
            elif body[-1][1] == 20: #if location is bottom right
                if food[0] > 1 and food[1] > 10: #food region consistent
                    for i in range(len(hamb)): #full length of movements
                        m = hamb[i] #Hamiltonian Cycle for one rotation
                        body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                        if w == 0:
                            #uncomment if you want to watch what is happening; WARNING may be a long time
                            plt.figure("SPF")
                            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                            plt.pause(.01) #pauses code for .05 seconds to refresh figure
                            pass
                        elif w == 4: #occurs when move goes into snake body or wall
                            #print("You Lose! Better Luck Next Time") #comment for simulation
                            break
                        elif w == 5: #occurs when entire board is filled
                            #print("Congradulations! You won!") #comment for simulation
                            break
                else: #food region inconsistent
                    for i in range(len(hamd)): #full length of movements
                        m = hamd[i] #Hamiltonian Cycle for one rotation
                        body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                        if w == 0:
                            #uncomment if you want to watch what is happening; WARNING may be a long time
                            plt.figure("SPF")
                            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                            plt.pause(.01) #pauses code for .05 seconds to refresh figure
                            pass
                        elif w == 4: #occurs when move goes into snake body or wall
                            #print("You Lose! Better Luck Next Time") #comment for simulation
                            break
                        elif w == 5: #occurs when entire board is filled
                            #print("Congradulations! You won!") #comment for simulation
                            break
                    for i in range(len(hama)): #full length of movements
                        m = hama[i] #Hamiltonian Cycle for one rotation
                        body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                        if w == 0:
                            #uncomment if you want to watch what is happening; WARNING may be a long time
                            plt.figure("SPF")
                            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                            plt.pause(.01) #pauses code for .05 seconds to refresh figure
                            pass
                        elif w == 4: #occurs when move goes into snake body or wall
                            #print("You Lose! Better Luck Next Time") #comment for simulation
                            break
                        elif w == 5: #occurs when entire board is filled
                            #print("Congradulations! You won!") #comment for simulation
                            break
            else:
                print("Error in Starting Location")
                break
        else:
            #initial conditions
            if all(body[-1] == np.array([2,1])): #if location is bottom left
                body, length, field, food, w, am = move(8, body, length, field, food, am) #movement command
            elif all(body[-1] == np.array([2,20])): #if location is bottom right
                for i in range(len(hame)): #full length of movements
                    m = hame[i] #Hamiltonian Cycle for one rotation
                    body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                    if w == 0:
                        #uncomment if you want to watch what is happening; WARNING may be a long time
                        plt.figure("SPF")
                        plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                        plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                        plt.pause(.01) #pauses code for .05 seconds to refresh figure
                        pass
                    elif w == 4: #occurs when move goes into snake body or wall
                        #print("You Lose! Better Luck Next Time") #comment for simulation
                        break
                    elif w == 5: #occurs when entire board is filled
                        #print("Congradulations! You won!") #comment for simulation
                        break
            else:
                pass
            for i in range(len(ham)): #full length of movements
                m = ham[i] #Hamiltonian Cycle for one rotation
                body, length, field, food, w, am = move(m, body, length, field, food, am) #movement command
                if w == 0:
                    #uncomment if you want to watch what is happening; WARNING may be a long time
                    plt.figure("SPF")
                    plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
                    plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
                    plt.pause(.01) #pauses code for .05 seconds to refresh figure
                    pass
                elif w == 4: #occurs when move goes into snake body or wall
                    #print("You Lose! Better Luck Next Time") #comment for simulation
                    break
                elif w == 5: #occurs when entire board is filled
                    #print("Congradulations! You won!") #comment for simulation
                    break
            if w != 0:
                break
            
    #plt.ioff()
    return(body,length,field,food,w,am)

plt.figure("SPF")
plt.title("Snake Playing Field")
plt.axis("off") #turns off array axes
plt.pause(3)
body,length,field,food,w,am = subHamiltonian(ham,hama,hamb,hamc,hamd,hame,lenx,leny,sl) #1 trial
'''
runs = 10000
score = np.array([])
movesreq = np.array([])

for n in range(runs):
    body,field,food,w,am,length = reset(lenx,leny,sl)
    body, length, field, food, w, am = subHamiltonian(ham,hama,hamb,hamc,hamd,hame,lenx,leny,sl)
    score = np.append(score, length)
    movesreq = np.append(movesreq, am)

print(np.mean(movesreq))
np.savetxt("SubHam20x11SimScores.txt",score)
np.savetxt("SubHam20x11SimMoves.txt",movesreq)
'''
'''
plt.figure("SPF") #opens new figure
plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3) #sets color map of field
plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red") #puts a red dot where the head is
plt.show("SPF") #shows new plot    
'''

'''
#Hamiltonian Map; SubHamiltonian based on rng
plt.figure("HamMap")
plt.title("Sub-Hamiltonian Map")
plt.xlim([0,21])
plt.ylim([0,12])
plt.axis("off")

bodya,fielda,fooda,w,am,lengtha = reset(lenx,leny,sl)
bodya, lengtha, fielda, fooda, w, am = move(6,bodya,lengtha,fielda,fooda,am)

for i in range(0,len(hama)): #full length of movements
    m = hama[i] #Hamiltonian Cycle for one rotation
    
    plt.figure("HamMap")
    if m == 6:
        plt.arrow(bodya[-1][1], bodya[-1][0], dx = 0, dy = 1, head_width = 0.2)
    elif m == 7:
        plt.arrow(bodya[-1][1], bodya[-1][0], dx = 1, dy = 0, head_width = 0.2)
    elif m == 8:
        plt.arrow(bodya[-1][1], bodya[-1][0], dx = 0, dy = -1, head_width = 0.2)
    elif m ==9:
        plt.arrow(bodya[-1][1], bodya[-1][0], dx = -1, dy = 0, head_width = 0.2)
    bodya,sl,fielda,fooda, w, am = move(m,bodya,sl,fielda,fooda, am) #movement command
plt.show("HamMap")

bodyb,fieldb,foodb,w,am,lengthb = reset(lenx,leny,sl)
for i in range(19):
    bodyb, lengthb, fieldb, foodb, w, am = move(7,bodyb,lengthb,fieldb,foodb,am)
bodyb, lengthb, fieldb, foodb, w, am = move(6,bodyb,lengthb,fieldb,foodb,am)
for i in range(0,len(hamb)): #full length of movements
    m = hamb[i] #Hamiltonian Cycle for one rotation
    
    plt.figure("HamMap")
    if m == 6:
        plt.arrow(bodyb[-1][1], bodyb[-1][0], dx = 0, dy = 1, head_width = 0.2)
    elif m == 7:
        plt.arrow(bodyb[-1][1], bodyb[-1][0], dx = 1, dy = 0, head_width = 0.2)
    elif m == 8:
        plt.arrow(bodyb[-1][1], bodyb[-1][0], dx = 0, dy = -1, head_width = 0.2)
    elif m ==9:
        plt.arrow(bodyb[-1][1], bodyb[-1][0], dx = -1, dy = 0, head_width = 0.2)
    bodyb,sl,fieldb,foodb, w, am = move(m,bodyb,sl,fieldb,foodb, am) #movement command
plt.show("HamMap")

bodyc,fieldc,foodc,w,am,lengthc = reset(lenx,leny,sl)
bodyc, lengthc, fieldc, foodc, w, am = move(6,bodyc,lengthc,fieldc,foodc,am)

for i in range(0,len(hamc)): #full length of movements
    m = hamc[i] #Hamiltonian Cycle for one rotation
    
    plt.figure("HamMap")
    if m == 6:
        plt.arrow(bodyc[-1][1], bodyc[-1][0], dx = 0, dy = 1, head_width = 0.2)
    elif m == 7:
        plt.arrow(bodyc[-1][1], bodyc[-1][0], dx = 1, dy = 0, head_width = 0.2)
    elif m == 8:
        plt.arrow(bodyc[-1][1], bodyc[-1][0], dx = 0, dy = -1, head_width = 0.2)
    elif m ==9:
        plt.arrow(bodyc[-1][1], bodyc[-1][0], dx = -1, dy = 0, head_width = 0.2)
    bodyc,sl,fieldc,foodc, w, am = move(m,bodyc,sl,fieldc,foodc, am) #movement command
plt.show("HamMap")

bodyd,fieldd,foodd,w,am,lengthd = reset(lenx,leny,sl)
for i in range(19):
    bodyd, lengthd, fieldd, foodd, w, am = move(7,bodyd,lengthd,fieldd,foodd,am)
bodyd, lengthd, fieldd, foodd, w, am = move(6,bodyd,lengthd,fieldd,foodd,am)
for i in range(0,len(hamd)): #full length of movements
    m = hamd[i] #Hamiltonian Cycle for one rotation
    
    plt.figure("HamMap")
    if m == 6:
        plt.arrow(bodyd[-1][1], bodyd[-1][0], dx = 0, dy = 1, head_width = 0.2)
    elif m == 7:
        plt.arrow(bodyd[-1][1], bodyd[-1][0], dx = 1, dy = 0, head_width = 0.2)
    elif m == 8:
        plt.arrow(bodyd[-1][1], bodyd[-1][0], dx = 0, dy = -1, head_width = 0.2)
    elif m ==9:
        plt.arrow(bodyd[-1][1], bodyd[-1][0], dx = -1, dy = 0, head_width = 0.2)
    bodyd,sl,fieldd,foodd, w, am = move(m,bodyd,sl,fieldd,foodd, am) #movement command
plt.show("HamMap")
'''
