from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

def move_ball():
    global x, y, dx, dy
    canv.move(ball_id, dx, dy)
    x += dx
    y += dy
    if (x + r) >= 800:
        dx = -dx
        dy = rnd(-3, 3)
    elif (x - r) <= 0:
        dx = -dx
        dy = rnd(-3, 3)
    elif (y + r) >= 600:
        dx = rnd(-3, 3)
        dy = -dy
    elif (y - r) <= 5:
        dx = rnd(-3, 3)
        dy = -dy
    root.after(50, move_ball)

def new_ball():
    global x, y, r, ball_id, dx, dy
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    dx = rnd(-10, 10)
    dy = rnd(-10, 10)

    ball_id = canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
 
    root.after(1000, new_ball)

def click(event):
    global pointsG
    l = ((x - event.x)**2 + (y - event.y)**2) ** 0.5
    if l < r:
        pointsG += 1
    print('Points:', pointsG)


new_ball()
move_ball()
pointsG = 0
canv.bind('<Button-1>', click)
mainloop()





