import requests
from bs4 import BeautifulSoup
from random import choice
from tkinter.filedialog import askdirectory
from tkinter import messagebox, ttk
from tkinter import *
import threading
 
def download(url, name, file_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4389.90 Safari/531.36'
        ,
        'Cookie': '_pk_id.1.01b8=cce9862fdcfc7513.1611905452.; remember_web_59ba36add22b2f9401580f014c7f58ea4e30989d=eyJpdiI6InZJNDZBaW5hVEFyVlwvMEROQU5GcjFRPT0iLCJ2YWx1ZSI6ImJGYkFDa3lyMzBRa1V6cFdVa3oyYTg2RFwvdURrWXU2V1ZqVEM4azRRTVN0ZnBKaEpDdjBcL1pvampJSHNId290S3VQQW1PY0FsbU4xdjlkM3hhb1Y0WXJVNzJCWTZYYUxEREdrN1FCZDBmVkhmclZ4TkRoZHZaN1AzZWdsdXRsZFM0ZmpOT1wvM1wvSzNQYXUrOUpTQUVOdUpcL0ZncTYxbDRoT2EyRDNxdTVzQW53NlhiaUhqK24zTnE5cHVKQmNnWWR1IiwibWFjIjoiODE5NjdlMWMxOWE1ODVjYmQzYzQyMzUzZWU5MmMyMWNmNWUyNjU2ZWZlOTgzYzEzODA2MDQ0NTlmZmQ2ZTc3NCJ9; __cfduid=d80f535c03e3d1a3b6bb69705f60b839f1616502624; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6ImNXeUViZmlnUDdHNmM4XC9wdm1IUDdBPT0iLCJ2YWx1ZSI6IkFiSzJTd1l5Mm9Jdks0WHBmVmg0NDA3SkJ2emc4QWNsMExjbnZUdjZBSUxyMlJYWkN6T0ZpXC92SGpwem91MkE1IiwibWFjIjoiZWYyOWMyMzJjNzM1ZDdlZjQxN2Q5NmEwMzQ0ZmJmZWYzMzY0YTA3ODkxOThkZWE5NDlmOTVmZDY3NTgwYTA2YiJ9; wallhaven_session=eyJpdiI6InMzTlF1WThGWmpoZzduTEJMT2hyZHc9PSIsInZhbHVlIjoiRWpyZW9JWmw1YlZOYlZhXC9na0FPTW91Rk5NdG1ZT2tpaTlUdUpPODU4S25GTmJYN093d0Jlb0pRR3M0NnRmb1kiLCJtYWMiOiI3OGUzMmEyMjkzMzA1MmZiMWM4MmQ1NGU3MGVkZDY0M2FiOWVlMzBjYzJjNWNjNmY4MGI3YWNkZDk2N2VjYWUyIn0%3D'}
    with open('%s/%s.jpg' % (file_path, name), 'wb') as f:
        img = requests.get(url, headers=headers).content
        f.write(img)
        f.close()
 
def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4389.90 Safari/531.36'
        ,
        'Cookie': '_pk_id.1.01b8=cce9862fdcfc7513.1611905452.; remember_web_59ba36add22b2f9401580f014c7f58ea4e30989d=eyJpdiI6InZJNDZBaW5hVEFyVlwvMEROQU5GcjFRPT0iLCJ2YWx1ZSI6ImJGYkFDa3lyMzBRa1V6cFdVa3oyYTg2RFwvdURrWXU2V1ZqVEM4azRRTVN0ZnBKaEpDdjBcL1pvampJSHNId290S3VQQW1PY0FsbU4xdjlkM3hhb1Y0WXJVNzJCWTZYYUxEREdrN1FCZDBmVkhmclZ4TkRoZHZaN1AzZWdsdXRsZFM0ZmpOT1wvM1wvSzNQYXUrOUpTQUVOdUpcL0ZncTYxbDRoT2EyRDNxdTVzQW53NlhiaUhqK24zTnE5cHVKQmNnWWR1IiwibWFjIjoiODE5NjdlMWMxOWE1ODVjYmQzYzQyMzUzZWU5MmMyMWNmNWUyNjU2ZWZlOTgzYzEzODA2MDQ0NTlmZmQ2ZTc3NCJ9; __cfduid=d80f535c03e3d1a3b6bb69705f60b839f1616502624; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6ImNXeUViZmlnUDdHNmM4XC9wdm1IUDdBPT0iLCJ2YWx1ZSI6IkFiSzJTd1l5Mm9Jdks0WHBmVmg0NDA3SkJ2emc4QWNsMExjbnZUdjZBSUxyMlJYWkN6T0ZpXC92SGpwem91MkE1IiwibWFjIjoiZWYyOWMyMzJjNzM1ZDdlZjQxN2Q5NmEwMzQ0ZmJmZWYzMzY0YTA3ODkxOThkZWE5NDlmOTVmZDY3NTgwYTA2YiJ9; wallhaven_session=eyJpdiI6InMzTlF1WThGWmpoZzduTEJMT2hyZHc9PSIsInZhbHVlIjoiRWpyZW9JWmw1YlZOYlZhXC9na0FPTW91Rk5NdG1ZT2tpaTlUdUpPODU4S25GTmJYN093d0Jlb0pRR3M0NnRmb1kiLCJtYWMiOiI3OGUzMmEyMjkzMzA1MmZiMWM4MmQ1NGU3MGVkZDY0M2FiOWVlMzBjYzJjNWNjNmY4MGI3YWNkZDk2N2VjYWUyIn0%3D'}
    list_ip = ['61.145.212.31', '59.124.224.180', '117.26.41.218', '183.6.183.35', '117.65.47.142']
    proxy = choice(list_ip)
    proxies = {
        "http": "http://{}".format(proxy), "https": "https://{}".format(proxy)
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html
 
 
if __name__ == '__main__':
    root = Tk()
    root.title('wallhaven壁纸简单下载器')
    file = ['']
    Width = 350
    Height = 200
    down_numbers=0
    canvas = Canvas(root, width=Width, height=Height, highlightthickness=0, borderwidth=0)
    canvas.create_rectangle(0, 0, 550, 300, outline='yellow', fill="pink")
    canvas.place(x=0, y=0)
    root.resizable(height=False, width=False)
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (Width, Height, (screenwidth - Width) / 2, (screenheight - Height) / 2)
    root.geometry(alignstr)
    root.focus_set()
    canvas.create_text(64,48,text='网址')
    canvas.create_text(64, 88, text='要下载几页')
    e1 = Entry(root)
    e1.place(x=125, y=36)
    e2 = Entry(root)
    e2.place(x=125, y=76)
    def helpme():
        # 说明
        win2=Toplevel(root)
        win2.title('说明文档')
        width = 550
        height = 200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr2 = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        win2.geometry(alignstr2)
        win2.resizable(width=False,height=False)
        win2.focus_set()
        Help=Label(win2,text='''步骤：
1、输入wallhaven网址  不同分类下的网址 如hot部分的 https://wallhaven.cc/hot
2、输入要下载的页数
3、选择保存的文件夹后自动开始下载''',  font=('微软雅黑',10))
        Help.place(x=40,y=40)
 
    def about():
        #关于
        win2 = Toplevel(root)
        win2.title('关于')
        width = 200
        height = 200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr2 = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        win2.geometry(alignstr2)
        win2.resizable(width=False, height=False)
        win2.focus_set()
        Help = Label(win2, text='lthero制作\n\n喜欢可收藏', font=('微软雅黑',10))
        Help.place(x=70, y=60)
 
 
    # 头部菜单
    menu = Menu(root, tearoff=False)
    Cmenu = Menu(menu, tearoff=False)
    Cmenu.add_command(label='说明', command=helpme)
    Cmenu.add_separator()
    Cmenu.add_command(label='关于',command=about)
    menu.add_cascade(label='菜单', menu=Cmenu)
    root.config(menu=menu)
 
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()
 
    def get_start(temp_url, number, file_path):
        mod = '?page='
        url = [temp_url]
        if int(number) >= 2:
            url.append(temp_url)
            for i in range(2, int(number) + 1):
                url.append(temp_url + mod + str(i))
        collection = []
 
        for x in url:
            content = open_url(x)
            soup = BeautifulSoup(content, 'lxml')
            images = soup.find('section', class_="thumb-listing-page")
            for li in images.find_all('li'):
                string = str(li.a['href'])
                collection.append(string)
        count = 0
        #print(file_path)
        for i in collection:
            canvas.create_text(55, 133, text='已经下载张数 ')
            canvas.create_text(99, 133, text=count)
            name = i.split('/')[-1]
            each_url = 'https://w.wallhaven.cc/full/%s/wallhaven-%s.jpg' % (name[0:2], name)
            #print(each_url)
            download(each_url, name, file_path)
            count += 1
            canvas.create_rectangle(5, 100, 140, 240, fill="pink",outline='pink')
            #if count % 20 == 0:
                #print('下载 ', count, ' 张了')
 
 
    def choice_file():
        file[0] = askdirectory()
        messagebox.showinfo('选取成功', file[0])
        try:
            get_start(e1.get(),e2.get(),file[0])
            messagebox.showinfo('！！！！','下载完成！！！')
        except(requests.exceptions.ProxyError):
            messagebox.showinfo('到达今日下载上限')
 
    ttk.Button(root, text='选择文件夹', command=lambda: thread_it(choice_file)).place(x=150, y=120)
    root.mainloop()