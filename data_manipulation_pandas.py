import pandas as pd
from fuzzywuzzy import process

df = pd.DataFrame(columns=['Division', 'Code'], data=[['Dhak', '30'], ['Chattogrram', '20']])

divisions = ['Dhaka', 'Chattogram']

for i in range(len(df)):
    division = process.extractOne(df.Division[i], divisions)[0]
    df.at[i, 'Division'] = division

print(df)
#      Division Code
# 0       Dhaka   30
# 1  Chattogram   20
