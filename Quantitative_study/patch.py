import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from statannot import add_stat_annotation

random.seed(1)
lines_list = list(np.arange(0, 300, 2))
# lines_list.insert(1, 1)
DL_lines_dict = dict.fromkeys(lines_list, 0)
FL_lines_dict = dict.fromkeys(lines_list, 0)

DL_file = "DL_Patch.csv"
FL_file = "FL_Patch.csv"
DL_rate_list = []
FL_rate_list = []
for file in [DL_file, FL_file]:
    df = pd.read_csv(file, sep=",")
    total_list = df["total"].tolist() if file == FL_file else random.sample(df["total"].tolist(), 161)
    for i in range(len(total_list)):
        for lines in lines_list:
            if total_list[i] <= lines:
                if file == DL_file:
                    DL_lines_dict[lines] += 1
                else:
                    FL_lines_dict[lines] += 1

    sumBug = len(total_list)
    if file == DL_file:
        for lines in DL_lines_dict:
            DL_rate_list.append(DL_lines_dict[lines] / sumBug)
    else:
        for lines in FL_lines_dict:
            FL_rate_list.append(FL_lines_dict[lines] / sumBug)
print(DL_rate_list)
print(FL_rate_list)


plt.figure(figsize=(6.8, 3))
plt.figure(1)
plt.subplot(1, 2, 1)
# plt.title('(a) Fix ratio and patch size', fontsize = 'medium', fontweight = 'medium')
plt.plot(lines_list, DL_rate_list, label=u'DL', linewidth=1, color='#1F6092', markersize=5)
plt.plot(lines_list, FL_rate_list, label=u'FL', linewidth=1, color='r', markersize=5)

plt.xlabel(u'LOC')
plt.ylabel(u'% of fixed bugs')

y = list(np.arange(0, 1.01, 0.2))
plt.yticks(y, ["0", "20%", "40%", "60%", "80%", "100%"])
plt.legend(loc='best')

plt.figure(1)
plt.subplot(1, 2, 2)
# plt.title('(b) Distribution of patch size', fontsize = 'medium', fontweight = 'medium')

FL_additions_list = []
FL_deletions_list = []
FL_total_list = []
DL_additions_list = []
DL_deletions_list = []
DL_total_list = []
dataSources = ['FL', 'DL']
for dataSource in dataSources:
    if dataSource == 'FL':
        data_file = "FL_Patch.csv"
        df = pd.read_csv(data_file, sep=",")
        FL_additions_list = df["additions"].tolist()
        FL_deletions_list = df["deletions"].tolist()
        FL_total_list = df["total"].tolist()
    elif dataSource == 'DL':
        data_file = "DL_Patch.csv"
        df = pd.read_csv(data_file, sep=",")
        DL_additions_list = random.sample(df["additions"].tolist(), 161)
        DL_deletions_list = random.sample(df["deletions"].tolist(), 161)
        DL_total_list = random.sample(df["total"].tolist(), 161)
sunBug = len(FL_total_list)
type_list = []
for i in range(sunBug * 6):
    if i < sunBug * 3:
        type_list.append("DL")
    else:
        type_list.append("FL")
way_list = []
for i in range(sunBug * 6):
    if i < sunBug:
        way_list.append("Additions")
    elif i < sunBug * 2:
        way_list.append("Deletions")
    elif i < sunBug * 3:
        way_list.append("Total")
    elif i < sunBug * 4:
        way_list.append("Additions")
    elif i < sunBug * 5:
        way_list.append("Deletions")
    else:
        way_list.append("Total")
data = pd.DataFrame({
    "Lines": DL_deletions_list + DL_additions_list + DL_total_list + FL_additions_list + FL_additions_list + FL_total_list,
    "Source": type_list,
    "Way": way_list,
})

# data.plot.box(showmeans=True)
g = sns.boxplot(x='Way', y='Lines', hue='Source', data=data, width=0.5, showfliers = False)

add_stat_annotation(g, data=data, x='Way', y='Lines', hue='Source',
                   box_pairs=[(("Total", "FL"), ("Total", "DL")),
                                (("Additions", "FL"), ("Additions", "DL")),
                                (("Deletions", "FL"), ("Deletions", "DL"))
                              ],
                   test='Mann-Whitney-gt', text_format='simple', loc='outside', comparisons_correction=None,
                   line_offset_to_box=4, line_offset=0.02, line_height=0.02, text_offset=5,
                   verbose=1)

g.legend(loc="upper left")
plt.xlabel("Count categories")
plt.ylabel("Loc")
plt.tight_layout()
plt.show()
# plt.savefig('../data/Quantitative_study/patch_size.pdf', format='pdf', bbox_inches='tight')

result = stats.mannwhitneyu(DL_total_list, FL_total_list, alternative='greater')
print(result)