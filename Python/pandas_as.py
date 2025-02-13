import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'DOB': ['2015/05/21','2022/12/23','2012/12/11']
}

df = pd.DataFrame(data)
print(df)

for index ,row in df.iterrows():
    print(f'{index}')
    print(f"{row['Name']}")