# DESCRIPTIVE STATISTICS of df
print(df.info())
print(df.describe()) # numeric columns only!!
print(df.value_counts()) # categorical data

# Visual exploratory data analysis
# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Plot the HISTOGRAM (one var)
df.population.plot("hist") # call the dataframe.column with the plot method
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
plt.show()
# Plot the BOXPLOT (one var BY another (categorical) var)
df.boxplot(column="initial_cost", by="Borough", rot=90)
plt.show()
# Plot the SCATTERPLOT (one var BY another (numerical) var)
df.plot(kind="scatter", x="initial_cost", y="total_est_fee", rot=70)
plt.show()
