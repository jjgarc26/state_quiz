import turtle
from check_state import check_state
from map_marker import map_marker

# --- screen set up ---

screen = turtle.Screen()
screen.bgpic('blank_states_img.gif')


# --- main game ---

state_place_holders = []

while not len(state_place_holders) == 50:

    player_input = turtle.textinput(title='State Quiz', prompt='Enter State')

    check_for_state = check_state(player_input)

    if check_for_state == 'no state found':
        continue
    else:
        marker = map_marker(check_for_state[0], check_for_state[1])
        state_place_holders.append(marker)


screen.mainloop()