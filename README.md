# Assessing Water Supply Security Trends in Malaysia (2003-2022) and Their Implications for Reducing Future Access Loss

## Problem Statement
Malaysia produces billions of litres of water daily, yet there are over two million citizens who lack clean water access. The gap between how many litres of water are produced and the numbers that actually reach the population has widened over the 2 decades, due to aging infrastructure that loses more than a third of the processed water before it reaches the taps at homes, a persistent division of rural and urban areas where rural communities are not served well, and a state-level of water shortages that is so acute that the Kedah state recorded a zero in water reserve margin for 5 years straight. This project uses 20 years of government data on water production, water consumption, and water access to illustrate the water system failures. The records are grouped by state, sector, and date to identify where the intervention had the greatest impact on this failure. Without further analysis, the risk of water security will gradually increase as there is no exposure to how the water access fails.

## Analysis Questions
1) What are the major causes of the decline in clean water access across states in 2019?
2) What are the key factors that threaten the clean water delivery security to each state as water demand rises?
3) Which states consistently fall below the national average for clean water access, and has the gap between the best and worst performing states narrowed or widened between 2003 and 2022?
4) Is the rise in water consumption driven by population growth, production capacity, or both?

## Key Findings: The National Water Access Gap
The states’ average clean water access rates from 2003 to 2022 reveal a significant disparity, revealing a structural divide rather than a gradual inequality. The Kelantan State (64.1%), Sabah State (81.2%), and Sarawak State (89.2%) sit dramatically at the bottom of the ranking table, below the other states, clustering between 96% and 100%. The W.P. Labuan scored a perfect 100% grade for water access over the 20 years, with a 36% gap compared with the lowest-performing state, Kelantan. This finding suggests that the issue may extend beyond infrastructure failure to include policy challenges.

## Findings 1: Major Cause of Clean Water Access Decline 
The decline in clean water access from 95.6% in 2018 to 94.5% in 2020 was significantly driven by the water access loss in Sabah, which recorded a sharp drop of 12% in the same period. There are three possible compounding factors that explain these events, Sabah's non revenue water rate of approximately 50%, meaning half of the water access never have reached the consumers; a major drought that forced the shutdown of water facility in Papar after seawater had contaminated the river supply; and decades of infrastructure failure. The drop from 2018 to 2020 was not a sudden water crisis. It was an accumulated event that cost a long-term loss.

## Findings 2: Key Factors to Clean Water Delivery Failure
Between the year 2003 and 2022, the total water production in Malaysia has increased by 70% from 22,094 to 37,656 million litres per day without a single decline. Over the same 20 years, the clean water access grows by only 1.2%, from 93.7% in 2003 to 94.9% in 2022. However, there are two significant highlights, a 4.3% drop in 2007 and a 1.1% decline between 2018 and 2020 despite the increasing water production. This findings suggest that the water production is stable and gradualyl increasing, the faliure point locates in the delivery process. 

## Findings 3: The Gap Across States
Based on the rankings, 10 out of 15 states are consistently performed above the national average of 94.3% from 2003 to 2022. Terengganu sits marginally below the national average. There are 3 critically underserved states, which are Sarawak (89.2%), Sabah (81.2%), and Kelantan (64.1%). All the under performing states actually shares the same characteristics, they are either geographically remote, rural, or both. The gap between these states has not meaningfulyl closed over the 20 years, suggesting that the current existing policy and infrastructure investment has not reached the point it needs to be.

## Findings 4: Rising Gap Between Water Production and Water Consumption 
Based on the chart, the water consumption and water production are gradually increasing without a single drop. Water consumption consistently represented 60% - 65% of total production across the 20 years. This locked ratio means that consumption and water production are not casually linked to each other, both are actually driven by the population growth and increasing demand with scaling production to meet it. The remaining 35% - 40% represents water loss due to leaking pipes, water theft, and infrstructure limitations. Critically, these number of loss stayed consistent, meaning that when the water consumption and production are rising by 70%, the amount of water lost percentage are rising about the same, from a 8,745 to 14,085 million litres per day between 2003 and 2022. With this numbers, Malaysia are not fixing the leaking system, but it builds more capacity to absorb the losses.
## Dataset Description
All three datasets are obtained from the Open Data Portal of the Department of Statistics Malaysia (DOSM) at https://open.dosm.gov.my/

1. Water Production (water_production.csv)
    - Data Range: Year 2000 - 2022 (Filtered to 2003 - 2022)
    - Columns: state, date, water_production
    - Unit: Million litres per day
    - Source: OpenDOSM
2. Water Consumption (water_consumption.csv)
    - Data Range: Year 2003 - 2022
    - Columns: state, sector (domestic and non-domestic), date, water_consumption
    - Unit: Million litres per day
    - Source: OpenDOSM
3. Water Access (water_access.csv)
    - Data Range: Year 2000 - 2022 (Filtered to 2003 - 2022)
    - Columns: state, strata (overall, urban, rural), date, proportion
    - Unit: Water Access Percentage
    - Source: OpenDOSM

All three datasets were filtered to a common range of year 2003 - 2022 for a consistent data analysis.

## Tools and Libraries
### Tools Used
- Python: The primary language
- SQL: Database querying
- Power BI: For interactive dashboard

### Libraries Used
- pandas: Data cleaning and aggregation
- numpy: Colour mapping for visualization
- matplotlib: For visual graphs.

## Project Structure
