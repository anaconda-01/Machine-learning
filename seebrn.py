import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')
data=sns.load_dataset('tips')
print(data.head())
sns.relplot(x='total_bill',y='tip',kind="scatter")
