import pandas as pd
import matplotlib.pyplot as plt

Uconn_mbb = pd.read_csv("UConnMBB_season_stats.csv")
Uconn_mbb = Uconn_mbb.dropna(axis = 'columns')


Uconn_mbb.sort_values('PPG', inplace = True, ascending = False)
games_played = Uconn_mbb['GP']
player_names = Uconn_mbb['Player']
ppg = Uconn_mbb['PPG']
total_ppg = 0
weighted_ppg = []
for i in range(0,14):
    print(i)
    weighted_ppg.append(ppg[i]*games_played[i]/33)
    total_ppg = total_ppg + weighted_ppg[i]
print(weighted_ppg)
print(total_ppg)


## Games player bar graph
fig, ax1 = plt.subplots()
plt.gcf().subplots_adjust(bottom=0.25, top =0.92)
ax1.bar(range(1,15), games_played, align = 'center', width = 0.5)
ax1.set_xticks(range(1,15))
ax1.set_xticklabels(player_names, rotation = 45, ha="right")
for i, v in zip(range(1,15), games_played):
    ax1.text(i, v, str(v), ha = 'center')
ax1.set_title("Games Played")
plt.savefig("out.png")
