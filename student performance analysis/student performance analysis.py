import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('drive/My Drive/Projects/Students Performance/StudentsPerformance.csv')

print(data.shape)

data.head()

data.info()


# visualising the number of male and female in the dataset

data['gender'].value_counts(normalize = True)
data['gender'].value_counts(dropna = False).plot.bar(color = 'magenta')
plt.title('Comparison of Males and Females')
plt.xlabel('gender')
plt.ylabel('count')
plt.show()
