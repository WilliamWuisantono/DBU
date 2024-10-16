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
    'Variable_B': np.random.randn(data_size),
    'Variable_C': np.random.randint(1, 100, size=data_size),
    'Variable_D': np.random.randn(data_size) * 10,
})

print(data.dtypes)

# Create a pairplot of the dataset
sns.pairplot(data)

# Show the plot
plt.show()

# Optionally, save the plot as a PNG file
# plt.savefig('pairplot_output.png')