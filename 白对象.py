import pandas as pd

filename ="C:\\Users\\贺志浩\\Downloads\\2015_2017_top5.xlsx"

# TODO：读取'2015'、'2016'、'2017'三个工作簿
df_data = pd.read_excel(filename,sheet_name=['2015','2016','2017'])
# TODO：通过describe()方法获取'2015'工作表中的数据信息的内容
data_2015=(df_data["2015"].describe())
# TODO：通过describe()方法获取'2016'工作表中的数据信息的内容
data_2016=(df_data["2016"].describe())
# TODO：通过describe()方法获取'2017'工作表中的数据信息的内容
data_2017=(df_data["2017"].describe())

# GDP_mean_2015=
print(data_2015['Economy (GDP per Capita)']['mean'])
# GDP_mean_2016=data_2016['Economy (GDP per Capita)']['mean']
# GDP_mean_2017=data_2017['Economy (GDP per Capita)']['mean']

# print(GDP_mean_2015)
# if GDP_mean_2017>GDP_mean_2016>GDP_mean_2015:
#     print("GDP越来越好了呢")
#     pass
# else:
#     print("GDP没有越来越好")
# print(GDP_mean_2015)




