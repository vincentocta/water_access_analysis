import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

#To read the three csv files that contain the data on water production, consumption, and clean water access from OpenDOSM.
df_water_production = pd.read_csv('water_production.csv')
df_water_consumption = pd.read_csv('water_consumption.csv')
df_water_access = pd.read_csv('water_access.csv')

#To check the few first rows from each dataset / dataframe to identify the data structure and the variables.
df_water_production.head()
df_water_consumption.head()
df_water_access.head()

#To convert the "date" column in each dataset from a string format to a proper datetime format.
df_water_production['date'] = pd.to_datetime(df_water_production['date'])
df_water_consumption['date'] = pd.to_datetime(df_water_consumption['date'])
df_water_access['date'] = pd.to_datetime(df_water_access['date'])

#To rename the "values" column in the datasets to distinguish the water production and water consumption values.
df_water_production = df_water_production.rename(columns={'value': 'water_production'})
df_water_consumption = df_water_consumption.rename(columns={'value': 'water_consumption'})

#To filter the datasets to include only the data from 2003 onwards as the data of year 2000 - 2003 is not available for water consumption.
df_water_production = df_water_production[df_water_production['date'].dt.year >= 2003]
df_water_consumption = df_water_consumption[df_water_consumption['date'].dt.year >= 2003]
df_water_access = df_water_access[df_water_access['date'].dt.year >= 2003]

#To check the number of rows and columns in each dataset, and identify if there is any null values in the three datasets.
df_water_production.info()
df_water_consumption.info()
df_water_access.info()

#To check the data range of each datasets to confirm that they all have been filtered and only includes data from 2003 onwards.
print(df_water_production['date'].min(), df_water_production['date'].max())
print(df_water_consumption['date'].min(), df_water_consumption['date'].max())
print(df_water_access['date'].min(), df_water_access['date'].max())

national_access = df_water_access[df_water_access['strata'] == 'overall'].groupby('date')['proportion'].mean()

national_access.plot(figsize=(12, 5), title='National average clean water access 2003–2022')
plt.ylabel('Access (%)')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

#To filter the water access dataset into only overall strata data. 
df_overall = df_water_access[df_water_access['strata'] == 'overall']

#Pivoting the dataset to have dates as index, states as columns, and the proportion as values for plotting.
state_pivot = df_overall.pivot(index='date', columns='state', values='proportion')

#To assign distinct colors to each state for better visualization in the line plot. 
colors = cm.tab20(np.linspace(0, 1, len(state_pivot.columns)))

# To create a line plot for visualization of clean water access trends in every state over the years.
fig, ax = plt.subplots(figsize=(14, 7))
for col, color in zip(state_pivot.columns, colors):
    ax.plot(state_pivot.index, state_pivot[col], 
            label=col, color=color, linewidth=1.5)

ax.set_title('Clean water access by state 2003–2022')
ax.set_ylabel('Access (%)')
ax.set_xlabel('Year')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.show()

#Using Selangor, Sabah, and Sarawak as the key states to compare their clean water access trends over the years.
key_states = ['Selangor', 'Sabah', 'Sarawak']
df_key = df_overall[df_overall['state'].isin(key_states)]
df_key_pivot = df_key.pivot(index='date', columns='state', values='proportion')
print(df_key_pivot)

#To create a table that shows the average clean water access proportion for each state across the years, sorted in ascending order.
state_avg = df_overall.groupby('state')['proportion'].mean().sort_values()
print(state_avg)

#To rank the states based on their average clean water access and visualize it using a horizontal bar chart.
fig, ax = plt.subplots(figsize=(10, 7))

colors = ['#d73027' if v < 90 else '#fee08b' 
          if v < 97 else '#1a9850' 
          for v in state_avg.values]

state_avg.plot(kind='barh', ax=ax, color=colors)

ax.axvline(x=state_avg['Malaysia'], color='black', 
           linestyle='--', linewidth=1.2, label='National average')
ax.set_xlabel('Average clean water access (%)')
ax.set_title('Average clean water access by state 2003–2022')
ax.legend()
plt.tight_layout()
plt.show()

df_states_only = df_overall[df_overall['state'] != 'Malaysia']

national_production = df_water_production.groupby('date')['water_production'].sum()

fig, ax1 = plt.subplots(figsize=(12, 5))

ax1.plot(national_production.index, national_production.values,
           color = 'blue', linewidth = 2, label='Total Water Production')
ax1.set_ylabel('Water Production (million litres/day)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
national_access = df_overall[df_overall['state'] == 'Malaysia'].set_index('date')['proportion']
ax2.plot(national_access.index, national_access.values,
        color = 'crimson', linewidth = 2, label='National Clean Water Access %')
ax2.set_ylabel('Clean Water Access (%)', color='crimson')
ax2.tick_params(axis='y', labelcolor='crimson')

ax1.set_title('National Water Production and Clean Water Access in 2003-2022')
ax1.set_xlabel('Year')
plt.tight_layout()
plt.show()

print(national_production.sort_index())

print(national_access.sort_index())