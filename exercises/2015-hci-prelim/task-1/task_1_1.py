# get current top team and points from file
infile = open("TOP_TEAM.txt", "r")
curr_top_team, curr_top_points = infile.read()[:-1].split(',')
infile.close()

# get today's team names and points
team_points = list()  # list of tuples, i.e. [(name, points), ...]
teams = 0
while teams < 4:  # only allow input of up to 4 teams
    name = input("\nEnter team name <XXX to exit>: ")
    if name == "XXX":
        break
    elif 1 <= len(name) <= 12:
        wins = input("Enter number of wins: ")
        draws = input("Enter number of draws: ")
        losses = input("Enter number of losses: ")
        points = 3*int(wins) + 1*int(draws) + 0*int(losses)
        team_points.append((name, points))
        teams += 1
    else:
        print("\nError: Invalid name. Try again.\n")

# get today's team with the highest points
highest_team, highest_points = team_points[0]
for index, team in enumerate(team_points):
    name, points = team
    if points > highest_points:
        highest_team, highest_points = team_points[index]

# display today's team with the highest points
print("\nTop today:")
print("{0} with {1} points".format(highest_team, highest_points))

# check if highest points today beat current highest
if highest_points > int(curr_top_points):
    print("\nHighest points today beat the current highest team!")
    outfile = open("TOP_TEAM.txt", "w")
    print("{0},{1}".format(highest_team, highest_points), file=outfile)
    outfile.close()
    print("Record updated.")
else:
    print("\nHighest points today did not beat the current highest team...")
