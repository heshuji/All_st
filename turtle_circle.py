import turtle as t
t.penup()                 # 抬起笔
t.goto(-150, 0)         # 到起始点
t.pensize(25)           # 设置画笔粗细
t.pencolor('green')    # 设置画笔颜色
t.left(45)                 # 画笔向左转45度
t.pendown()             # 落下画笔
t.circle(-50, 90)       # 顺时针方向画90度的弧线
t.circle(50, 90)         # 继续按逆时针方向画弧
t.circle(-50, 90)       # 顺时针方向画90度的弧线
t.circle(50, 90)         # 继续按逆时针方向画弧
t.circle(-50, 90)       # 顺时针方向画90度的弧线
t.circle(50, 90)        # 继续按逆时针方向画弧
t.circle(-50, 90)      # 顺时针方向画90度的弧线
t.circle(50, 45)        # 继续按逆时针方向画弧
t.forward(50)         # 向前走50个单位
t.circle(10, 160)      # 继续画一个160度的小弧
t.forward(8)           # 再向前伸一点
t.done()