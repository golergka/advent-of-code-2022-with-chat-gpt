# Open the file containing the input data
with open('input.txt') as f:
    # Read the input data
    data = f.read()

# Create a dictionary that maps each letter to the corresponding move
moves = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

# Split the input data into a list of rounds
rounds = data.splitlines()

# Initialize the total score to 0
total_score = 0

# Loop over each round
for round in rounds:
    # Get the predicted move of the opponent
    opponent_move = moves[round[0]]

    # Get your move
    your_move = moves[round[2]]

    # Determine the outcome of the round
    if opponent_move == your_move:
        # The round is a draw
        outcome = 3
    elif (opponent_move == 'rock' and your_move == 'scissors') or (opponent_move == 'paper' and your_move == 'rock') or (opponent_move == 'scissors' and your_move == 'paper'):
        # You lose the round
        outcome = 0
    else:
        # You win the round
        outcome = 6

    # Get the score of your move
    if your_move == 'rock':
        move_score = 1
    elif your_move == 'paper':
        move_score = 2
    else:
        move_score = 3

    # Update the total score
    total_score += move_score + outcome

# Print the total score
print(total_score)