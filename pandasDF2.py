import pandas as pd

df = pd.read_excel("text.xlsx")
df["calories"][0] =df["calories"][0]+1000
df.to_excel("text2.xlsx")


def style_negative(v, props=''):
    return props if v >300 else None
s2 = df.style.applymap(style_negative, props='color:red;')
html = s2.to_html()
text_file = open("index.html","w")
text_file.write(html)
text_file.close()

