import pandas as pd
df = pd.read_csv(r"C:\Users\sri\Desktop\index\employe.csv")
print(df)
print(df[df.duplicated()])
x = df.loc[4,'name'] = "jhon"
print(df)
filtered_df = df[(df['depertement'] == 'hr') & (df['age'] > 25) & (df['salary'] > 35000)]
print(filtered_df)