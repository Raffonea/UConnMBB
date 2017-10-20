import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_files = [
    "Game1_Wagner",
    "Game2_NorthEastern",
    "Game3_LoyolaMarymount",
    "Game4_OklahomaState",
    "Game5_Chaminade",
    "Game6_Oregon",
    "Game7_BostonUniversity",
    "Game8_Syracuse",
    "Game9_OhioState"
]
games ={}
for f in data_files:
    d = pd.read_csv(format(f)+".csv")
    key_name = f.replace(".csv", "")
    games[key_name] = d
    d.dropna(axis = "index")

##Types of plays and scores
score_type = {"GOOD!DUNK" :2, "GOOD!LAYUP":2, "GOOD!JUMPER":2, "GOOD!3PTR":3, "GOOD!TIP-IN":2, "GOOD!FTSHOT":1}
missed_type = ["MISSEDLAYUP", "MISSED3PTR", "MISSEDJUMPER", "MISSEDSHOT"]
play_type = ["ASSIST", "TURNOVR",  "SUBOUT:", "SUBIN:", "BLOCK", "REBOUND(OFF)", "REBOUND(DEF)", "TIMEOUTmedia", "TIMEOUT30sec", "FOUL", "STEAL"]

##Margins column of game to floats
pure_margins = {}
margins = {}
for game in games:
    pure_margins[game] = games[game]["MAR"]
    margins[game] = pure_margins[game].dropna()
    margins[game] = margins[game].reset_index(drop = True)
    for margin in margins[game]:
        float(margin)

##Times of all scoring plays
scoring_times = {}
times = {}
for game in games:
    times[game] = games[game]["TIME"]
    time_length = len(times[game])
    scoring_times[game] = []
    for i in range(0, time_length):
        if pure_margins[game][i] >= -9999999:
            scoring_times[game].append(times[game][i])

##margin vs. game time
for game in games:
    fig, ax = plt.subplots()
    ax.plot(range(0,len(margins[game])), margins[game])
    ax.axhline(c = "black", ls = 'dashed')
    ax.set_title("UCONN Score Margin "+game)
    ax.set_yticks(range(int(min(margins[game])), int(max(margins[game]))+1))
    ax.set_xticks([0, len(scoring_times[game])*1/8, len(scoring_times[game])*2/8, len(scoring_times[game])*3/8,len(scoring_times[game])*4/8,len(scoring_times[game])*5/8,len(scoring_times[game])*6/8,len(scoring_times[game])*7/8,len(scoring_times[game])-1])
    ax.set_xticklabels(["Start", "15:00", "10:00", "5:00","Halftime", "15:00", "10:00", "5:00", "Final"])
    plt.savefig(game+".png")
