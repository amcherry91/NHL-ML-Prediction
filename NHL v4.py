import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
import seaborn as sns
sns.set(style="darkgrid")

# To see a larger data head if desired
"""pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)"""

data = pd.read_csv("team_stats_cleaned_test.csv", sep=";")

data = data[["game_id","team_id","HoA","won", "settled_in","head_coach","goals","shots","hits", "pim", "powerPlayOpportunities", "powerPlayGoals", "faceOffWinPercentage", "giveaways", "takeaways",
             "type","away_team_id","home_team_id","away_goals","home_goals","outcome","home_rink_side_start","venue","venue_time_zone_id","venue_time_zone_offset"]]

# LabelEnconder converts strings to numerical values for computation
le = preprocessing.LabelEncoder()
game_id = le.fit_transform(list(data["game_id"]))
team_id = le.fit_transform(list(data["team_id"]))
HoA = le.fit_transform(list(data["HoA"]))
won = le.fit_transform(list(data["won"]))
settled_in = le.fit_transform(list(data["settled_in"]))
head_coach = le.fit_transform(list(data["head_coach"]))
goals = le.fit_transform(list(data["goals"]))
shots = le.fit_transform(list(data["shots"]))
hits = le.fit_transform(list(data["hits"]))
pim = le.fit_transform(list(data["pim"]))
powerPlayOpportunities = le.fit_transform(list(data["powerPlayOpportunities"]))
powerPlayGoals = le.fit_transform(list(data["powerPlayGoals"]))
faceOffWinPercentage = le.fit_transform(list(data["faceOffWinPercentage"]))
giveaways = le.fit_transform(list(data["giveaways"]))
takeaways = le.fit_transform(list(data["takeaways"]))
type = le.fit_transform(list(data["type"]))
away_team_id = le.fit_transform(list(data["away_team_id"]))
home_team_id = le.fit_transform(list(data["home_team_id"]))
away_goals = le.fit_transform(list(data["away_goals"]))
home_goals = le.fit_transform(list(data["home_goals"]))
outcome = le.fit_transform(list(data["outcome"]))
home_rink_side_start = le.fit_transform(list(data["home_rink_side_start"]))
venue = le.fit_transform(list(data["venue"]))
venue_time_zone_id = le.fit_transform(list(data["venue_time_zone_id"]))
venue_time_zone_offset = le.fit_transform(list(data["venue_time_zone_offset"]))

predict = "outcome"

# print data head to show strings converted to list with integer values
"""print(data.head())
print(outcome)"""

# assign data classes to x or y lists for computation
x = list(zip(game_id, team_id, HoA, won, settled_in, head_coach, goals, shots, hits, pim, powerPlayOpportunities, powerPlayGoals, faceOffWinPercentage, giveaways, takeaways,
             type, away_team_id, home_team_id, away_goals, home_goals, home_rink_side_start, venue, venue_time_zone_id, venue_time_zone_offset))
y = list(outcome)

best = 0
for _ in range(5000):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)
# pickle will save the best model so long long as it performs better than the previous best
    if acc > best:
        best = acc
        with open("NHLmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)

#load the best algorithm using the saved pickle file from above
"""pickle_in = open("NHLmodel.pickle", "rb")
linear = pickle.load(pickle_in)
acc = linear.score(x_test, y_test) # acc is short for accuracy
print("Accuracy: ", acc)"""

# compare predicted result to real result
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

# bar chart comparing the outcome to the number of goals based on whether team was home or away
"""sns.barplot(x="outcome", y="goals", hue="HoA", data=data)
pyplot.show()"""

