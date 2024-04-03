import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data1 = pd.read_csv("data/lr001_lrtypecosine_trainpsnr.csv")
data2 = pd.read_csv("data/lr0002_lrtypecosine_trainpsnr.csv")
data3 = pd.read_csv("data/lr0005_lrtypecosine_trainpsnr.csv")

label_x = 'Epochs'
label_y = 'PSNR'

plt.figure(figsize=(10,6))
sns.lineplot(data=data1, x='Step', y='Value', label='lr001_lrtypecosine')
sns.lineplot(data=data2, x='Step', y='Value', label='lr0002_lrtypecosine')
sns.lineplot(data=data3, x='Step', y='Value', label='lr0005_lrtypecosine')
plt.legend()
plt.title(f'Train {label_y} vs. {label_x}')
plt.xlabel(label_x)
plt.ylabel(label_y)
plt.show()

