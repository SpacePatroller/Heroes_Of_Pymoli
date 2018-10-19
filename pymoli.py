import pandas as pd 
import os 
import csv

file = 'purchase_data.csv'

data = pd.read_csv(file)

#   *** Total Number of Players ***
count = len(data["SN"].value_counts())
total = pd.DataFrame([count])
total_players = total.rename(columns={0:"Total Players"})
print("Total Players")
print(total_players)

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
print("Purchasing Analysis Total")
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
print("Gender Demographics")
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
print("Purchase Analysis by Gender")
print(pur_analysis_by_gender)

#   *** Age Demographics ***
 
data_parsed = data.drop_duplicates("SN")

bins = [0,9,14,19,24,29,34,39,200]
groups = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

data_parsed["Total Count"] = pd.cut(data_parsed["Age"], bins, labels=groups)

age_data = pd.DataFrame(data_parsed["Total Count"].value_counts())

age_data["Percent"] = age_data["Total Count"] / age_data["Total Count"].sum() * 100
age_data["Percent"] = age_data["Percent"].map("% {:.2f}".format)

age_data.sort_index()
print("Age Demographics")
print(age_data)


#   *** Purchasing Analysis (Age) ***


data["Total Count"] = pd.cut(data["Age"], bins, labels=groups)
byage = pd.DataFrame(data["Total Count"].value_counts())
byage = byage.reset_index()


lessthen_ten = data.loc[data["Age"] < 10,:]
first = lessthen_ten["Price"].sum() / lessthen_ten["Price"].count()

lessthen_fourteen = data.loc[(data["Age"] <= 14) & (data["Age"] >= 10)]
second = lessthen_fourteen["Price"].sum() / lessthen_fourteen["Price"].count()

lessthen_nineteen = data.loc[(data["Age"] <= 19) & (data["Age"] >= 15)]
third = lessthen_nineteen["Price"].sum() / lessthen_nineteen["Price"].count()

lessthen_twentyfour = data.loc[(data["Age"] <= 24) & (data["Age"] >= 20)]
fourth = lessthen_twentyfour["Price"].sum() / lessthen_twentyfour["Price"].count()

lessthen_twentynine = data.loc[(data["Age"] <= 29) & (data["Age"] >= 25)]
fifth = lessthen_twentynine["Price"].sum() / lessthen_twentynine["Price"].count()


lessthen_thirtyfour = data.loc[(data["Age"] <= 34) & (data["Age"] >= 30)]
sixth = lessthen_thirtyfour["Price"].sum() / lessthen_thirtyfour["Price"].count()

lessthen_thirtynine = data.loc[(data["Age"] <= 39) & (data["Age"] >= 35)]
seventh = lessthen_thirtynine["Price"].sum() / lessthen_thirtynine["Price"].count()

lessthen_forty = data.loc[data["Age"] >=40]
eight = lessthen_forty["Price"].sum() / lessthen_forty["Price"].count()

avp = pd.DataFrame({"Average Purchase Price":[first,second,third,fourth,fifth,sixth,seventh,eight]})
#avp = pd.Series([first,second,third,fourth,fifth,sixth,seventh])
avp["Average Purchase Price"] = avp["Average Purchase Price"].map("% {:.2f}".format)

tester = pd.concat([byage,avp], axis=1)

#Total Purchase Value
lessthen_ten = data.loc[data["Age"] < 10,:]
one = lessthen_ten["Price"].sum()

lessthen_fourteen = data.loc[(data["Age"] <= 14) & (data["Age"] >= 10)]
two = lessthen_fourteen["Price"].sum() 

lessthen_nineteen = data.loc[(data["Age"] <= 19) & (data["Age"] >= 15)]
three = lessthen_nineteen["Price"].sum()

lessthen_twentyfour = data.loc[(data["Age"] <= 24) & (data["Age"] >= 20)]
four = lessthen_twentyfour["Price"].sum()

lessthen_twentynine = data.loc[(data["Age"] <= 29) & (data["Age"] >= 25)]
five = lessthen_twentynine["Price"].sum() 


lessthen_thirtyfour = data.loc[(data["Age"] <= 34) & (data["Age"] >= 30)]
six = lessthen_thirtyfour["Price"].sum()

lessthen_thirtynine = data.loc[(data["Age"] <= 39) & (data["Age"] >= 35)]
seven = lessthen_thirtynine["Price"].sum() 

lessthen_forty = data.loc[data["Age"] >=40]
aight = lessthen_forty["Price"].sum() 

tpv = pd.DataFrame({"Total Purchase Price":[one,two,three,four,five,six,seven,aight]})
tpv["Total Purchase Price"] = tpv["Total Purchase Price"].map("$ {:.2f}".format)

tested = pd.concat([tester,tpv], axis=1)

#Avg Total Purchase per Person
lessthen_ten = data.loc[data["Age"] < 10,:]
one = lessthen_ten["Price"].sum() / len(lessthen_ten["SN"].value_counts())

