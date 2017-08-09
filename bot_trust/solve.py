# Problem statement here: https://code.google.com/codejam/contest/975485/dashboard#s=p0

# set state of both bots
# for instruction i
#    look at this instruction to see who needs to press their button now
#    add walk time + 1 to total time
#    decriment walk time of other bot by walk time +1 of current bot (rectify if negative)
#    get new target pos for current bot
#    update walk time of current bot

input_file = 'large_practice.in'

test_sequences = []
with open(input_file) as f:
    test_num = int(f.readline())
    for t in range(test_num):
        test_sequences.append([])
        prob_def = f.readline().split()
        prob_size = int(prob_def.pop(0))
        for i in range(prob_size):
            test_sequences[t].append((prob_def.pop(0), int(prob_def.pop(0))))

def solve_sequence(seq):
    O_init_walk_time = 0
    B_init_walk_time = 0
    try:
        O_init_walk_time = abs(next_pos('O', 0, seq)-1)
    except Exception:
        pass
    try:
        B_init_walk_time = abs(next_pos('B', 0, seq)-1)
    except Exception:
        pass
    states = {'O': [1, O_init_walk_time], 'B': [1, B_init_walk_time]} # state format [current_pos, walk_time]

    total_time = 0
    for instruction in range(len(seq)):
        target_bot, target_pos = seq[instruction]

        walk_time = states[target_bot][1]
        total_time += walk_time+1

        states[other_bot(target_bot)][1] -= walk_time+1
        states[other_bot(target_bot)][1] = max(0, states[other_bot(target_bot)][1])

        states[target_bot][0] = target_pos
        try:
            states[target_bot][1] = abs(next_pos(target_bot, instruction+1, seq)-states[target_bot][0])
        except Exception:
            pass

    return total_time



def next_pos(target_bot, instruction_ind, seq):
    for bot_name, button_pos in seq[instruction_ind:]:
        if bot_name == target_bot:
            return button_pos
    else:
        raise Exception("Next position not found for {}. (len(seq)=={}, instruction_ind={}, seq={})".format(target_bot, len(seq), instruction_ind, seq))

def other_bot(bot_name):
    if bot_name == 'O':
        return 'B'
    else:
        return 'O'



if __name__ == '__main__':
    for i, seq in enumerate(test_sequences):
        print('Case #{}: {}'.format(i+1, solve_sequence(seq)))
