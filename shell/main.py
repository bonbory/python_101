from tkinter import *
from random import randrange as rnd, choice
import time


class Ball:
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dx = rnd(-10, 10)
        self.dy = rnd(-10, 10)
        self.points = 0
        self.ball_id = canv.create_oval(self.x - self.r, self.y - self.r, 
                                        self.x + self.r, self.y + self.r,
                                        fill=choice(colors), width=0)

    def move_ball(self):
        canv.move(self.ball_id, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        if (self.x + self.r) >= 800:
            self.dx = -self.dx
            self.dy = rnd(-3, 3)
        elif (self.x - self.r) <= 0:
            self.dx = -self.dx
            self.dy = rnd(-3, 3)
        elif (self.y + self.r) >= 600:
            self.dx = rnd(-3, 3)
            self.dy = -self.dy
        elif (self.y - self.r) <= 5:
            self.dx = rnd(-3, 3)
            self.dy = -self.dy

    def points_counter(self, event):
        self.l = ((self.x - event.x)**2 + (self.y - event.y)**2) ** 0.5
        if self.l < self.r:
            self.points += 1
            print('Points:', self.points)

    def new_ball(self):
        canv.delete(ALL)
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dx = rnd(-10, 10)
        self.dy = rnd(-10, 10)
        self.ball_id = canv.create_oval(self.x - self.r, self.y - self.r, 
                                        self.x + self.r, self.y + self.r,
                                        fill=choice(colors), width=0)
      

def tick():
    global timer
    ball.move_ball()
    root.after(50, tick)
    

def main():
    global root, canv, ball, colors, timer

    timer = 0
    root = Tk()
    root.geometry('800x600')
    canv = Canvas(root, bg='black')
    canv.pack(fill=BOTH, expand=1)
    colors = ['red', 'orange', 'yellow', 'green', 'blue']

    
    ball = Ball()
    tick()

    canv.bind('<Button-1>', ball.points_counter)
    mainloop()

if __name__ == '__main__':
    main()





