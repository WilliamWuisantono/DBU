# Import libraries
import pandas as pd

# Create a DataFrame
data = {'Product': ['A', 'B', 'C'], 'Sales': [100, 200, 300]}
df = pd.DataFrame(data)

# Print DataFrame
print("Original DataFrame:")
print(df)

# Sort by Sales
df_sorted = df.sort_values('Sales', ascending=False)
print("\nDataFrame Sorted by Sales:")
print(df_sorted)

# Exercise 1: modify the script to add a new column for "Profit" and sort by it.
df['Profit'] = df['Sales'] * 0.4
df.sort_values('Profit', ascending=True)
print("\nDataFrame Sorted by Profit:")
print(df)

# Import libraries
import pandas as pd

# Create a DataFrame with missing values
data = {'Country': ['USA', 'UK', 'Canada', None],
        'GDP': [21.43, 2.83, 1.74, 0.3]}
df = pd.DataFrame(data)

# Exercise 2: clean the missing values and sort by GDP
df_cleaned = df.fillna({'Country': 'Indonesia'})
df_cleaned.sort_values('GDP', ascending=True, inplace=True) 

print("\nCleaned and Sorted DataFrame by GDP:")
print(df_cleaned)

# Exercise 3: calculate the total GDP

total_gdp = df_cleaned['GDP'].sum()
print("\nTotal GDP:")
print(total_gdp)

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Exercise 4: generate a scatter plot between two features
x = df['sepal length (cm)']
y = df['sepal width (cm)']
plt.scatter(x, y)
plt.title('Scatter plot of Sepal Length vs Spela Width') 
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)') 
plt.show() 