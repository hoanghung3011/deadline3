left_side = rich = 1
right_side = thief = 0
initial_state = [3,3,left_side]
goal_state = [0,0,right_side]

def is_valid(no_thief, no_rich):
    return (no_rich >= no_thief) or (no_thief >= no_rich and no_rich == 0) #or (not (no_rich > no_thief and no_rich < 3))
def is_valid_state(state):
    opposite_state = [3-state[0], 3-state[1]]
    return is_valid(opposite_state[thief], opposite_state[rich]) and is_valid(state[thief], state[rich])
def move_1_thief(current_state):
    next_state = current_state
    if next_state[2] == left_side and next_state[thief] > 0:
        next_state[thief] -= 1
        next_state[2] = right_side
        if is_valid_state(next_state):
            return next_state
    elif next_state[2] == right_side and next_state[thief] < 3:
        next_state[thief] += 1
        next_state[2] = left_side
        if is_valid_state(next_state):
            return next_state
    return None

def move_2_thief(current_state):
    next_state = current_state
    if next_state[2] == left_side and next_state[thief] > 1:
        next_state[thief] -= 2
        next_state[2] = right_side
        if is_valid_state(next_state):
            return next_state
    elif next_state[2] == right_side and next_state[thief] < 2:
        next_state[thief] += 2
        next_state[2] = left_side
        if is_valid_state(next_state):
            return next_state
    return None
def move_1_rich(current_state):
    next_state = current_state
    if next_state[2] == left_side and next_state[rich] > 1:
        next_state[rich] -= 1
        next_state[2] = right_side
        if is_valid_state(next_state):
            return next_state
    elif next_state[2] == right_side and next_state[rich] < 2:
        next_state[rich] += 1
        next_state[2] = left_side
        if is_valid_state(next_state):
            return next_state
    return None
def move_2_rich(current_state):
    next_state = current_state
    if next_state[2] == left_side and next_state[rich] > 1:
        next_state[rich] -= 2
        next_state[2] = right_side
        if is_valid_state(next_state):
            return next_state
    elif next_state[2] == right_side and next_state[rich] < 2:
        next_state[rich] += 2
        next_state[2] = left_side
        if is_valid_state(next_state):
            return next_state
    return None
def move_rich_thief(current_state):
    next_state = current_state
    if next_state[2] == left_side and next_state[thief] > 0 and next_state[rich] > 0:
        next_state[thief] -= 1
        next_state[rich] -= 1
        next_state[2] = right_side
        if is_valid_state(next_state):
            return next_state
    elif next_state[2] == right_side and next_state[thief] < 3 and next_state[rich] < 3:
        next_state[thief] += 1
        next_state[rich] += 1
        next_state[2] = left_side
        if is_valid_state(next_state):
            return next_state
    return None
operator_set = [move_1_rich, move_2_rich, move_1_thief, move_2_thief, move_rich_thief]

