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

# Sort the calories list in descending order by the sum of each Elf's food Calories.
calories = sorted(calories, key=sum, reverse=True)

# Take the top three Elves carrying the most Calories.
top_calories = calories[:3]

# Compute the total number of Calories carried by these Elves.
total_calories = sum(sum(elf_calories) for elf_calories in top_calories)

# Print the total number of Calories carried by the top three Elves carrying the most Calories.
print(total_calories)
