import pandas as pd
df = pd.read_csv(r"C:\Users\sri\Desktop\index\sales.csv") 
print(df)
start_letter = df['product'].str.startswith('k')  
print(df[start_letter])
sum_revenue = df['revenue'].sum() 
highest_selling_product = df['quantity'].value_counts().idxmax()
print(highest_selling_product)
total_sales = df['quantity'].sum()
print(total_sales)
print(df['price'].describe())






