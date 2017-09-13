import pandas as pd
import numpy as np

wells = pd.read_csv('./../dat/well-data-orig.csv')
wells["FUNC"][wells.FUNC == "no"] = "No"
# Extract year from report date
wells.RPT_DATE = pd.to_datetime(wells.RPT_DATE)
wells["RPT_YEAR"] = wells.RPT_DATE.dt.year
wells.RPT_YEAR.value_counts()  # See how many records per year we have

# Select only wells with report years in [2001, 2015]
df = wells[wells.RPT_YEAR > 2000]
df = df[df.RPT_YEAR < 2016]
# Remove water source if it is rain-fed. Need to make sure there are no
# NA values for this to work
df["WATERSRC"] = df["WATERSRC"].fillna("Not recorded")
df = df[~df["WATERSRC"].str.contains("^rain", case=False)]
# There is a small set of "WATERTECH" entries that are
# rainwater collection. Get rid of these too.
df["WATERTECH"] = df["WATERTECH"].fillna("Not recorded")
df = df[~df["WATERTECH"].str.contains("^rain", case=False)]

# Write this modified data to a new CSV file.
df.to_csv('./../dat/well-data-2001-2015-no-rainwater.csv', index=False)
