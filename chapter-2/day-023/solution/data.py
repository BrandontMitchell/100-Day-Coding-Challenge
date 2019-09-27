import pandas as pd

# Two primary components of pandas are Series and DataFrames
# Multiple series make up a dataframe

data = {
    'apples': [1, 3, 4, 1, 3, 2, 2],
    'bananas': [2, 2, 5, 2, 1, 1, 7],
    'squash': [3, 0, 0, 0, 1, 0, 8]
}

purchases = pd.DataFrame(data)
print(data) # lets see the difference between raw data and a dataframe

# We can specify the indexes or columns in our data
purchases = pd.DataFrame(data, index=['Brandon', 'Fadel', 'Jin', 'john', 'johnson', 'erik', 'maksim'])
print(purchases)

# We can locate specified indexes called querying an item
print(purchases.loc['Jin'])

# Convert to different formats
purchases.to_csv("data.csv")
purchases.to_json("data.json")

# can also convert to sql, but we don't have a db setup to do so


# viewing our data
baby_names = pd.read_csv("Popular_Baby_Names.csv", index_col=0)
print(baby_names.head())    # outputs first 5 rows in data set
print(baby_names.tail())    # outputs last 5 rows in data set

# check if we have any null values
print(baby_names.isnull())
print(baby_names.isnull().sum())        #great! no null values in our data set

names = baby_names['Child\'s First Name']
print(names.head(10))


print(df.iloc[0])
print(df.head(5))


# lets locate if your name is in the popular name list
name = df["Child\'s First Name"]=="Brandon"
print(df.where(name, inplace=True))

#returned none for me :( guess im unique ;))
