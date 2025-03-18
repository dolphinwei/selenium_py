# selenium_py
一些用selenium写的python自动化脚本

## 12306目录
12306目录下是一个12306网站的购票自动化脚本：selenium12306.py

使用前提：安装python3.8+、安装Edge以及相应驱动、安装selenium库。

使用步骤（20250318）：

1.将脚本中的一下信息补充。（13~15行）
username = ''
password = ''
id_4 = ''

2.修改代码中起始站（47、48行）、终点站（54、55行）、发车时间（62行）、列车号（75行）的信息为自己对应的信息

3.运行过程中会有验证码发送到绑定的手机号。切换到网页中，把验证码输入，然后点击确认。

4.回到IDE中的控制台，按回车键继续。

5.已经买到了票，记得支付。