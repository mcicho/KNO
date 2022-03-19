import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('charts.csv')

#print(dataset.head())

"""
##most_fr = dataset['title'].value_counts(ascending=False)
most_fr = dataset['title'].value_counts(ascending=False)[:1]
##most_fr = dataset['title'].value_counts().nlargest(n=1)

least_fr = dataset['title'].value_counts().nsmallest(keep='all')
#least_fr = dataset['title'].value_counts(ascending=True)[:18653]

#print(most_fr, least_fr)
"""

ds_shakira = dataset.loc[dataset['artist'] == 'Shakira']

rank_by_date = ds_shakira.groupby('date', dropna=True).agg({'rank': ['max']})
rank_by_date.plot()
plt.ylabel('Rank')
plt.xlabel('Date')
plt.show()


#print(rank_by_date)





