from turtle import Turtle
import math


class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(5)
        self.hideturtle()
        self.penup()
        self.draw_grid()
        self.player = 1

    def draw_x(self):
        self.speed(5)
        self.setheading(45)
        self.forward(100)
        self.setheading(-135)
        self.forward(200)
        self.setheading(90)
        self.penup()
        self.speed(30)
        self.forward(200//math.sqrt(2))
        self.pendown()
        self.speed(5)
        self.setheading(-45)
        self.forward(200)

    def draw_o(self):
        self.speed(10)
        self.penup()
        self.setheading(0)
        self.forward(80)
        self.setheading(90)
        self.pendown()
        self.circle(80)

    def draw_grid(self):
        self.speed(10)
        self.goto(-300, -300)
        self.pendown()
        for i in range(4):
            self.forward(600)
            self.left(90)
        self.penup()
        self.goto(-300, 100)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(-300, -100)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(-100, -300)
        self.pendown()
        self.left(90)
        self.forward(600)
        self.penup()
        self.goto(100, -300)
        self.pendown()
        self.forward(600)

    def draw(self):
        if self.player == 1:
            self.draw_x()
            self.player = 2
        else:
            self.draw_o()
            self.player = 1

    def user_choice(self, x, y):
        if x < -100 and y < -100:
            p_input = 'd1'
            self.penup()
            self.goto(-200, -200)
            self.pendown()
            self.draw()
        elif x > -100 and y < -100 and x < 100:
            p_input = 'd2'
            self.penup()
            self.goto(0, -200)
            self.pendown()
            self.draw()
        elif x > 100 and y < -100:
            p_input = 'd3'
            self.penup()
            self.goto(200, -200)
            self.pendown()
            self.draw()
        elif x < -100 and y > -100 and y < 100:
            p_input = 'm1'
            self.penup()
            self.goto(-200, 0)
            self.pendown()
            self.draw()
        elif x > 100 and y > -100 and y < 100:
            p_input = 'm3'
            self.penup()
            self.goto(200, 0)
            self.pendown()
            self.draw()
        elif x > 100 and y > 100:
            p_input = 't3'
            self.penup()
            self.goto(200, 200)
            self.pendown()
            self.draw()
        elif x < 100 and x > -100 and y > 100:
            p_input = 't2'
            self.penup()
            self.goto(0, 200)
            self.pendown()
            self.draw()
        elif x < -100 and y > 100:
            p_input = 't1'
            self.penup()
            self.goto(-200, 200)
            self.pendown()
            self.draw()
        else:
            p_input = 'm2'
            self.penup()
            self.goto(0, 0)
            self.pendown()
            self.draw()
        return [p_input, self.player]
