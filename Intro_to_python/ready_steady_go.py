import turtle
import random

y_pos = -100

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

#create user turtle
user = turtle.Turtle()
user.shape("turtle")
user.color("red")
user.penup()
user.goto(-200, 100)

# Function to move the user turtle
def move_right():
    x = user.xcor()
    if x < 205:
        user.setx(x + 20)

# Keyboard events
screen.listen()
screen.onkey(move_right, "Right")

# Create players
colors = [ "blue", "green", "orange", "purple"]
players = []

# Position and create players
for color in colors:
  player = turtle.Turtle(shape="turtle")
  player.color(color)
  player.penup()
  player.goto(-200, y_pos)
  players.append(player)
  y_pos += 50

# Move players forward
def move_players():
  for player in players:
    distance = random.randint(1, 10)
    player.forward(distance)

# Check if any turtle has reached the finish line
def check_winner():
  players.append(user)
  for player in players:
    if player.xcor() >= 200:
      return player.color()[0]  # Return the color of the winning turtle

  return None


# Game loop
game_over = True
while game_over:
    move_players()
    for player in players:
        if player.xcor() >= 200 :
            game_over = True
            if user.xcor()> player.xcor():
              winner="red"
            else:
              winner = player.color()[0]
            break

# Display the winner
if winner:
    turtle.write(f"The {winner.upper()} turtle wins!", align="center", font=("Arial", 16, "bold"))
    turtle.hideturtle()





