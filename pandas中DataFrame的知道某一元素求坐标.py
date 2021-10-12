import pandas as pd
df = pd.DataFrame({
       'BoolCol': [1, 2, 3, 3, 4],
       'attr': [22, 33, 22, 44, 66]
})
print(df)
a = df[(df.BoolCol==1)].index.tolist()
print(a)