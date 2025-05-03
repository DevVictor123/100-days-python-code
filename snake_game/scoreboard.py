from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Record: {self.high_score} ", align= ALIGNMENT, font= FONT)   

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font= FONT)
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_high_score(self):
        try:
            with open("record.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
    
    def save_high_score(self):
        with open("record.txt", mode="w") as file:
            file.write(str(self.high_score))


