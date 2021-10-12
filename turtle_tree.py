#用递归函数实现turtle画一棵树。
import turtle as t
def branch(plist, len):  # 自定义函数，画树枝
    if len > 16:  # 递归的退出条件，树枝的长度小于16时退出
        pen_list = []  # 新画笔列表，注意，每次递归都会重新创建一个空列表
        for i in plist:
            # 遍历原画笔列表
            # 第一次进入函数时，列表中只有一支画笔，递归时（第二次进入函数），树枝有两叉，所以有两支画笔，以此类推
            i.forward(len)  # 原画笔划过树枝长度个单位
            p = i.clone()  # 克隆一支画笔
            i.left(65)  # 原画笔左转65度
            p.right(65)  # 克隆的新画笔右转65度
            pen_list.append(i)  # 将画笔 i 存入新画笔列表 pen_list
            pen_list.append(p)  # 将话题 p 存入新画笔列表 pen_list
        branch(pen_list, len * 0.65)  # 递归，pen_list为新画笔列表，树枝长为上一层的65%
# 创建原画笔
# 按照绘制树干基础部分的方法
t.penup()
t.goto(0, -200)
t.left(90)
t.pensize(7)
t.pencolor('green')
t.pendown()
original_pen_list = [t]  # 将原画笔添加到画笔列表中
branch(original_pen_list, 200)
t.done()