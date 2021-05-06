import turtle
import pandas
from names import StateName

screen = turtle.Screen()
screen.title("US STATES QUIZ")
usa_map  = "blank_states_img.gif"
data = "50_states.csv"
screen.addshape(usa_map)
turtle.shape(usa_map)
state_name = StateName()
df = pandas.read_csv(data)
s=0
while s<50:
    answer_box = screen.textinput("United States Quiz","Guess a name of a state:")
    if answer_box == 'exit':
        break
    location = df[df['state'] == answer_box][{'x','y'}]
    if len(location) == 1:
        s+=1
        state_name.write_it(answer_box,location['x'].iloc[0],location['y'].iloc[0])