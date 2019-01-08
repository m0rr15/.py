
import pandas as pd
from sqlalchemy import create_engine

# CREATE engine: engine
engine = create_engine("sqlite:///Chinook.sqlite") # from specific database

# OPEN engine in context manager (so we don't have to close it)
# Perform query and save results to DataFrame: df
with engine.connect() as con: # connecting query
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6") # executing query
    df = pd.DataFrame(rs.fetchall()) #  save query as dataframe using pandas
    df.columns = rs.keys() # conserve column names


# pandas accomplishes the same on ONE line!!!
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeId >= 6", engine)



# Print the head of the DataFrame df
print(df.head())

# another SQL query with an INNER JOIN of two relational databases!!
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on \
PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000", engine)