import turtle
import pandas

# Setup the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Variables
data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()
correct_answers = []

while len(correct_answers) < 50:
  answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?").title()

  if answer_state in states:
    correct_answers.append(answer_state)
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()

    state_data = data[data.state == answer_state]
    state.goto(int(state_data.x), int(state_data.y))
    state.write(state_data.state.item())

  

screen.exitonclick()