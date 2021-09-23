from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Arial", 12, 'normal')
FONT_1 = ("Arial", 28, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(-200, 270)
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score_screen()

    def score_screen(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_screen()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_screen()

