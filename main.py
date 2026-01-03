import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
data = pd.read_csv("data/winequality-red.csv", sep=';')

#quick view for initial understanding
print(data.head(n=5))

# cleaning and analysis
print("\nChecking for missing data...")
if data.isnull().any().any():
    print("Found some missing values.")
else:
    print("No missing values found. We are good to go!")

print("\nData Info:")
data.info()

#consider 7+ as "great", <5 as "poor", and 5-6 as "average"
n_wines = data.shape[0]

#good wine
quality_above_6 = data.loc[(data['quality'] > 6)]
n_above_6 = quality_above_6.shape[0]

#low quality wine
quality_below_5 = data.loc[(data['quality'] < 5)]
n_below_5 = quality_below_5.shape[0]

#average wine
quality_between_5 = data.loc[(data['quality'] >= 5) & (data['quality'] <= 6)]
n_between_5 = quality_between_5.shape[0]

#high quality
greater_percent = n_above_6 * 100 / n_wines

print(f"\nTotal number of wine data: {n_wines}")
print(f"Wines with rating 7 and above: {n_above_6}")
print(f"Wines with rating less than 5: {n_below_5}")
print(f"Wines with rating 5 and 6: {n_between_5}")
print(f"Percentage of wines with quality 7 and above: {greater_percent:.2f}%")

#basic stats such as mean, min, max, etc.
print("\nBasic Statistics:")
print(np.round(data.describe()))

#histogram for distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='quality', data=data)
plt.title("Distribution of Wine Quality")
plt.show()

#scatter matrix
pd.plotting.scatter_matrix(data, alpha=0.3, figsize=(15, 15), diagonal='kde')
plt.show()

#heatmap
correlation = data.corr()
plt.figure(figsize=(14, 12))
sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")
plt.title("Correlation Heatmap")
plt.show()


#pH drops as acidity rises
fixedAcidity_pH = data[['pH', 'fixed acidity']]
gridA = sns.JointGrid(x="fixed acidity", y="pH", data=fixedAcidity_pH, height=6)
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s": 10})
gridA = gridA.plot_marginals(sns.histplot, kde=True)
plt.show()

fig, axs = plt.subplots(ncols=1, figsize=(10, 6))
sns.barplot(x='quality', y='alcohol', data=data, ax=axs)
plt.title('Quality x Alcohol')
plt.tight_layout()
plt.show()

#Tukey's method to find outliers
for feature in data.keys():
    Q1 = np.percentile(data[feature], q=25)
    Q3 = np.percentile(data[feature], q=75)
    interquartile_range = Q3 - Q1
    step = 1.5 * interquartile_range
    outliers_list = data[~((data[feature] >= Q1 - step) & (data[feature] <= Q3 + step))]
    
    if not outliers_list.empty:
        print(f"Found {len(outliers_list)} outliers for feature '{feature}'")
