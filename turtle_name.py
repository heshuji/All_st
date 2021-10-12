import turtle as t
import math
t.shape('turtle')        # 显示出小乌龟
t.penup()                 # 抬笔，先不要画
t.goto(-250, 100)      # 移动到起始点
t.pendown()             # 落笔
t.right(60)                # 向右旋转60度
t.forward(200)          # 向前走200个单位
t.penup()                  # 抬起笔
t.goto(-150,100)        # 去往（-150，100）坐标点
t.pendown()              # 落下笔
t.right(60)                # 向右旋转60度
t.forward(200)          # 向前走200个单位长度
t.penup()             # 第一个字母"X"画完，抬笔
t.goto(-50,100)    # 前往（-50，100）坐标点
t.pendown()         # 落笔
t.left(60)             # 向左转60度
t.forward(200)     # 向前走200个单位
t.penup()             # 抬笔
t.goto(50,100)      # 去往（50，100）坐标点
t.pendown()         # 落笔
t.right(60)            # 向右旋转60度
t.forward(200)      # 向前走200各单位长度
t.penup()              # 抬笔
t.goto(250,100)     # 前往（250，100）坐标点
t.pendown()          # 落笔
t.left(30)              # 向左转30度
t.forward(100*math.sqrt(3))     # 向前走
t.right(90)            # 向右转90度
t.forward(100)      # 向前走100个单位
t.right(90)            # 向右转90度
t.forward(50)       # 向前走50个单位
t.done()