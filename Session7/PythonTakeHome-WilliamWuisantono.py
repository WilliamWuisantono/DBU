import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define dataset size
data_size = 50

# Exercise 5: Generate a sample dataset and display a pairplot
# Create a sample dataset with numpy np.random.randn(), np.random.rand(), np.random.randint()
data = pd.DataFrame({
    'Variable_A': np.random.randn(data_size),
    'Variable_B': np.random.rand(data_size),
    'Variable_C': np.random.randint(1, 25, size=data_size),
    'Variable_D': np.random.randn(data_size) * 10,
})

# Pairplot didn't print properly so I had to remove the brackets to make it numerical.
print(data.dtypes)

# Create a pairplot of the dataset
sns.pairplot(data)

# Show the plot
plt.show()

# Optionally, save the plot as a PNG file
# plt.savefig('pairplot_output.png')

# Sources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html, 
# https://www.geeksforgeeks.org/pandas-dataframe-dtypes/ - Helped me figure out data type (categorical or numerical)
