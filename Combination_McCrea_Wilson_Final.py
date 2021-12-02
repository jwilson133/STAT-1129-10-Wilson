#!/usr/bin/env python
# coding: utf-8

# In[3]:


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 03:16:49 2021

@author: tmccr
"""

"""
import turtle as t
from tkinter import *

t.hideturtle()
t.speed(speed=0)
t.title("American Flag")
t.setup(410,230)

def draw_rectangle(length,height,color):
    t.color(color)
    if color == "white" or "#FFFFFF":
        t.color("black")
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()
        
def draw_star(size,color):
    t.forward(0.5*size)
    t.right(162)
    t.color(color)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()
    t.left(162)
    t.backward(0.5*size)
    
def draw_star_array(rows,columns,E,G,size,color):
    for i in range(rows//2):
        t.backward(E)
        t.right(90)
        t.forward(G)
        for i in range(columns//2):
            t.left(90)
            draw_star(size,color)
            t.right(90)
            t.forward(G*2)
        t.left(90)
        draw_star(size,color)
        t.right(90)
        t.backward(G*columns)
        t.left(90)
        t.backward(E)
        t.right(90)
        for i in range(columns//2):
            t.forward(G*2)
            t.left(90)
            draw_star(size,color)
            t.right(90)
        t.backward(G*(columns-1))
        t.left(90)
    if (rows%2) == 1:
        t.backward(E)
        t.right(90)
        t.forward(G)
        for i in range(columns//2):
            t.left(90)
            draw_star(size,color)
            t.right(90)
            t.forward(G*2)
        t.left(90)
        draw_star(size,color)
        t.right(90)
        t.backward(G*columns)
        t.left(90)
        t.backward(E)

def get_color(color):
    pass

def draw_flag(height):

    A = (height)*1.0    # Hoist (height of the flag)
    B = (height)*1.9    # Fly (width) of the flag
    C = A*(7/13)        # Hoist (height) of the canton ("union)
    D = B*(2/5)         # Fly (width) of the canton
    E = F = (C/10)      # One-tenth of the height of the Canton
    G = H = (D/12)      # One twelfth of the width of the canton
    K = (A/13)*(4/5)    # Diameter of star
    L = (A/13)          # Width of stripe
    
    t.backward((B/2)+3)
    t.left(90)
    t.forward((A/2)+3.5)
    t.right(90)

    draw_rectangle(B,A,"#FFFFFF")           #"white"
    for i in range(6):
        draw_rectangle(B,L,"#B22234")       #"red"
        t.left(90)
        t.backward(L*2)
        t.right(90)
    draw_rectangle(B,L,"#B22234")           #"red"
    t.left(90)
    t.forward(A-L)
    t.right(90)
    
    draw_rectangle(D,C,"#3C3B6E")           #"blue"
    t.left(90)
    draw_star_array(9,11,E,G,K,"#FFFFFF")   #"white"

"""
######Previous main() function######
#def AMflag():    
#    draw_flag(200)
#
#    t.exitonclick()
#    t.done()
"""

draw_flag(200)
ts = t.getscreen()
ts.getcanvas().postscript(file="American_Flag.eps")
t.exitonclick()

from PIL import Image

#Need GhostScripts installed for this to work
#PIL is a backward compatible package, made for earlier itterations of python
#The package name is actually Pillow, but it's still called using PIL

img = Image.open("American_Flag.eps").convert("RGBA")
img.save("American_Flag.png")


# open an image file (.jpg or.png) you have in the working folder
im1 = Image.open("American_Flag.png")

# multiply each pixel by 0.75 (makes the image darker)
# works best with .jpg and .png files, darker < 1.0 < lighter
# (.bmp and .gif files give goofy results)
# note that lambda is akin to a one-line function
im2 = im1.point(lambda p: p * 0.75)

# brings up the modified image in a viewer, simply saves the image as
# a bitmap to a temporary file and calls viewer associated with .bmp
# make certain you have associated an image viewer with this file type
im2.show()

# save modified image to working folder as Audi2.jpg
im2.save("Dark_America_Flag.png")

im3 = Image.open("Dark_America_Flag.png")
im3 = im3.resize((475, 250))   # (500,263) gives a resize to fit the whole width of the board, but isn't in 1.9:1 ration and 263 is rounded down

im3.show()

im3.save("Resized_Dark_America_Flag.png")
"""
###################

import random

def clarity(move):
    if move == "r":
        return "Rock"
    elif move == "p":
        return "Paper"
    elif move == "s":
        return "Scissors"
    elif move == "rock":
        return "Rock"
    elif move == "paper":
        return "Paper"
    elif move == "scissors":
        return "Scissors"
    
def valid_func(move):
    lowermove = move.lower()
    if lowermove == "r":
        return True
    elif lowermove == "p":
        return True
    elif lowermove == "s":
        return True
    elif lowermove == "rock":
        return True
    elif lowermove == "paper":
        return True
    elif lowermove == "scissors":
        return True
    else:
        return False

def raise_exception(move):
    x = valid_func(move)
    if x == True:
        return move
        pass
    elif x == False:
        while True:
            print("Uh oh! It looks like there was a problem with the input you gave.\nPlease try again below.")
            newmove = input("please input 'r' (Rock), 'p' (Paper), or 's' (Scissors) for your move.\nOther player please do not look at their input!\nType Here:")
            newmove = newmove.lower()
            y = valid_func(newmove)
            if y == True:
                break
            else:
                continue
        return newmove

def result_func(p1move, p2move):
    #If p1 won-> True, if lost-> False
    if p1move == "Rock":
        if p2move == "Rock":
            return "Tie"
        elif p2move == "Paper":
            return False
        elif p2move == "Scissors":
            return True
    elif p1move == "Paper":
        if p2move == "Rock":
            return True
        elif p2move == "Paper":
            return "Tie"
        elif p2move == "Scissors":
            return False
    elif p1move == "Scissors":
        if p2move == "Rock":
            return False
        elif p2move == "Paper":
            return True
        elif p2move == "Scissors":
            return "Tie"

def scorekeeper(p1,p2,p1move,p2move):
    if result_func(p1move,p2move) == True:
        p1.score += 1
    elif result_func(p1move,p2move) == False:
        p2.score += 1
    elif result_func(p1move,p2move) == "Tie":
        pass

class Player:
    def __init__(self,name="",move="Rock",score=0):
        self.name = name
        self.move = move
        self.score = score
    pass

def play_2Pgame():
    player = {}
    playername = {}
    move = "Rock"
    score = 0
    playername[1] = input("Player1, please enter your name\nType Here:")
    playername[2] = input("Player2, please enter your name\nType Here:")
    player[1] = Player(playername[1],move,score)
    player[2] = Player(playername[2],move,score)
    while True:
        for i in range(1,3):
            move = input("Player"+str(i)+" please input 'r' (Rock), 'p' (Paper), or 's' (Scissors) for your move.\nOther player please do not look at their input!\nType Here:")
            move = move.lower()
            move = raise_exception(move)
            move = clarity(move)
            player[i].move = move
        scorekeeper(player[1],player[2],player[1].move,player[2].move)
        print("Player1 played",player[1].move,"and Player2 played",player[2].move)
        if result_func(player[1].move,player[2].move) == True:
            print("Player 1, "+str(player[1].name)+", won!")
        elif result_func(player[1].move,player[2].move) == False:
            print("Player 2, "+str(player[2].name)+", won!")
        elif result_func(player[1].move,player[2].move) == "Tie":
            print("It was a Tie.")
        print("The current score is:\nPlayer1:",player[1].score,"vs",player[2].score,":Player2")
        if player[1].score == 2:
            break
        elif player[2].score == 2:
            break
        else:
            continue
    if player[1].score == 2:
        print("Player1, "+str(player[1].name)+", won the duel!")
    elif player[2].score == 2:
        print("Player2, "+str(player[2].name)+", won the duel!") 
    
def play_1Pgame():
    player = {}
    playername = input("Player1, please enter your name\nType Here:")
    move = "Rock"
    score = 0
    player[1] = Player(playername,move,score)
    player[2] = Player("AI",move,score)
    while True:    
        move1 = input("please input 'r' (Rock), 'p' (Paper), or 's' (Scissors) for your move.\nOther player please do not look at their input!\nType Here:")
        move1 = move1.lower()
        move1 = raise_exception(move1)
        move1 = clarity(move1)
        player[1].move = move1
        move2 = random.randint(1,3)
        if move2 == 1:
            move2 = "Rock"
        elif move2 == 2:
            move2 = "Paper"
        elif move2 == 3:
            move2 = "Scissors"
        player[2].move = move2
        scorekeeper(player[1],player[2],player[1].move,player[2].move)
        print("Player1 played",player[1].move,"and the AI played",player[2].move)
        if result_func(player[1].move,player[2].move) == True:
            print("Player 1, "+str(player[1].name)+", won!")
        elif result_func(player[1].move,player[2].move) == False:
            print("The AI won.")
        elif result_func(player[1].move,player[2].move) == "Tie":
            print("It was a Tie.")
        print("The current score is:\nPlayer1:",player[1].score,"vs",player[2].score,":The AI")
        if player[1].score == 2:
            break
        elif player[2].score == 2:
            break
        else:
            continue
    if player[1].score == 2:
        print("Player1, "+str(player[1].name)+", won the duel!")
    if player[2].score == 2:
        print("Unfortunately the AI beat you this game. Better luck next time!")
    


"""
def main():
    x = input("Would you like to play '1' (Single Player) or '2' (2 Player)?\nType Here:")
    if x == "1":
        play_1Pgame()
    elif x == "2":
        play_2Pgame()
    elif x != "1" or "2":
        print("Uh oh! It looks like there was a problem with the input you gave.\nPlease Run the program again.")

if __name__ == "__main__":
    main()
"""

import tkinter as tk
from tkinter import messagebox

def revival():
    
    rev = tk.Tk()
    rev.title("Second chance")
    rev.geometry("320x150")    
    
    class choice:
        def __init__(self,pick="no"):
            self.pick = pick
    
    choose = choice("no")
    
    def select(pick):
        if pick == "yes":
            rev.destroy()
            choose.pick = "yes"
        if pick == "no":
            rev.destroy()
            choose.pick = "no"
    
    text = tk.Label(rev, text = "Uh oh. It looks like you crashed\nWould you like a chance at revival?")
    text.pack(side = "top")
    
    yes = tk.Button(rev, text = "Yes", width = 15, relief="groove", bd=3, command=lambda: select("yes"))
    yes.pack(side = "left")
    no = tk.Button(rev, text = "No", width = 15, relief="groove", bd=3, command=lambda: select("no"))
    no.pack(side = "right")
    
    def RockPaperScissors_mb():
        
        rps = tk.Toplevel()
        rps.title("Rock Paper Scissors")
        rps.geometry("250x100")
        
        
        class move:
            def __init__(self, move="rock"):
                self.move = move
        
        move = move()
        
        def select(choice):
            if choice == "rock":
                rps.destroy()
                move.move = "rock"
            if choice == "paper":
                rps.destroy()
                move.move = "paper"
            if choice == "scissors":
                rps.destroy()
                move.move = "scissors"
        
        text = tk.Label(rps, text = "Pick a move!")
        text.pack(side = "top")
        
        rock = tk.Button(rps, text = "Rock", width = 10, relief="groove", bd=3, command=lambda: select("rock"))
        rock.pack(side = "left")
        paper = tk.Button(rps, text = "Paper", width = 10, relief="groove", bd=3, command=lambda: select("paper"))
        paper.pack(side = "left")
        scissors = tk.Button(rps, text = "Scissors", width = 10, relief="groove", bd=3, command=lambda: select("scissors"))
        scissors.pack(side = "left")
        
        rps.mainloop()
        return move.move
    
    def outcome():
        
        out = tk.Toplevel()
        out.title("Current Standings")
        out.geometry("400x200")
        
        class cont():
            def __init__(self,boolean=False):
                self.boolean = boolean
        
        res = cont(False)
        
        player = {}
        move = "Rock"
        score = 0
        player[1] = Player("",move,score)
        player[2] = Player("AI",move,score)
        while True:    
            move1 = RockPaperScissors_mb()
            move1 = move1.lower()
            move1 = raise_exception(move1)
            move1 = clarity(move1)
            player[1].move = move1
            move2 = random.randint(1,3)
            if move2 == 1:
                move2 = "Rock"
            elif move2 == 2:
                move2 = "Paper"
            elif move2 == 3:
                move2 = "Scissors"
            player[2].move = move2
            scorekeeper(player[1],player[2],player[1].move,player[2].move)
            text1 = tk.Label(out, text = "You played"+str(player[1].move)+"and the AI played"+str(player[2].move))
            text1.pack(side = "top")
            #print("Player1 played",player[1].move,"and the AI played",player[2].move)
            if result_func(player[1].move,player[2].move) == True:
                text2 = tk.Label(out, text = "You won!")
                text2.pack(side = "top")
                #print("Player 1, "+str(player[1].name)+", won!")
            elif result_func(player[1].move,player[2].move) == False:
                text2 = tk.Label(out, text = "The AI won.")
                text2.pack(side = "top")
                #print("The AI won.")
            elif result_func(player[1].move,player[2].move) == "Tie":
                text2.Label(out, text = "It was a Tie.")
                text2.pack(side = "top")
                #print("It was a Tie.")
            text3.Label(out, text = "The current score is:\nYou:"+str(player[1].score)+"vs"+str(player[2].score)+":The AI")
            text3.pack(side = "bottom")
            #print("The current score is:\nYou:",player[1].score,"vs",player[2].score,":The AI")
            if player[1].score == 2:
                break
            elif player[2].score == 2:
                break
            else:
                continue
        if player[1].score == 2:
            text1.Label(out, text = "You won the duel!\nGood luck this time!")
            text1.pack(side = "top")
            out.destroy()
            res.boolean = True
            #print("Player1, "+str(player[1].name)+", won the duel!")
        if player[2].score == 2:
            text1.Label(out, text = "Unfortunately the AI beat you this game. Better luck next time!")
            text1.pack(side = "top")
            out.destroy()
            res.boolean = False
            #print("Unfortunately the AI beat you this game. Better luck next time!")
        
        out.mainloop()
    
    #prog = messagebox.askyesno("Second chance","Uh oh. It looks like you crashed\nWould you like a chance at revival?")
    #if prog == True:
    #    return outcome()
    #else:
    #    pass
    
    rev.mainloop()

#revival()


###################

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


def difficulty():
    
    message_window = tk.Tk()
    message_window.title("Difficulty")
    message_window.geometry("250x100")
    
    class difficulty:
        def __init__(self, difficulty=10):
            self.difficulty = difficulty
    
    diff = difficulty()
    
    def select(choice):
        if choice == "Easy":
            message_window.destroy()
            diff.difficulty = 5
        elif choice == "Medium":
            message_window.destroy()
            diff.difficulty = 10
        elif choice == "Hard":
            message_window.destroy()
            diff.difficulty = 15
        elif choice == "Extreme":
            message_window.destroy()
            diff.difficulty = 25

    text = tk.Label(message_window, text = "Welcome to the Snake Game!\nPlease choose a difficulty!")
    text.pack(side = "top")
    
    easy = tk.Button(message_window, text = "Easy", width = 7, relief="groove", bd=3, command=lambda: select("Easy"))
    easy.pack(side = "right")
    medium = tk.Button(message_window, text = "Medium", width = 7, relief="groove", bd=3, command=lambda: select("Medium"))
    medium.pack(side = "right")
    hard = tk.Button(message_window, text = "Hard", width = 7, relief="groove", bd=3, command=lambda: select("Hard"))
    hard.pack(side = "right")
    extreme = tk.Button(message_window, text = "Extreme", width = 7, relief="groove", bd=3, command=lambda: select("Extreme"))
    extreme.pack(side = "right")
    
    message_window.mainloop()
    return diff.difficulty
    
difficulty = difficulty()


class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
    
    
class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                score = len(s.body)
                if score > high_score:
                    high_score = score
                score_p = "Score: " + str(score) + ", High Score: " + str(high_score) + ", Play Again..."
                message_box('Game Over!', score_p)
                s.reset((10,10))
                break
    
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
    
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
    
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)
        
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    bg = pygame.image.load("Resized_Dark_America_Flag.png")
    surface.blit(bg,(12.5,125))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    
    positions = item.body
    
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    
    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), color=(0,255,0))
    flag = True
    
    clock = pygame.time.Clock()
    high_score = 0
    
    while flag:
        pygame.time.delay(50)
        clock.tick(difficulty)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))
            
        #for x in range(len(s.body)):
        #    if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
        #        score = len(s.body)
        #        if score > high_score:
        #            high_score = score
        #        score_p = "Score: " + str(score) + ", High Score: " + str(high_score) + ", Play Again..."
        #        message_box('Game Over!', score_p)
        #        s.reset((10,10))
        #        break
        #redrawWindow(win)
        
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                if revival() == False:
                    score = len(s.body)
                    if score > high_score:
                        high_score = score
                    score_p = "Score: " + str(score) + ", High Score: " + str(high_score) + ", Play Again..."
                    message_box('Game Over!', score_p)
                    s.reset((10,10))
                    break
                else:
                    clock.tick(0)
                    if keys:
                        clock.tick(difficulty)
        redrawWindow(win)
    
    pass

if __name__ == "__main__":
    main()





# In[ ]:




