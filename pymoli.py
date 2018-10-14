import pandas as pd 
import os 
import csv

file = 'purchase_data.csv'

data = pd.read_csv(file)

#   *** Total Number of Players ***
count = len(data["SN"].value_counts())
total = pd.DataFrame([count])
total_players = total.rename(columns={0:"Total Players"})
#print(total_players)

#   *** Purchasing Analysis (Total) ***

#find count of unique games
unique_items = len(data["Item ID"].value_counts())
#find total count of all prices
total_price = data["Price"].count()
#avg price
avg = data["Price"].sum() / total_price
#number of purhases
num_purchases = data["SN"].count()
#total revenue
total_rev = data["Price"].sum()

#create data tabel 
purchasing_analysis_total = pd.DataFrame({"Number of Unique Items":[unique_items],
                                          "Average Price":[avg],
                                          "Number of Purchases":[num_purchases],
                                          "Total Revenue":[total_rev]})

#purchasing_analysis_total.columns = ('Number of Unique Items','Average Price','Number of Purchases', 'Total Revenue')
print(purchasing_analysis_total)

#       *** Gender Demographics ***

#find count of male players
male = data.loc[data["Gender"] == "Male",:]
males = len(male["SN"].value_counts())
#percent
percent_male = males / total_players
#find count of female players
female = data.loc[data["Gender"] == "Female",:]
females = len(female["SN"].value_counts())
#percent
percent_female = females / total_players
#find count of Other/Non-Disclosed players
other_non_disclosed = data.loc[data["Gender"] == "Other / Non-Disclosed",:]
others = len(other_non_disclosed["SN"].value_counts())
#percent
percent_other = others / total_players

#gender demographics table
index1 = ["Male","Female","Other / Non-Disclosed"]
gender_df = pd.DataFrame ({"Total Count":[males,females,others],
                           "Percentage of Players":[percent_male,percent_female,percent_other]}, index=index1)
print(gender_df)

#   *** Purchase Analysis by Gender ***

#total purchases per catg
female_count = female["SN"].count()
male_count = male["SN"].count()
other_count = other_non_disclosed["SN"].count()

#avg purchase per catg
female_avg = female["Price"].mean()
male_avg = male["Price"].mean()
other_avg = other_non_disclosed["Price"].mean()

#total $ per catg
female_purchases = female["Price"].sum()
male_purchases = male["Price"].sum()
other_purchases = other_non_disclosed["Price"].sum()

#avg total per person
female_mean = female_purchases / females
male_mean = male_purchases / males
other_mean = other_purchases / others