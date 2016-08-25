import pandas

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

# # rows are called indices
# # Passing list of lists
# df1 = pandas.DataFrame([['a', 'b', 'c'], [10, 20, 30]])
# print(df1)
# print(type(df1))
#
# print('\n')
# # can pass column and index names if required.
# # Number of labels must match number of items!
# df2 = pandas.DataFrame([['a', 'b', 'c'], [10, 20, 30]], columns=['Brand', 'Type', 'Model'], index=['Name', 'Price'])
# print(df2)

print('\n')
# Passing list of dictionaries
# Can accept missing fields, will print "NaN"
# Arranges columns in alphabetic order
df3 = pandas.DataFrame([{'Name': 'John', 'Surname': 'Smith', 'Age': 35, 'Height': 172},
                        {'Name': 'Bob', 'Age': 12, 'Height': 152},
                        {'Name': 'Mark', 'Surname': 'Fob', 'Age': 29, 'Height': 190}])
print(df3, '\n')

# Data Analysis Basics

# some dictionary methods
print(df3.keys())
print(df3.values)

# statistics
print(df3.mean())  # prints mean of each column with numbers
print()
print(df3.mean().mean())  # prints mean of all columns with numbers

# other
print(df3.head(2), '\n')  # same as head in Linux, print x amount of rows from the top
print(df3.tail(1), '\n')  # print x amount of rows from the botton
