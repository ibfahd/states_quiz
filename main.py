import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES QUIZ")
usa_map  = "blank_states_img.gif"
data = "50_states.csv"
screen.addshape(usa_map)
turtle.shape(usa_map)

df = pandas.read_csv(data)

answer_box = screen.textinput("United States Quiz","Guess a name of a state:")

screen.exitonclick()