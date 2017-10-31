#This program was done using dynamic programming
def find_number_of_steps(index):
    if index == 0:
        return 1 
    elif index < 0:
        return 0
    elif index in dynamically:
        return dynamically[index]
    dynamically[index] = find_number_of_steps(index -1) + find_number_of_steps(index - 2) + find_number_of_steps(index - 3)
    return dynamically[index]

s = int(input().strip())
dynamically = {}
for a0 in range(s):
    value = int(input().strip())
    steps = find_number_of_steps(value)
    print(steps)
