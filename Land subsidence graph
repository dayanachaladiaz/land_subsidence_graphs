# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
file_path = "C:/Users/Dayana/Documents/1. PHD - done/2. Propuesta de disertacion and papers/2. LS Paper/Figure 7 modifiedX.xlsx"
data = pd.read_excel(file_path)

# Print data for debugging
print(data)

# Extract relevant columns from the dataset
X = data["X"]
X1 = data["Terzaghi"]
Min = data["Min"]
Max = data["Max"]
Min1 = data["Min1"]
Max1 = data["Max1"]
y = data["S=3e-4"]
y2 = data["Y2"]
y3 = data["Y3"]
y4 = data["Y4"]

# Plot configuration
plt.figure(figsize=(10, 6))  # Set figure size

# Add shaded region for uncertainty based on the experimental results (ribbon)
plt.fill_between(X, Max1, Min1, color='gray', alpha=0.2, label='Experiments with sensor 2')

# Plot lines for the simulated results using Terzaghi models
plt.plot(X, y, color='black', linestyle='--', marker='.', label='Terzaghi S=3e-4')
plt.plot(X, y2, color='black', linestyle='-', label='Terzaghi S=3.5e-4')

# Add labels and legend
plt.xlabel("Time (h)")
plt.ylabel("Vertical displacement (mm)")
plt.legend(loc='upper left')

# Display the plot
plt.show()
