import pandas

# rows are called indices
# Passing list of lists
df1 = pandas.DataFrame([['a', 'b', 'c'], [10, 20, 30]])
print(df1)

print('\n')
# can pass column and index names if required.
# Number of labels must match number of items!
df2 = pandas.DataFrame([['a', 'b', 'c'], [10, 20, 30]], columns=['Brand', 'Type', 'Model'], index=['Name', 'Price'])
print(df2)


print('\n')
# Passing list of dictionaries
