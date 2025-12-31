import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')
df['AREA NAME'].value_counts().plot(kind='bar', color='red',figsize=(12, 6))
plt.title('Top 10 areas with Most Crimes')
plt.xlabel('Area Name')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('areas_plot.png')
plt.show()
