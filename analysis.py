import pandas as pd
df = pd.read_csv(r'Desktop/index/salary.csv')
df['average salary'] = df['salary'].mean()
df['bonus amount'] = df['salary'] * df['bonus']
df['total salary'] = df['salary'] + df['bonus amount']
df['count'] = df[df['department'] == 'IT'].shape[0]
print(df)