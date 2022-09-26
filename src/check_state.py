import pandas as pd


def check_state(state):
    data = pd.read_csv('50_states.csv')

    # --- check if state is in csv file

    if state in set(data['state']):
        state_info = data[data['state'] == state]
        state_xcor = state_info['x'].values[0]
        state_ycor = state_info['y'].values[0]
        return [state_xcor, state_ycor]
    else:
        return 'no state found'
