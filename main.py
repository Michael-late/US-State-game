import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State games")
map_img = "blank_states_img.gif"
screen.addshape(map_img)
screen.setup(width=900, height=600)
turtle.shape(map_img)

states = pd.read_csv("50_states.csv")
state_name = states["state"].to_list()
state_x = states["x"].tolist()
state_y = states["y"].tolist()

def place_state(a):
    state_placement = turtle.Turtle()
    state_placement.penup()
    state_placement.hideturtle()
    state_placement.goto(state_x[state_name.index(a)],state_y[state_name.index(a)])
    state_placement.write(f"{a}")

answer_state = []

score = 0
while score != 50:
    answer = screen.textinput(f"Guess the state {score}/50", prompt="State:").capitalize()
    if answer in state_name:
        score+=1
        place_state(answer)
        answer_state.append(answer)
    
    if answer == "Exit":
        break


#add to csv
state_left = {
    "state": [x for x in state_name if x not in answer_state]
}
df = pd.DataFrame(state_left)
df.to_csv("StateLeft")
    
# screen.mainloop()
