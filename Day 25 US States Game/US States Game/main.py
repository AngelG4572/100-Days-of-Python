import turtle
import pandas

FONT = ("Times New Roman", 9, "normal")

screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")

score = 0
correct_guesses = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while len(correct_guesses) < 50:
    if score != 0:
        answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        data = data[data.state.isin(correct_guesses) == False]
        data = data["state"].to_list()
        pandas.DataFrame(data).to_csv("states_to_learn.csv")
        break

    if answer_state in data.values:
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        correct_state = data[data["state"] == answer_state]
        state.goto(x=int(correct_state.x), y=int(correct_state.y))
        state.write(arg=answer_state, align="center", font=FONT)
        score += 1
        correct_guesses.append(answer_state)

    else:
        continue
else:
    print("Congrats! You got everything!")

screen.exitonclick()
