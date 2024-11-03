import pandas as pd 

data = pd.read_csv('static\data\data.csv')

marks_list = data.loc[data[" Course id"] == 2001, " Marks"].tolist()


print(marks_list)