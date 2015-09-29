from task_2_1 import Pastry


budget = input("Enter budget ($): ")

# remove sold out pastries
pastries = list()
for item in Pastry[1:]:
    if item[2] > 0:
        pastries.append(item)

# sort pastries according to ascending order of price
for i in range(len(pastries)-1):
    for j in range(len(pastries)-1-i):
        if pastries[j][1] > pastries[j+1][1]:
            pastries[j], pastries[j+1] = pastries[j+1], pastries[j]

# TODO: get optimal combinations
