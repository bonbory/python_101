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



def points_counter(event):
    global points
    for ball in balls:
        l = ((ball.x - event.x)**2 + (ball.y - event.y)**2) ** 0.5
        if l < ball.r:
            points += 1
            print('Points:', points)


def tick():
    global timer

    for ball in balls:
        ball.move_ball()
    timer += 1
    root.after(50, tick)
    if timer == 120:
        timer = 0
        canv.delete(ALL)
        make_balls(5)
    

def make_balls(number_of_ball):
    global balls
    balls = [Ball() for i in range(number_of_ball)]



def main():
    global root, canv, balls, colors, points, timer

    root = Tk()
    root.geometry('800x600')
    canv = Canvas(root, bg='black')
    canv.pack(fill=BOTH, expand=1)
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    points = 0
    timer = 0

    make_balls(1)
    tick()
    for ball in balls:
       canv.bind('<Button-1>', points_counter)
    
    mainloop()

if __name__ == '__main__':
    main()





