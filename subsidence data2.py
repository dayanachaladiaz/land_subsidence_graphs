# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# # Read csv file
data = pd.read_excel("H:/Other computers/My Laptop/2. Propuesta de disertacion and papers/2. LS Paper/Simulations/Fine sand s5e-4 case 1.xlsx")
print(data)

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
data_filtered=data.groupby(['X'],as_index=False).max() 


data_filtered.plot(x='X', y='Y', kind='scatter')
plt.show()

# # Export csv
data_filtered.to_excel('H:/Other computers/My Laptop/2. Propuesta de disertacion and papers/2. LS Paper/Simulations/Fine sand s5e-4 case 12.xlsx')

