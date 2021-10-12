import pandas as pd
# def work_year(years,data):
#     try:
#         selected = data[data['工作经验'] <= int(years)]  # 意思是得出符合条件的数据(表格)
#         return selected
#     except ValueError:
#         print('请输入整数,并且是阿拉伯数字')
#         return ''
# 

# if __name__=='__main__':
#     data = pd.read_excel("c:\\Users\\贺志浩\\Desktop\\Python_position1.xlsx")
#     years = input('请输入工作年限(整数)')
#     good=work_year(years,data)
#     for i in range(len(good)):
#         print('**************第%s个职位**********************'%(i+1))
#         print('职位名称:',good.loc[:,'职位名称'].iloc[i])
#         print('城市:',good.loc[:,'城市'].iloc[i])
#         print('公司简称:',good.loc[:,'公司简称'].iloc[i])
#         print('学历要求:',good.loc[:,'学历要求'].iloc[i])
#         print('工资范围:%s-%s'%(good.loc[:,'薪资下限'].iloc[i],good.loc[:,'薪资上限'].iloc[i]))







# def education(edu,data):
#     options=['A','B','C','D','F']
#     if edu in options:
#         edu_level=[]
#         for i in data['学历要求']:
#             if i =='博士':
#                 edu_level.append(4)
#             elif i =='硕士':
#                 edu_level.append(3)
#             elif i =='研究生':
#                 edu_level.append(2)                
#             elif i =='本科':
#                 edu_level.append(1)
#             else:
#                 edu_level.append(0)            
#     else:
#         print('你输入学历不存在')
#     data['学历等级']=edu_level
#     try:

#         selected = data[data['学历等级'] <= int(options.index(edu))]  # 意思是得出符合条件的数据(表格)
#         return selected
#     except ValueError:
#         print('输入的选项不存在或者不是大写字母')

# if __name__=='__main__':
#     data=pd.read_excel('c:\\Users\\贺志浩\\Desktop\\Python_position1.xlsx')
#     edu= input('请输入学历选项:\nA.专科以下 \nB.大专 \nC.本科 \nD.研究生 \nE.硕士 \nF.博士 \n')
#     good=education(edu,data)
#     for i in range(len(good)):
#         print('**************第%s个职位**********************'%(i+1))
#         print('职位名称:',good.loc[:,'职位名称'].iloc[i])
#         print('城市:',good.loc[:,'城市'].iloc[i])
#         print('公司简称:',good.loc[:,'公司简称'].iloc[i])
#         print('学历要求:',good.loc[:,'学历要求'].iloc[i])
#         print('工资范围:%s-%s'%(good.loc[:,'薪资下限'].iloc[i],good.loc[:,'薪资上限'].iloc[i]))





# def work_city(city,data):
#     city.split()
#     selected=data.copy()
#     for i in range(len(data)):
#         if data.loc[i,'城市'] not in city:
#             selected=selected.drop([i])
#     return selected

# if __name__=='__main__':
#     data=pd.read_excel('c:\\Users\\贺志浩\\Desktop\\Python_position1.xlsx')
#     city=input('请输入城市,多个城市请用空格隔开')
#     good=work_city(city,data)
#     if len(good)==0:
#         print('没有找到符合预期的职位')
#     else:
#         for i in range(len(good)):
#             print('**************第%s个职位**********************'%(i+1))
#             print('职位名称:',good.loc[:,'职位名称'].iloc[i])
#             print('城市:',good.loc[:,'城市'].iloc[i])
#             print('公司简称:',good.loc[:,'公司简称'].iloc[i])
#             print('学历要求:',good.loc[:,'学历要求'].iloc[i])
#             print('工资范围:%s-%s'%(good.loc[:,'薪资下限'].iloc[i],good.loc[:,'薪资上限'].iloc[i]))



