# Read the input file and store the Calories of each Elf's food in a list.
calories = []
current_elf_calories = []
with open('input.txt', 'r') as f:
  for line in f:
    if line.strip():  # Skip blank lines.
      current_elf_calories.append(int(line))
    else:  # This line is blank, so we've reached the end of the current Elf's food.
      calories.append(current_elf_calories)
      current_elf_calories = []  # Start a new list for the next Elf.

# If the last Elf's food list is not empty, we need to append it to the calories list.
if current_elf_calories:
  calories.append(current_elf_calories)

# Find the Elf carrying the most Calories.
max_calories = 0
for elf_calories in calories:
  max_calories = max(max_calories, sum(elf_calories))

# Print the number of total Calories carried by the Elf carrying the most Calories.
print(max_calories)
