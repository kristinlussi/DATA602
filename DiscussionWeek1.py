import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = "/Users/kristinlussi/Documents/MSDS/DATA602/Week10/Salary_Data.csv" # specify file path
salary_data = pd.read_csv(path)  # read csv

# 1. How do you plot a histogram in Seaborn?  

sns.histplot(salary_data['Salary'], bins=10) # histogram
plt.title('Frequency of Salaries') # title 
plt.xlabel('Salary') # x label
plt.ylabel('Frequency') # y label
plt.show() # show plot

# 2. Plot a histogram with NAs dropped.
salary_data_cleaned = salary_data.dropna() # drop nas 

sns.histplot(salary_data_cleaned['Salary'], bins=10)  # histogram
plt.title('Frequency of Salaries') # title
plt.xlabel('Salary') # x label
plt.ylabel('Frequency') # y label
plt.show() # show plot

# 3. How do you set the color for a histogram?

sns.histplot(salary_data_cleaned['Salary'], bins=10, color = "pink") # add color = "" to change the color  
plt.title('Frequency of Salaries') # title
plt.xlabel('Salary') # x label
plt.ylabel('Frequency') # y label
plt.show() # show plot


# 4.  What type of plot would allow you to compare two continuous features?  Give an example of code.
# A plot to compare two continuous features would be a scatter plot. 

sns.scatterplot(data=salary_data_cleaned, x='Salary', y='Age', color='blue') # scatter plot
plt.title('Salary vs Age') # title
plt.xlabel('Salary') # x label
plt.ylabel('Age') # y label
plt.grid(True)  # add gridlines 
plt.show() # show plot

# 5. Give example of a correlation plot.

# calculate correlation matrix
corr_matrix = salary_data_cleaned.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5) #heat map
plt.title('Correlation Plot') # title
plt.show() # show plot

# 6. Change the figure size of your plot(s).

# to change the figure size of the plot, you would use plt.figure(figsize=(_,_)))

plt.figure(figsize=(8, 6)) # change figure size
sns.scatterplot(data=salary_data_cleaned, x='Salary', y='Age', color='blue') # scatter plot
plt.title('Salary vs Age') # title
plt.xlabel('Salary') # x label
plt.ylabel('Age') # y label
plt.grid(True)  # Add gridlines 
plt.show() # show graph