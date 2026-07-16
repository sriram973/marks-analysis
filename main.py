import pandas as pd
df = pd.read_csv(r"C:\Users\sri\Desktop\index\students.csv")
df['total'] = df['maths'] + df['science'] + df['english']
df['average'] = df['total'] / 3
df['topper'] = df['average'].max()
print(df)