lessthen_fourteen = data.loc[(data["Age"] <= 14) & (data["Age"] >= 10)]
two = lessthen_fourteen["Price"].sum() / len(lessthen_fourteen["SN"].value_counts())

lessthen_nineteen = data.loc[(data["Age"] <= 19) & (data["Age"] >= 15)]
three = lessthen_nineteen["Price"].sum() / len(lessthen_nineteen["SN"].value_counts())

lessthen_twentyfour = data.loc[(data["Age"] <= 24) & (data["Age"] >= 20)]
four = lessthen_twentyfour["Price"].sum() / len(lessthen_twentyfour["SN"].value_counts())

lessthen_twentynine = data.loc[(data["Age"] <= 29) & (data["Age"] >= 25)]
five = lessthen_twentynine["Price"].sum() / len(lessthen_twentynine["SN"].value_counts())


lessthen_thirtyfour = data.loc[(data["Age"] <= 34) & (data["Age"] >= 30)]
six = lessthen_thirtyfour["Price"].sum() / len(lessthen_thirtyfour["SN"].value_counts())

lessthen_thirtynine = data.loc[(data["Age"] <= 39) & (data["Age"] >= 35)]
seven = lessthen_thirtynine["Price"].sum() / len(lessthen_thirtynine["SN"].value_counts())

lessthen_forty = data.loc[data["Age"] >=40]
aight = lessthen_forty["Price"].sum() / len(lessthen_forty["SN"].value_counts())

atpp = pd.DataFrame({"Avg Total Purchase per Person":[one,two,three,four,five,six,seven,aight]})
atpp["Avg Total Purchase per Person"] = atpp["Avg Total Purchase per Person"].map("$ {:.2f}".format)

Pur_Analysis_Age = pd.concat([tested,atpp], axis=1)
Pur_Analysis_Age.rename(columns = {'index':'Age_Range'})
Pur_Analysis_Age = pd.concat([tested,atpp], axis=1)

Pur_Analysis_Age = Pur_Analysis_Age.rename(index=str, columns={"index": "Age Range"})
print("Purchasing Analysis Age")
print(Pur_Analysis_Age)

#   *** Top Spenders ****

purchases = pd.DataFrame(data["SN"].value_counts())
purchases = purchases.iloc[0:5]
#purchases

#Average Purchase Price
one = data.loc[data["SN"] == 'Lisosia93',["Price"]]
ones = one["Price"].sum() / one["Price"].count()

two = data.loc[data["SN"] == 'Iral74',["Price"]]
twos = two["Price"].sum() / two["Price"].count()

three = data.loc[data["SN"] == 'Idastidru52',["Price"]]
threes = three["Price"].sum() / three["Price"].count()

four = data.loc[data["SN"] == 'Chamjask73',["Price"]]
fours = four["Price"].sum() / four["Price"].count()

five = data.loc[data["SN"] == 'Ialallo29',["Price"]]
fives = five["Price"].sum() / five["Price"].count()

avps = pd.DataFrame({"Average Purchase Price":[ones,twos,threes,fours,fives]})
avps["Average Purchase Price"] = avps["Average Purchase Price"].map("$ {:.2f}".format)

avp3 = pd.concat([purchases,avps], axis=1)
#avp3

#Average Purchase Price / #Total Purchase Value
one = data.loc[data["SN"] == 'Lisosia93',["Price"]]
ones = one["Price"].sum() / one["Price"].count()
onest = one["Price"].sum()

two = data.loc[data["SN"] == 'Iral74',["Price"]]
twos = two["Price"].sum() / two["Price"].count()
twost = two["Price"].sum() 

three = data.loc[data["SN"] == 'Idastidru52',["Price"]]
threes = three["Price"].sum() / three["Price"].count()
threest = two["Price"].sum() 

four = data.loc[data["SN"] == 'Chamjask73',["Price"]]
fours = four["Price"].sum() / four["Price"].count()
fourst = two["Price"].sum() 

five = data.loc[data["SN"] == 'Ialallo29',["Price"]]
fives = five["Price"].sum() / five["Price"].count()
fivet = two["Price"].sum() 

avps = pd.DataFrame({"Average Purchase Price":[ones,twos,threes,fours,fives]})
avps["Average Purchase Price"] = avps["Average Purchase Price"].map("$ {:.2f}".format)
avp3 = pd.concat([purchases,avps], axis=1)

avpt = pd.DataFrame({"Total Purchase Values":[onest,twost,threest,fourst,fivet]})
avpt["Total Purchase Values"] = avpt["Total Purchase Values"].map("$ {:.2f}".format)
avp4 = pd.concat([avp3,avpt], axis=1)
avp4 = avp4.rename(index=str, columns={"index": "Name"})

avp4.set_index("Name")

print("Top Spenders")
print("avp4")
