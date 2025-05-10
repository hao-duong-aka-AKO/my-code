import turtle

# Create the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Trio Eyes RPG - Undertale-like")

# Create the player
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, 0)  # Start in the center of the screen

# Create some basic map boundaries
boundary_left = -300
boundary_right = 300
boundary_top = 200
boundary_bottom = -200

# Create an enemy
enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.goto(100, 100)  # Enemy's initial position

# Create the dialogue box (for interactions)
dialogue_box = turtle.Turtle()
dialogue_box.hideturtle()
dialogue_box.penup()
dialogue_box.goto(0, -250)
dialogue_box.color("white")
dialogue_box.write("Press 'E' to talk to the enemy.", align="center", font=("Arial", 16, "normal"))

# Player movement functions with boundary checking
def move_up():
    y = player.ycor()
    if y < boundary_top:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > boundary_bottom:
        player.sety(y - 20)

def move_left():
    x = player.xcor()
    if x > boundary_left:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < boundary_right:
        player.setx(x + 20)

# Function to start combat (simple example)
def start_combat():
    dialogue_box.clear()
    dialogue_box.goto(0, -250)
    dialogue_box.write("Battle has started! Use arrow keys to dodge.", align="center", font=("Arial", 16, "normal"))
    
    # Here you could add more combat mechanics, like bullets and dodging, etc.

# Function for dialogue interaction
def interact():
    if player.distance(enemy) < 50:  # If player is close to the enemy
        dialogue_box.clear()
        dialogue_box.goto(0, -250)
        dialogue_box.write("Enemy: 'Do you want to fight or run?'", align="center", font=("Arial", 16, "normal"))
        screen.onkey(start_combat, "f")  # Press 'F' to fight

# Bind keyboard events to player movement
screen.listen()
screen.onkey(move_up, "w")     # W key for up
screen.onkey(move_down, "s")   # S key for down
screen.onkey(move_left, "a")   # A key for left
screen.onkey(move_right, "d")  # D key for right
screen.onkey(interact, "e")    # E key for interact (to talk to enemy)

# Start the game
screen.mainloop()
