import pandas as pd

df = pd.read_excel("text.xlsx")
df["calories"][0] =df["calories"][0]+1000
df.to_excel("text2.xlsx")
print(df)