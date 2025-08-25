# import pandas as pd
# cars={'Brand': ['Honda', 'Toyota', 'Ford'],
#       'Price': [22000, 25000, 27000]}
# df=pd.DataFrame(cars)
# print(df)

#Pandas Series its like 1-d Array(column in table)

# import pandas as pd
# a=[1,2,5,4,5]
# b=pd.Series(a)
# print(b)

# import pandas as pd
# a=[1,2,3,4,5]
# myvar=pd.Series(a)
# print(myvar)

# import pandas as pd
# data=pd.read_csv('data.csv')
# print(data.to_string())

#labels
# import pandas as pd
# a=[10,20,30,40]
# myvar=pd.Series(a,index=["A","B","C","D"])
# print(myvar)

# import pandas as pd
# a=["Apple","Bannana","Cat","Dog"]
# var=pd.Series(a,index=[1,2,3,4])
# print(var)

#Pandas Dataframes
# import pandas as pd
# data={
#     "Name":["Shivu","Mahesh"],
#     "Age":[20,21]
# }
# a=pd.DataFrame(data)
# print(a)
# print(a.loc[0])

# import pandas as pd
# data={
#     "Anime":["One piece","Naruto","Bleach"],
#     "Rating":[9.5,9.0,8.5]
# }
# a=pd.DataFrame(data)
# print(a)
# print(a.loc[[0,2]])

# import pandas as pd
# pd.options.display.max_rows=5
# data=pd.read_csv("data.csv")
# print(data.head(10))

# import pandas as pd
# a=pd.read_csv("data.csv")
# b=a.dropna()
# print(b.to_string())


#Pandas -Cleaning empty cells
# import pandas as pd
# data=pd.read_csv("data.csv")
# new=data.dropna()
# print(new.to_string()) #removes rows with empty cells


# import pandas as pd
# data=pd.reaqd_csv("data.csv")
# data.dropna(inplace=True)
# print(data.to_string()) #removes rows with empty cells permanently

