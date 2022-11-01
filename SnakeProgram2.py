# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:56:37 2021

@author: Kevin

Kevin Harmer
"""

import numpy as np #numerics
import matplotlib.pyplot as plt #graphics
import random as rd #random number generation
from matplotlib import cm #color sets from matplotlib
import time #for time function
import keyboard #key assignments


colorset = cm.get_cmap('Dark2', 4) #color used in graphics

'''
Part 0: Sensitivity Analysis
Change movements to diagonal, starting point, dimensions, snake length
(including apple gets 2), look for new algorithms, etc.

Sources: Primarily algorithms and related papers
'''


'''
Part 1: Setting the Playing Field
'''
#dimensions: x = horizontal, y = vertical; 20x11 dimensions for phone game
lenx = 20
leny = 11

#field for snake
field = np.array([[0]*(lenx+2)]*(leny+2))

#surrounding area for snake by 3
field[0,] = 3
field[leny+1,] = 3
field[:,0] = 3
field[:,lenx+1] = 3

#snake starting length; starts at 9 on phone game
sl = 9
field[1,1:sl+1] = 1 #labeling the snake as 1

body = np.array([[1,1]]) #parameterizing the body from where movement takes place

for x in range(2,sl+1): #creates starting body based on snake length
    body = np.append(body,[[1,x]],0)

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
            return field
        else: #if space is occupied, rerun without placing apple
            True

field = apple(field, lenx, leny) #reseting field with apple

'''
Part 2: Game Logistics
'''
#defining movement: u = "up", r = "right", d = "down", l = "left"
def move(m, body, sl, field, am): #m: head move, n: tail move
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
        sl = sl + 1 #snake length; adding 1 if apple is eaten
        field[spot[0][0],spot[0][1]] = 1 #head moves to spot; tail stays the same
        if np.min(field) == 0:
            field = apple(field, lenx, leny)
        else:
            w = 5
    elif field[spot[0][0],spot[0][1]] == 1: #1: snake body
        print("You Hit your body! Please Reset")
        w = 4
    elif field[spot[0][0],spot[0][1]] == 3: #3: wall
        print("You Hit the wall! Please Reset")
        w = 4
    else:
        field[body[0][0],body[0][1]] = 0 #sets most recent tail point to 0
        body = np.delete(body, 0, 0) #deleting tail point
        field[spot[0][0],spot[0][1]] = 1 #sets head spot to 1)
    am = am + 1
    return(body, sl, field, w, am)

#when using, command must be: "body, sl, field, w = move(6,body,sl,field)"
'''
Part 3: Game Setup: Graphics
'''
'''
2 Dimensional Plots can improve the intake of data and part 5's simulations.
With graphics linked to program, data can be observed while taking data,
specifically improving the program commands.
'''

#Following Code is Program Code

'''
Part 4: Game Setup: Program Commands
'''
'''
For next time, research how to stop an if statement. That will lead to a
program with a while loop, giving the option which way to move. With this
functioning, manual data can be obtained.
'''

w = 0 #starting directive factor
a = 7 #starting move right
am = 0 #amount of moves

plt.ion() #starts interactive plot; needed inside while loop and for pause
plt.figure("SPF") #opens figure
plt.title("Snake Playing Field") #graphs title
plt.axis("off") #turns off numerical axes
plt.pause(3) #pauses code for three seconds. Use this time to adjust window

while True:
    rest = 20 #rests after 20 moves
    for i in range(rest):
        #w represents win condition    
        if w == 0:
            plt.figure("SPF") #opens new figure of colormap, with red dot on head
            plt.pcolormesh(field,cmap=colorset,rasterized=True, vmin=0, vmax=3)     #sets color map of field
            plt.scatter(body[-1][1]+0.5,body[-1][0]+0.5,color = "red")              #puts a red dot where the head is
            plt.show("SPF") #shows new plot
            plt.pause(.05) #pauses code for .05 seconds to refresh figure
        elif w == 4: #occurs when move goes into snake body or wall
            print("You Lose! Better Luck Next Time")
            break
        elif w == 5: #occurs when entire board is filled
            print("Congradulations! You won!")
            break
        
        t = .25 #movement frequency (per second)
        now = time.time()
        chn = time.time()
        com = "run"
        while (chn - now) < t:
            if keyboard.is_pressed("up"):#up movement; see move function
                a = 6 #parameterize
            elif keyboard.is_pressed("right"):#right movement; see move function
                a = 7 #parameterize
            elif keyboard.is_pressed("down"):#down movement; see move function
                a = 8 #parameterize
            elif keyboard.is_pressed("left"):#left movement; see move function
                a = 9 #parameterize
            elif keyboard.is_pressed("q"):
                com = "quit"
                break
            else:
                chn = time.time()
                pass
        if com == "quit":
            print("Game Successfully Closed")
            break
        else:
            body,sl,field,w,am = move(a,body,sl,field,am)
        #open in two windows
    plt.close()

plt.ioff() #turns off interactive plot

