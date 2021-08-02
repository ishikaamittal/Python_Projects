import turtle
import pandas

t = turtle.Turtle()
t.hideturtle()
t.penup()

screen = turtle.Screen()
screen.title("State games")
# screen.setup(width=600, height=400)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

no_of_states = []

while len(no_of_states) < 29:
    user_input = screen.textinput(title=f"{len(no_of_states)}/29 correct", prompt="What's you guess?").title()

    if user_input in states:
        no_of_states.append(user_input)
        right_state = data[data.state == user_input]
        t.goto(int(right_state.x), int(right_state.y))
        t.write(user_input)

    if user_input == "Exit":
        missing_states = [m for m in states if m not in no_of_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
