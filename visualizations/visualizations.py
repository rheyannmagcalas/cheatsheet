import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")

plt.figure(figsize=(15,8))
ax = sns.barplot(x="day", y="total_bill", data=tips, ci = None)
ax.set_title('Total Bill Per Day')
ax.set(xlabel='Total Bill', ylabel='Day')
plt.show()
