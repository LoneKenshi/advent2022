file = open("input.txt", "r")
highest_sum = [0, 0, 0]
current_sum = 0

for line in file:
    if line.isspace():
        # for index, elem in enumerate(highest_sum):
        #     if current_sum > elem:
        #         highest_sum[index] = current_sum
        #         break
        highest_sum.append(current_sum)
        highest_sum.sort(reverse=True)
        highest_sum.pop(3)
        current_sum = 0
        continue
    # print(f"{line}")
    current_sum += int(line)

print(f"{highest_sum[0] + highest_sum[1] + highest_sum[2]}")
file.close()
