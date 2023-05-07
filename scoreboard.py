from turtle import Turtle
ALLINGMENT = "center"
FONT = ("Arial", 22, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.Score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("gray100")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.Score}. High Score {self.high_score}", align=ALLINGMENT, font=FONT)

    def increse_score(self):
        self.Score += 1
        self.update_scoreboard()

    def reset(self):
        if self.Score > self.high_score:
            self.high_score = self.Score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.Score = 0
        self.update_scoreboard()





