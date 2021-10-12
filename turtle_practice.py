# import turtle as t     # 导入turtle库
# t.shape('turtle')       #箭头变成乌龟
# t.pendown()            # 落笔
# t.forward(100)         # 划过100个单位的长度
# t.left(90)                # 左转90度
# t.forward(100)        # 划过100个单位的长度
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.penup()              # 抬笔
# t.done()               # 结束


# import turtle as t
# t.shape('turtle')
# t.pendown()
# for j in range(10):    # 重复执行10次
#     # 画正方形-开始
#     t.forward(100)         
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(100)
#     t.left(90)             # 画正方形-结束
#     t.right(36)           # 右转36度
# t.penup()
# t.done()




# t.pencolor()              # 设置画笔的颜色，可以是字符串如"green", "red",也可以是RGB 3元组。
# t.pensize()               # 设置画笔的宽度；
# t.speed()                 # 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
# t.fillcolor()               # 设置填充的颜色
# t.begin_fill()             # 开始填充
# t.end_fill()               # 结束填充


# import turtle as t
# t.shape('turtle')
# def drawsquare():        # square定义一个函数，名为 drawsqure()
#     t.pencolor('red')      # 设置画笔的颜色
#     t.speed(2)
#     t.pensize(1)
#     t.fillcolor('pink')      # 设置填充的颜色
#     t.pendown()
#     t.begin_fill()           # 开始填充

#     for i in range(10):
#         t.right(36)
#         for j in range(4):
#             t.forward(100)
#             t.left(90)
#     t.end_fill()             # 结束填充
#     t.penup()
# drawsquare()            # 调用这个函数
# t.done()




import turtle as t
def drawsquare():
    t.pendown()
    t.speed(5)
    t.pensize(1)
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.penup()
def drawsquares(clrs):
    for j in range(10):
        t.fillcolor(clrs[j])  # 从列表中选择颜色
        t.begin_fill()  # 开始填充
        drawsquare()
        t.end_fill()  # 结束填充
        t.right(36)
color_list = ['red', 'pink', 'yellow', 'gray', 'lightblue', 'ivory', 'lightcoral', 'violet',
              'moccasin', 'lightseagreen']  # 颜色列表
drawsquares(color_list)

t.done()