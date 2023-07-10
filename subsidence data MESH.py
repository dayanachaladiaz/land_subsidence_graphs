# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# # Read csv file
data = pd.read_excel("H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/Coarse biot 12-20 1.xlsx")
print(data)

data1 = pd.read_excel("H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/Normal biot 12-20 1.xlsx")
print(data1)

data2 = pd.read_excel("H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/Finer biot 12-20 1.xlsx")
print(data2)

data3 = pd.read_excel("H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/Extra fine biot 12-20 1.xlsx")
print(data3)

# #Adjust x
#data['X'] = data['X']

# # Filter data
#data_filtered = data.groupby(['Y'], as_index=False).max()
#print(data_filtered)

# # Plot concentration vs. time
#data_filtered.plot(x='X', y='Y', kind='scatter')
#plt.show()
#data2=data_filtered

## delete data
#data2=data.drop(data.loc[data['X']>1e11].index, inplace=True) 

##Filter again
data_filtered=data.groupby(['X'],as_index=False).min() 
data1_filtered=data1.groupby(['X'],as_index=False).min() 
data2_filtered=data2.groupby(['X'],as_index=False).min() 
data3_filtered=data3.groupby(['X'],as_index=False).min() 

data_filtered.plot(x='X', y='Y', kind='scatter')
plt.show()

data1_filtered.plot(x='X', y='Y', kind='scatter')
plt.show()

data2_filtered.plot(x='X', y='Y', kind='scatter')
plt.show()

data3_filtered.plot(x='X', y='Y', kind='scatter')
plt.show()

# # Export csv
data_filtered.to_excel('H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/Coarse biot 12-20 12.xlsx')
data1_filtered.to_excel('H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/normal biot 12-20 12.xlsx')
data2_filtered.to_excel('H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/finer biot 12-20 12.xlsx')
data3_filtered.to_excel('H:/Other computers/My Laptop/1.1. DISSERTATION/Subsidencia/Modelos/12-20 meshes/extra fine biot 12-20 12.xlsx')