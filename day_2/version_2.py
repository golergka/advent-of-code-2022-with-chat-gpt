# Open the file containing the input data
with open('input.txt') as f:
    # Read the input data
    data = f.read()

# Split the input data into a list of rounds
rounds = data.split()

# Initialize the total score to 0
total_score = 0

# Loop over each round
for round in rounds:
    # Check if the round has the correct format
    if len(round) != 3:
        # Skip the round if it doesn't have the correct format
        continue

    # Get the predicted move of the opponent
    opponent_move = round[0]

    # Get your move
    your_move = round[2]

    # Determine the outcome of the round
    if opponent_move == your_move:
        # The round is a draw
        outcome = 3
    elif (opponent_move == 'A' and your_move == 'Y') or (opponent_move == 'B' and your_move == 'Z') or (opponent_move == 'C' and your_move == 'X'):
        # You win the round
        outcome = 6
    else:
        # You lose the round
        outcome = 0

    # Get the score of your move
    if your_move == 'X':
        move_score = 1
    elif your_move == 'Y':
        move_score = 2
    else:
        move_score = 3

    # Update the total score
    total_score += move_score + outcome

# Print the total score
print(total_score)