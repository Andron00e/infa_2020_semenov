from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """
        x/y - координаты мяча
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.maxlength = 80
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 25

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move_ball(self):
        if self.r != 0:
            self.vy -= 2
            self.x += self.vx
            self.y -= self.vy
            if self.x + self.r >= 800 or self.x - self.r <= 0:
                self.vx *= -1
                if self.x + self.r >= 800:
                    self.x = 800 - self.r
                else:
                    self.x = 0 + self.r
            if self.y + self.r >= 550:
                self.vy *= -2 / 3
                self.vx *= 5 / 6
                self.y = 550 - self.r
            canv.coords(self.id, self.x - self.r,
                        self.y - self.r,
                        self.x + self.r,
                        self.y + self.r, )

    def hit_check(self, obj):
        if (self.x - obj.x) * (self.x - obj.x) + (self.y - obj.y) * (self.y - obj.y) < (obj.r + self.r) * (
                obj.r + self.r):

            return True
        else:
            return False

    def kill(self):
        canv.coords(self.id, -100, -100, -100, -100)
        self.vx = 0
        self.vy = 0
        self.r = 0


class gun():
    def __init__(self):
        self.Fire_power = 10
        self.Fire_on = 0
        self.angle = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def Fire_start(self, event):
        self.Fire_on = 1

    def Fire_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.Fire_power * math.cos(self.angle)
        new_ball.vy = - self.Fire_power * math.sin(self.angle)
        balls += [new_ball]
        self.Fire_on = 0
        self.Fire_power = 10

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.Fire_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.Fire_power, 20) * math.cos(self.angle),
                    450 + max(self.Fire_power, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        if self.Fire_on:
            if self.Fire_power < 100:
                self.Fire_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class enemy():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_enemy()
        self.E = 0

    def new_enemy(self):
        color = self.color = 'red'
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        self.x0 = rnd(400, 600)
        self.y0 = rnd(100, 300)
        self.a = rnd(100, 170)
        self.b = rnd(100, 170)
        E = rnd(1, 4)
        if E == 1:
            self.k1 = 1
            self.k2 = 1
        if E == 2:
            self.k1 = -1
            self.k2 = 1
        if E == 3:
            self.k1 = 1
            self.k2 = -1
        if E == 4:
            self.k1 = -1
            self.k2 = -1
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def shot(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.y0 = -1000
        self.x0 = -1000
        self.r = 0
        self.points += points

    def move_enemy(self):
        m = 60
        self.x = self.x0 + self.k1 * self.a * math.sin(self.E)
        self.y = self.y0 + self.k2 * self.b * math.cos(self.E)
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.a *= -1
            if self.x + self.r >= 800:
                self.x = 800 - self.r
            else:
                self.x = 0 + self.r
        if self.y + self.r >= 550 or self.y - self.r < 0:
            self.b *= -1
            if self.y + self.r >= 550:
                self.y0 = self.y
                self.y = 550 - self.r
            else:
                self.y0 = self.y
                self.y = 0 + self.r

        canv.coords(self.id, self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r, )
        self.E += math.pi / m


E1 = enemy()
E2 = enemy()
screen1 = canv.create_text(400, 300, text='', font='14')
g1 = gun()
bullet = 0
balls = []
points = 0
id_points = canv.create_text(30, 30, text=points, font='14')


def new_game(event=''):
    global E1, E2, screen1, balls, bullet, points
    canv.itemconfig(screen1, text='')
    E1.new_enemy()
    E2.new_enemy()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.Fire_start)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<ButtonRelease-1>', g1.Fire_end)                                  
    E1.live = 1
    lop = 1
    E2.live = 1
   
    while lop:  
        E1.move_enemy()
        E2.move_enemy()
        for b in balls:
            b.move_ball()
            if b.maxlength > 0:
                b.maxlength -= 1
                if b.maxlength == 0:
                    b.kill()
            
            if b.hit_check(E1) and E1.live == 1:
                E1.live = 0
                E1.shot()
                points += 1
                canv.itemconfig(id_points, text=points)
            if b.hit_check(E2) and E2.live == 1:
                E2.live = 0
                E2.shot()
                points += 1
                canv.itemconfig(id_points, text=points)
            if E1.live == 0 and E2.live == 0:
                root.after(3000, new_game)
                E1.live = 2
                E2.live = 2
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text = 'Balls spent '+ str(bullet))
                
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()


new_game()
root.mainloop()