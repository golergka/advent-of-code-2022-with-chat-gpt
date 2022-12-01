# Read the input file and store the Calories of each Elf's food in a list.
calories = []
with open('input.txt', 'r') as f:
  for line in f:
    if line.strip():  # Skip blank lines.
      calories.append(int(line))

# Find the Elf carrying the most Calories.
max_calories = 0
for c in calories:
  max_calories = max(max_calories, c)

# Print the number of total Calories carried by the Elf carrying the most Calories.
print(max_calories)
