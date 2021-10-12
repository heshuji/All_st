import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
path='C:\\Users\\贺志浩\\Desktop\\20210303_20210303_ACCLOG.csv'
path1="C:\\Users\\贺志浩\\Desktop\\20级21春学生返校信息统计表.csv"
data=pd.read_csv(path,encoding="gbk")#不知道为什么用gbk就可可以
le=len(data)-1
chuli_data=data[12:le]
chuli_data1=chuli_data['Unnamed: 3']#获取名字列表
chuli_data2=chuli_data['Unnamed: 4']#获取捐款列表
name_list_alpay=[]
juankuan_list_alpay=[]
for i in chuli_data1:
    j=i[3:]
    name_list_alpay.append(j)
    pass
for i in chuli_data2:
    juankuan_list_alpay.append(i)
    pass
print(name_list_alpay)
print(juankuan_list_alpay)
data1=pd.read_csv(path1,encoding='gbk')
姓名_list=[] ; 学号_list=[] ; 电话_list=[]
for i in data1[1:]['Unnamed: 2']:
    姓名_list.append(i)
    pass
for i in data1[1:]['Unnamed: 5']:
    学号_list.append(i)
    pass
for i in data1[1:]['Unnamed: 9']:
    电话_list.append(i)
    pass
school_data=pd.DataFrame({
    '姓名':姓名_list,
    '学号':学号_list,
    '电话':电话_list
})

for i in school_data['学号']:
    j=int(i[7:8])
    if j==3:
        x_site= school_data[(school_data.学号==i)].index.tolist()
        
        print(x_site)


# name=school_data[(school_data.学号==2009014319)].index.tolist()
# print(name)
    # print(type(j))

    
    # print(name)
#     xuehao_list.append(i)
# class_name_list=[]
# for j in range(len(xuehao_list)):
#     if int(xuehao_list[j][7:8])==3:
    #     class_data1=school_data.loc[j]['Unnamed: 2']
    #     class_name_list.append(class_data1)
        # print(xuehao_list[j])
        # print(school_data.loc[j]['Unnamed: 2'])
# print(class_name_list)
# print(len(xuehao_list))
# print(xuehao_list[2][7:8])
# print(school_data.loc[4])