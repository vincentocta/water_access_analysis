import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

#To read the three csv files that contain the data on water production, consumption, and clean water access from OpenDOSM.
df_water_production = pd.read_csv('water_production.csv')
df_water_consumption = pd.read_csv('water_consumption.csv')
df_water_access = pd.read_csv('water_access.csv')

#To check the few first rows from each dataset as an overview
df_water_production.head()
df_water_consumption.head()
df_water_access.head()
print(df_water_production.head())
print(df_water_consumption.head())
print(df_water_access.head())

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

#To check the date range of the data in each dataset.
print(df_water_production['date'].min(), df_water_production['date'].max())
print(df_water_consumption['date'].min(), df_water_consumption['date'].max())
print(df_water_access['date'].min(), df_water_access['date'].max())

#To check the number of rows and columns in each dataset, and identify if there is any null values in the three datasets.
df_water_production.info()
df_water_consumption.info()
df_water_access.info()

national_access_mean = df_water_access[df_water_access['strata'] == 'overall'].groupby('date')['proportion'].mean()

national_access_mean.plot(figsize=(12, 5), title='National average clean water access 2003–2022')
plt.ylabel('Access (%)')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

#To filter the water access dataset into only overall strata data. 
df_overall = df_water_access[df_water_access['strata'] == 'overall']

#Pivoting the dataset to have dates as index, states as columns, and the proportion as values for plotting.
pivot_states = df_overall.pivot(index='date', columns='state', values='proportion')

#To assign distinct colors to each state for better visualization in the line plot. 
colors = cm.tab20(np.linspace(0, 1, len(pivot_states.columns)))

# To create a line plot for visualization of clean water access trends in every state over the years.
fig, ax = plt.subplots(figsize=(14, 7))
for col, color in zip(pivot_states.columns, colors):
    ax.plot(pivot_states.index, pivot_states[col], 
            label = col, color = color, linewidth = 2)
ax.set_title('Clean water access by state 2003–2022')
ax.set_ylabel('Access (%)')
ax.set_xlabel('Year')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.show()

# Exclude the national average row to avoid double-counting in aggregations
df_states_only = df_overall[df_overall['state'] != 'Malaysia']

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

#To calculate the national water production by summing up the water production values across all states for each year.
national_production = df_water_production.groupby('date')['water_production'].sum()
fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(national_production.index, national_production.values,
           color = 'blue', linewidth = 2, label='Total Water Production')
ax1.set_ylabel('Water Production (million litres/day)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
#To create a secondary y-axis to plot the national clean water access percentage on the same graph for comparison.
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

#To calculate the growth in water production from 2003 to 2022, both in absolute terms and as a percentage.
national_production = national_production.sort_index()
growth_rate = national_production.iloc[-1] - national_production.iloc[0]
growth_percentage = ((national_production.iloc[-1] - national_production.iloc[0]) / national_production.iloc[0]) * 100
print (f"Growth in water production from 2003 to 2022: {growth_rate:,.2f} million litres/day")
print (f"Growth percentage in water production from 2003 to 2022: {growth_percentage:.2f}%")

# To create a dual-axis line plot to compare the national water production with the national water consumption over the years.
national_consumption = df_water_consumption.groupby('date')['water_consumption'].sum()
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(national_production.index, national_production.values,
        color = 'blue', linewidth = 2, label='Total Water Production')
ax.plot(national_consumption.index, national_consumption.values,
        color = 'crimson', linewidth = 2, label='Total Water Consumption')
ax.set_title('National Water Production and Consumption in 2003-2022')
ax.set_xlabel('Year')
ax.set_ylabel('Water (million litres/day)')
ax.legend()
plt.tight_layout()
plt.show()

#To create a table that compares the national water production and consumption, and the gap between them.
comparison = pd.DataFrame({
        'Production': national_production,
        'Consumption': national_consumption
        })
comparison['gap'] = comparison['Production'] - comparison['Consumption']
comparison['Consumption_per_Production'] = comparison['Consumption'] / comparison['Production'] * 100
print(comparison)

print("Summary of The Water Access Analysis")
print("-" * 40)
print(f"Date Range: {df_water_access['date'].min().date()} to {df_water_access['date'].max().date()}")
print(f"Number of Records: {len(df_water_access)}")
print(f"Average Clean Water Access (National): {national_access_mean.mean():.2f}%")
print(f"State with Highest Average Access: {state_avg.idxmax()} ({state_avg.max():.2f}%)")
print(f"State with Lowest Average Access: {state_avg.idxmin()} ({state_avg.min():.2f}%)")
print(f"Production Growth (2003-2022): {growth_percentage:.2f}%")
print(f"Access Change (2003-2022): {national_access.iloc[-1] - national_access.iloc[0]:.1f} percentage points")
print(f"Average Water Loss Ratio: {comparison['Consumption_per_Production'].mean():.2f}%")