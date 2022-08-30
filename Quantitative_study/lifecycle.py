import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

day = 0
lines_list = list(np.arange(0, 450, 10))
lines_list.insert(1, 1)
print(lines_list)
pysyft_days_dict = dict.fromkeys(lines_list, 0)
fate_days_dict = dict.fromkeys(lines_list, 0)
tff_days_dict = dict.fromkeys(lines_list, 0)
other_days_dict = dict.fromkeys(lines_list, 0)
SO_days_dict = dict.fromkeys(lines_list, 0)

Issues_file = "GitHub_lifecycle.csv"
SO_file = "SO_lifecycle.csv"

df_issue = pd.read_csv(Issues_file, sep=",")
time_list1 = df_issue["lifecycle"].tolist()
frame_list = df_issue["framework"].tolist()
result = Counter(frame_list)
frame = []
for root, num in result.items():
    frame.append(num)
print(result, frame)
for i in range(len(time_list1)):
    for lines in lines_list:
        time_split = time_list1[i].split(" ")
        day = int(time_split[0])+1 if len(time_split) > 1 else 1
        if day <= lines:
            if frame_list[i] == "PySyft":
                pysyft_days_dict[lines] += 1
            elif frame_list[i] == "FATE":
                fate_days_dict[lines] += 1
            elif frame_list[i] == "TFF":
                tff_days_dict[lines] += 1
            elif frame_list[i] == "Others":
                other_days_dict[lines] += 1
df_so = pd.read_csv(SO_file, sep=",")
time_list2 = df_so["lifecycle"].tolist()
sumBug2 = len(time_list2)
print("__________________")
for i in range(len(time_list2)):
    for lines in lines_list:
        time_split = time_list2[i].split(" ")
        day = int(time_split[0]) + 1 if len(time_split) > 1 else 1
        if day <= lines:
            SO_days_dict[lines] += 1

pysyft_rate_list = []
fate_rate_list = []
tff_rate_list = []
other_rate_list = []
SO_rate_list = []
frame_list = []
for lines in pysyft_days_dict:
    pysyft_rate_list.append(pysyft_days_dict[lines] / frame[0])
for lines in fate_days_dict:
    fate_rate_list.append(fate_days_dict[lines] / frame[1])
for lines in tff_days_dict:
    tff_rate_list.append(tff_days_dict[lines] / frame[2])
for lines in other_days_dict:
    other_rate_list.append(other_days_dict[lines] / frame[3])
for lines in SO_days_dict:
    SO_rate_list.append(SO_days_dict[lines] / sumBug2)

print(pysyft_rate_list)
print(fate_rate_list)
print(tff_rate_list)
print(other_rate_list)
print(SO_rate_list)


plt.figure(figsize=(5.5, 3.5))
plt.plot(lines_list, pysyft_rate_list, label=u'PySyft', linewidth=1, color='r', marker = '|', markersize=6)
plt.plot(lines_list, fate_rate_list, label=u'FATE', linewidth=1, color='royalblue', marker = '.', markersize=6)
plt.plot(lines_list, tff_rate_list, label=u'TFF', linewidth=1, color='darkgreen', markersize=2)
plt.plot(lines_list, other_rate_list, label=u'Others', linewidth=1, color='peru', linestyle='--', markersize=6)
plt.plot(lines_list, SO_rate_list, label=u'Stack Overflow', linewidth=1, color='blueviolet', markersize=6)

plt.xlabel(u'Duration of bug (in days)')
plt.ylabel(u'% of fixed bugs')

y = list(np.arange(0, 1.01, 0.25))
plt.yticks(y, ["0", "25%", "50%", "75%", "100%"])
plt.legend(loc='best')
plt.tight_layout()
plt.show()
# plt.savefig('lifecycle.pdf', format = 'pdf', bbox_inches = 'tight')