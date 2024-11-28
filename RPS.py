import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if prev_play == "":
        return random.choice(["R", "P", "S"])

    if prev_play == "R":
        return "P"  
    elif prev_play == "P":
        return "S" 
    elif prev_play == "S":
        return "R"  

    return random.choice(["R", "P", "S"])
