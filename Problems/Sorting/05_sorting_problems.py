'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import data

#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)

headers = data.pop(0)
print(headers)


#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
top_highest = data[:]
top_highest.sort(reverse=True, key= lambda a: a[-1])
top_highest_ten = top_highest[0:9]
for player in top_highest_ten:
    print(player[2])

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)

kobe_data = []
points = []
for player in data:
    if player[2] == "Kobe Bryant":
        kobe_data.append(player)
for player in kobe_data:
    points.append(player[-1])

print("Kobe had", sum(points), "points")

#4  What player has the most 3point field goals in a single season. (3pts)
top_three = data[:]
top_three.sort(reverse=True, key= lambda a: a[-22])
top_three_four = top_three[0:1]
for player in top_three_four:
    print(player[2],"With points at three pointer being", player[-22])



#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)

top_ws = data[:]
top_ws.sort(reverse=True, key= lambda a: a[25])
top_playerws = top_ws[0:1]
for player in top_playerws:
    print(player[2]," with win shares being", player[25])

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".
#who is the most reliable threepointer?

precthree = data[:]
precthree.sort(reverse=True, key= lambda a: a[-20])
top_precthree = precthree[0:1]
for player in top_precthree:
    print(player[2],"is the most reliable threepointer with the precent being", player[-20] * 100, "%")

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)

top_seasons = data[:]
top_seasons.sort(reverse=True, key= lambda a: a[-1])
top_100 = top_seasons[0:100]
top_100.sort(reverse=True, key= lambda a: a[-10])
best_100 = top_100[0:1]
worst_100 = top_100[-2:-1]
for player in best_100:
    print(player[2],"has the best freethrow precentage")
for player in worst_100:
    print(player[2],"has the worst freethrow precentage")