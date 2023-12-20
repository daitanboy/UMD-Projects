# The program uses a titanic excel file which shows information such as how many survivors there were, passengers' sex, fares, their 
# passengerId, among other values recorded. The goal of this project was to read in a CSV of a data into a data frame object using Pandas 
# usign graphs as well.
# You have to download the titanic csv file. Once the file is uploaded 
# through VS, you can start playing around. Scatterplots, linepplots,
# histograms are some of the graphs used to describe some of the
# information from the file. 

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.getcwd()

titanic = pd.read_csv("titanic.csv") 
print(titanic)

# A few other handy methods for DataFrames
# head(), tail(), describe()
titanic.head()
titanic.tail()
titanic.describe()

###############################
# basic Matplotlib

# histogram of passengers' sex
plt.hist(titanic["Sex"])
plt.show()

# Boolean that shows passenger's age who were under 21
titanic_subset = pd.read_csv("titanic.csv", index_col ="Name")
print(titanic_subset['Age'] < 21)

# scatterplot between passengers ages and titanic fares
plt.scatter("Age", "Fare", data = titanic)
plt.show()

# lineplot between survived passengers and their respective ages
plt.plot("Survived", "Age", data = titanic)
plt.show()

# Adding a new row
new_row = {'PassengerId': '892', 'Survived': '1', 'Pclass': '2', 'Name': 'Molina, Mr. Alfred Caicedo', 'Sex': 'male', 'Age': 
         '45', 'SibSp': '3', 'Parch': '4', 'Ticket': '4267446', 'Fare': '46.3333', 'Cabin': '', 'Embarked': 'C'}

titanic_new_row = titanic.append(new_row, ignore_index=True)

print(titanic_new_row)

# I tried to add a new row to the csv file but there was a error popping up. 
# 8_2, 8_3, 8_4 Pandas Advanced topics from the checklist completed. 
# 9.1, 9.2, 9.3, 9.5 Git Advanced topic completed. 
