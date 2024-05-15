import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput("Guess the State", "What the another state call?")
print(answer_state)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
print(data_list)

if answer_state in data_list:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)

# if answer_state c

# def get_mouse_click_corr(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_corr)
#
#
turtle.mainloop()
# screen.exitonclick()
