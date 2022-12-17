import turtle
from turtle import Screen, Turtle, colormode, shape

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(1024, 768)
        self.screen.tracer(0,0)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Game")
        self.screen.tracer(0,0)
        self.screen.bgcolor("black")
