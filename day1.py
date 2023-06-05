file = open("input.txt", "r")
highest_sum = 0
current_sum = 0

for line in file:
    if line.isspace():
        if current_sum > highest_sum:
            highest_sum = current_sum
        current_sum = 0
        continue
    current_sum += int(line)

print(highest_sum)

file.close()