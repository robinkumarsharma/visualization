# Pie Chart
# Qupid - NIAA 2017-2018
# VU, Amsterdam
# Author - Robin Sharma

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

group_names=['Precision','Accuracy','Completeness','Neutrality','Relevance','Readability','Trustworthiness']
group_size=[14.28,14.28,14.28,14.28,14.28,14.28,14.28]

one=['1','1','1','1','1','1','1']
two=['2','2','2','2','2','2','2']
three=['3','3','3','3','3','3','3']
four=['4','4','4','4','4','4','4']
five=['5','5','5','5','5','5','5']

subgroup_size=[4,4,4,4,4,4,4]

a,b,c,d,e,f,g=[plt.cm.Greys, plt.cm.Purples, plt.cm.Blues, plt.cm.Greens, plt.cm.Oranges, plt.cm.Reds, plt.cm.PuBuGn]

fig, ax=plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.25, labels=group_names, colors=[a(0),b(0),c(0.6),d(0),e(0),f(0),g(0.4)])
plt.setp(mypie, width=0.3, edgecolor='black')
# plt.legend(mypie, group_names, loc="left")

#second Ring inside
mypie2,_ = ax.pie(subgroup_size, radius=1.25-0.25, labels=four, labeldistance=0.9,
colors=[a(0),b(0),c(0.6),d(0.6),e(0),f(0),g(0.4)])
plt.setp(mypie2, width=0.3, edgecolor='black')
plt.margins(0,0)

#third Ring inside
mypie3,_ = ax.pie(subgroup_size, radius=1.25-0.5,labels=three,  labeldistance=0.9,
colors=[a(0),b(0),c(0.6),d(0.6),e(0.6),f(0),g(0.4)])
plt.setp(mypie3, width=0.3, edgecolor='black')
plt.margins(0,0)

# #fourth Ring inside
mypie4,_ = ax.pie(subgroup_size, radius=1.25-0.75, labels=two, labeldistance=0.8,
colors=[a(0.6),b(0),c(0.6),d(0.6),e(0.6),f(0.6),g(0.4)])
plt.setp(mypie4, width=0.3, edgecolor='black')
plt.margins(1,1)

# #fith Ring inside
mypie5,_ = ax.pie(subgroup_size, radius=1.25-1, labels=one, labeldistance=0.8,
colors=[a(0.6),b(0.6),c(0.6),d(0.6),e(0.6),f(0.6),g(0.4)])
plt.setp(mypie5, width=0.25, edgecolor='black')
plt.margins(0,0)

#show it
plt.show()
