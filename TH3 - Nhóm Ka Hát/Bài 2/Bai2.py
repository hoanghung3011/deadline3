import river_problem

state_space = {}
found_state = {}
tmp_queue = []

#Construct state space
tmp_queue.append(river_problem.initial_state)
while tmp_queue:
    tmp_start = tmp_queue.pop(0)
    if tuple(tmp_start) not in state_space:
        state_space[tuple(tmp_start)] = []
    for operator in river_problem.operator_set:
        next_state = operator(tmp_start.copy())
        if next_state != None and next_state not in state_space[tuple(tmp_start)]:
            state_space[tuple(tmp_start)].append(operator(tmp_start.copy()))
            tmp_queue.append(operator(tmp_start.copy()))
    if tmp_start == river_problem.goal_state:
        break

#Pathfinding
tmp_queue.clear()
tmp_queue.append([river_problem.initial_state])
extended_list = []
found_path = []
while tmp_queue:
    tmp_start = tmp_queue.pop()
    if tmp_start[-1] == river_problem.goal_state:
        found_path = tmp_start
        break
    for subsequence_node in state_space[tuple(tmp_start[-1])]:
        if subsequence_node not in extended_list:
            extended_list.append(subsequence_node)
            current_path = tmp_start.copy()
            current_path.append(subsequence_node)
            tmp_queue.append(current_path)
print(found_path)

