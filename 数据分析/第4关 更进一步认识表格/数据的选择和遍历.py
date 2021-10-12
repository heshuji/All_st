import pandas as pd
df=pd.read_csv('C:\\Users\\贺志浩\\Downloads\\autobots_output.csv')
# 列的删除
df2=df.drop(['分机号'],axis=1,inplace=True)
print(df2)
print(df)
# df中的数据没有修改,修改的是df1的数据
