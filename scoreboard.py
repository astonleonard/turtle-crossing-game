from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-200, 255)
        self.hideturtle()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def update_level(self):
        self.level += 1

    def refresh(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write('Game Over', align='center', font=FONT)
