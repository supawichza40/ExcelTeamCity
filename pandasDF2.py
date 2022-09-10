import pandas as pd

df = pd.read_excel("text.xlsx")
df["calories"][0] =df["calories"][0]+1000
df.to_excel("text2.xlsx")
html = df.to_html()
text_file = open("index.html","w")
text_file.write(html)
text_file.close()
print(df)