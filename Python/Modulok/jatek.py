import turtle
import random

# Initialize Turtle
win = turtle.Screen()
win.title("Flappy Bird")
win.bgcolor("white")

# Set up some constants
WIDTH, HEIGHT = 480, 320
BIRD_SIZE = 20
PIPE_WIDTH, PIPE_HEIGHT = 50, 320
PIPE_GAP = 100
PIPE_VELOCITY = 2
GRAVITY = 1

# Set up some variables
bird_pos = [WIDTH // 2, HEIGHT // 2]
pipe_pos = [WIDTH, random.randint(0, HEIGHT - PIPE_GAP)]
score = 0
running = True

# Create the bird
bird = turtle.Turtle()
bird.shape("square")
bird.shapesize(BIRD_SIZE // 20, BIRD_SIZE // 20)
bird.color("red")
bird.penup()
bird.goto(bird_pos)

# Create the pipes
pipe_top = turtle.Turtle()
pipe_top.shape("square")
pipe_top.shapesize(PIPE_WIDTH // 20, PIPE_HEIGHT // 20)
pipe_top.color("blue")
pipe_top.penup()
pipe_top.goto(pipe_pos)

pipe_bottom = turtle.Turtle()
pipe_bottom.shape("square")
pipe_bottom.shapesize(PIPE_WIDTH // 20, PIPE_HEIGHT // 20)
pipe_bottom.color("blue")
pipe_bottom.penup()
pipe_bottom.goto(pipe_pos[0], pipe_pos[1] + PIPE_GAP)

# Create a function to draw the score
def draw_score():
    global score
    score_text = "Score: {}".format(score)
    turtle.write(score_text, font=("Arial", 16, "normal"))

# Create a function to check for collisions
def check_collision():
    if bird_pos[1] > HEIGHT or bird_pos[1] < 0:
        return True
    if pipe_pos[0] < 0 and pipe_pos[0] + PIPE_WIDTH > bird_pos[0] and pipe_pos[1] < bird_pos[1] + BIRD_SIZE < pipe_pos[1] + PIPE_GAP:
        return True
    return False

# Create a function to update the game state
def update():
    global bird_pos, pipe_pos, score
    bird_pos[1] += GRAVITY
    pipe_pos[0] -= PIPE_VELOCITY
    if pipe_pos[0] < -PIPE_WIDTH:
        pipe_pos[0] = WIDTH
        pipe_pos[1] = random.randint(0, HEIGHT - PIPE_GAP)
        score += 1

# Game loop
while running:
    for event in turtle.event.get():
        if event.type == turtle.ONKEYPRESS:
            if event.key == "space":
                bird_pos[1] -= 50
        if event.type == turtle.ONCLOSE:
            running = False

    win.clearscreen()
    draw_score()
    if check_collision():
        running = False
    bird.goto(bird_pos)
    pipe_top.goto(pipe_pos)
    pipe_bottom.goto(pipe_pos[0], pipe_pos[1] + PIPE_GAP)
    update()

# Quit Turtle
turtle.done()