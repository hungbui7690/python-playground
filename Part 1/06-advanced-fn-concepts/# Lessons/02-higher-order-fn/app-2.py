# built-in higher order functions -> ex: map, filter

# ******************
# 1 - map function
# ******************

moves = ['punch', 'kick', 'block', 'dodge']

def make_move_powerful(move):
    return f"{move.upper()}!!!"

powerful_moves = map(make_move_powerful, moves)
print(list(powerful_moves)) # ['PUNCH!!!', 'KICK!!!', 'BLOCK!!!', 'DODGE!!!']


# ******************
# 2 - filter function
# ******************

scores = [20, 95, 45, 85, 90, 15, 55, 100, 10]

def is_high_score(score):
    return score >= 90

high_scores = filter(is_high_score, scores)
print(list(high_scores)) # [95, 90, 100]
