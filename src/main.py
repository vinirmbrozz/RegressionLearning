import numpy as np
import pandas as pd
import yellowbrick as yb
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('flights.csv')


average_delay = df.groupby('airline')['delay'].mean().reset_index()
print(average_delay)
sns.barplot(x='airline', y='delay', data=average_delay)
plt.title('Average delay by airline')
plt.xlabel('Airline')
plt.ylabel('Average delay')
plt.show()

sns.countplot(x='airline', data=df)
plt.title('Number of flights by airline')
plt.xlabel('Airline')
plt.ylabel('Number of flights')
plt.show()