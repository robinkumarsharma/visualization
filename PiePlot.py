# Pie Chart
# Qupid - NIAA 2017-2018
# VU, Amsterdam
# Author - Robin Sharma

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors as mcolors
import pandas as pd
import time

df_1 = pd.read_csv('quality.csv')
group_names=list(df_1)[1:]
legend_name = group_names
nn_1 = len(group_names)
values=df_1.loc[0].drop('filename').values.flatten().tolist()

# Assign Pie chart header as the corresponding quntity measure
group_names = values

# group_names=['Precision','Accuracy','Completeness','Neutrality','Relevance','Readability','Trustworthiness']
group_size=[14.28,14.28,14.28,14.28,14.28,14.28,14.28]

one=['1','1','1','1','1','1','1']
two=['2','2','2','2','2','2','2']
three=['3','3','3','3','3','3','3']
four=['4','4','4','4','4','4','4']
five=['5','5','5','5','5','5','5']

subgroup_size=[4,4,4,4,4,4,4]

a,b,c,d,e,f,g=[plt.cm.Greys, plt.cm.Purples, plt.cm.Blues, plt.cm.Greens, plt.cm.Oranges, plt.cm.Reds, plt.cm.PuBuGn]

all_color = [a(0),a(0.6),b(0),b(0.6),c(0),c(0.6),d(0),d(0.6),e(0),e(0.6),f(0),f(0.6),g(0),g(0.4)]

color_1 = [a(0),b(0),c(0.0),d(0),e(0),f(0),g(0.0)]
color_2 =[a(0),b(0),c(0.0),d(0),e(0),f(0),g(0.0)]
color_3 =[a(0),b(0),c(0.0),d(0),e(0),f(0),g(0.0)]
color_4 =[a(0),b(0),c(0.0),d(0),e(0),f(0),g(0.0)]
color_5 =[a(0),b(0),c(0.0),d(0),e(0),f(0),g(0.0)]


#  ['Accuracy', 'Completeness', 'Neutrality', 'Relevance', 'Readiblity', 'Trustworthyness', 'Precision']
for n, i in enumerate(values):
	k=n+n
	if(i > 4):
		# print('4> ','n:',n,' i: ',i,' k: ',k)
		color_5[n] = all_color[k+1]
		color_4[n] = color_3[n] =  color_2[n] =  color_1[n] = color_5[n]
	elif(i > 3):
		# print('3>','n:',n,' i: ',i,' k: ',k)
		color_5[n] = all_color[k]
		color_4[n] = color_3[n] =  color_2[n] =  color_1[n] = all_color[k+1]
	elif(i > 2):
		# print('2> n:',n,' i: ',i,' k: ',k)	
		color_5[n] = color_4[n] = all_color[k]
		color_3[n] =  color_2[n] =  color_1[n] = all_color[k+1]
	elif(i > 1):
		# print('1> n:',n,' i: ',i,' k: ',k)
		color_5[n] = color_4[n] = color_3[n] = all_color[k]
		color_2[n] =  color_1[n] = all_color[k+1]
	elif(i > 0):
		# print('0> n:',n,' i: ',i,' k: ',k)
		color_5[n] = color_4[n] = color_3[n] = color_2[n] = all_color[k]
		color_1[n] = all_color[k+1]
	elif(i <= 0):
		# print('<0 n:',n,' i: ',i,' k: ',k)
		color_5[n] = color_4[n] = color_3[n] = color_2[n] = color_1[n] = all_color[k]

# Start time
start = time.time()

fig, ax=plt.subplots()
mpl.rcParams['font.size'] = 20.0
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.25, labels=group_names, colors=color_5) #[a(0),b(0),c(0.6),d(0),e(0),f(0),g(0.4)])
plt.setp(mypie, width=0.3, edgecolor='black')


#second Ring inside
mypie2,_ = ax.pie(subgroup_size, radius=1.25-0.25, labeldistance=0.9,
colors=color_4)#[a(0),b(0),c(0.6),d(0.6),e(0),f(0),g(0.4)])
plt.setp(mypie2, width=0.3, edgecolor='black')
plt.margins(0,0)

#third Ring inside
mypie3,_ = ax.pie(subgroup_size, radius=1.25-0.5,  labeldistance=0.9,
colors=color_3)#[a(0),b(0),c(0.6),d(0.6),e(0.6),f(0),g(0.4)])
plt.setp(mypie3, width=0.3, edgecolor='black')
plt.margins(0,0)

# #fourth Ring inside
mypie4,_ = ax.pie(subgroup_size, radius=1.25-0.75, labeldistance=0.8,
colors=color_2)#[a(0.6),b(0),c(0.6),d(0.6),e(0.6),f(0.6),g(0.4)])
plt.setp(mypie4, width=0.3, edgecolor='black')
plt.margins(1,1)

# #fith Ring inside
mypie5,_ = ax.pie(subgroup_size, radius=1.25-1, labeldistance=0.8,
colors=color_1)#[a(0.6),b(0.6),c(0.6),d(0.6),e(0.6),f(0.6),g(0.4)])
plt.setp(mypie5, width=0.25, edgecolor='black')
plt.margins(0,0)

plt.legend(mypie5, legend_name, loc="best")

#show it
plt.show()

# End time
end = time.time()

print(end-start)
