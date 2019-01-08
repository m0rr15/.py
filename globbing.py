# You're now going to practice using the glob module to find all csv files in 
# the workspace. The ? wildcard represents any 1 character, and the * wildcard 
# represents any number of characters.
# In the next exercise, you'll programmatically load them into
# DataFrames.

# Import necessary modules
import glob
import pandas as pd
# Write the pattern: pattern
pattern = 'uber-raw-data-2014_0?.csv'
# Save all file matches: csv_files
csv_files = glob.glob(pattern)
# Print the file names
print(csv_files)
# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])
# Print the head of csv2
print(csv2.head())


# String parsing with regular expressions
# Import the regular expression module
import re
# Compile the pattern: prog
prog = re.compile('\d{3}\-\d{3}\-\d{4}') # Compiling the pattern: 
# re.compile(). notice the escapes!
# See if the pattern matches: running tests
result = prog.match('123-456-7890')
print(bool(result))
# See if the pattern matches
result2 = prog.match("1123-456-7890")
print(bool(result2))

# Extracting numerical values from strings
# Import the regular expression module
import re
# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
# Print the matches
print(matches)

# Pattern test:
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

# Simple variable-manipulations: Lambda function to the rescue!
# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))
# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])
# Print the head of tips
print(tips.head())

# Dropping duplicates
# Create the new DataFrame: tracks
tracks = billboard[["year", "artist", "track", "time"]]
# Print info of tracks
print(tracks.info())
# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()
# Print info of tracks
print(tracks_no_duplicates.info()) # simply dropping all NaNs can be problematic
# too much information is lost!

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

# Testing your data with assert statements
