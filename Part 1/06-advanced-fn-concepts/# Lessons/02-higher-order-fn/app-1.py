# higher order functions -> more reusable & modular

# action === cb function
def ninja_action(action, x):
  return action("ninja", x)

def attack(character, x):
  return f"The {character} attacks with a strength of {x}"

def defend(character, x):
  return f"The {character} defends with a block power of {x}"

action_one = ninja_action(attack, 5) 
action_two = ninja_action(defend, 7)
print(action_one) # The ninja attacks with a strength of 5
print(action_two) # The ninja defends with a block power of 7
