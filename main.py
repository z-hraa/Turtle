import random 

def roll():
   min_value = 1
   max_value = 6 
   roll = random.randint(min_value, max_value)

   return roll

value = roll()
print(value)


while True:
   players = input("enter the number of players 2-4 ")
   if players.isdigit():
    players = int(players)
    if 2<= players <= 4:
        break
    else:
        print("must be between 2 and 4 players")
   else:
    print("invalid, try again")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
      current_score = 0 

    should_roll = input("would you like to roll(y)?")
    if should_roll.lower() == "y":
        break

    value = roll()
    if value == 1:
        print("you rolled a 1. turn done")
        current_score = 0 
        break
    else: 
        current_score += value
        print("you rolled a:", value)

    print("you score is :", current_score)

player_scores[player_idx] += current_score
print("your total scofre is :", player_scores[player_idx])