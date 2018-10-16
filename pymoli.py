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

#create data table
purchasing_analysis_total = pd.DataFrame({"Number of Unique Items":[unique_items],
                                          "Average Price":[avg],
                                          "Number of Purchases":[num_purchases],
                                          "Total Revenue":[total_rev]})

purchasing_analysis_total["Average Price"] = purchasing_analysis_total["Average Price"].map("${:.2f}".format)
purchasing_analysis_total["Total Revenue"] = purchasing_analysis_total["Total Revenue"].map("${:,.2f}".format)

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

index2 = ["Male","Female","Other / Non-Disclosed"]
pur_analysis_by_gender = pd.DataFrame ({" ":" ",
                                        "Purchase Count":[female_count,male_count,other_count],
                                        "Average Purchase Price":[female_avg,male_avg,other_avg],
                                        "Total Purchase Value":[female_purchases,male_purchases,other_purchases],
                                        "Avg Total Purchase per Person":[female_mean,male_mean,other_mean]},index = index1)

pur_analysis_by_gender["Average Purchase Price"] = pur_analysis_by_gender["Average Purchase Price"].map("${:.2f}".format)
pur_analysis_by_gender["Avg Total Purchase per Person"] = pur_analysis_by_gender["Avg Total Purchase per Person"].map("${:.2f}".format)
pur_analysis_by_gender.index.names = ["Gender"]

print(pur_analysis_by_gender)

#   *** Age Demographics ***
 
bins = [0,10,14,19,24,29,34,39,100]
groups = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

data["Total Count"] = pd.cut(data["Age"], bins, labels=groups)

data.groupby("Total Count")
#obtain counts for each age range
agedata = data["Total Count"].value_counts()
age = pd.DataFrame (agedata)
#sort index 
age.sort_index(inplace=True)

#format percent to two decimal places
age["Percent"] = age["Percent"].map("{:.2f}".format)

age["Percent"] = (age["Total Count"] / (age["Total Count"].sum()) ) * 100

print(age)



#   *** Purchasing Analysis (Age) ***

#df["Test Score Summary"] = pd.cut(df["Test Score"], bins,
 
bins = [0,9,14,19,24,29,34,39,200]
groups = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

unique_sn["Total Count"] = pd.cut(data["Age"], bins, labels=groups)

age_data = pd.DataFrame(unique_sn["Total Count"].value_counts())

age_data["percent"] = age_data["Total Count"] / age_data["Total Count"].sum() * 100
age_data["percent"] = age_data["percent"].map("% {:.2f}".format)

age_data.sort_index()