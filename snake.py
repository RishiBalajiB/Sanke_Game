from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

   def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


   def create_snake(self):
       for position in START_POSITION:
            self.add_segmets(position)

   def add_segmets(self, position):
       new_block = Turtle("square")
       new_block.color("white")
       new_block.penup()
       new_block.goto(position)
       self.segments.append(new_block)

   def reset(self):
       for seg in self.segments:
           seg.goto(1000,1000)
       self.segments.clear()
       self.create_snake()
       self.head = self.segments[0]


   def extent(self):
        self.add_segmets(self.segments[-1].position())

   def move_yo(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        # self.head.segments[0].forward(MOVE_DISTANCE)
        self.head.forward(MOVE_DISTANCE)

   def up(self):
       if self.head.heading() != DOWN:
        self.head.setheading(UP)

   def down(self):
       if self.head.heading() != UP:
        self.head.setheading(DOWN)

   def right(self):
       if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

   def left(self):
       if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)