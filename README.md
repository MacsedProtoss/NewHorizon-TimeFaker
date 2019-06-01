# NewHorizon-TimeFaker
英语视听说刷在线时长（老师要求至少4.5小时）

**使用说明**：

1. （建议使用Chrome）登陆视听说网址[(懒癌戳这里)](202.114.27.5)，登陆后进入个人中心-上网记录，获取Cookies。**注意**：其格式应为`NHCELoginCounter=*; NCCE=*; Hm_lvt_*=*; Hm_lpvt_*=*`   *' * ' 表示的是待自定义的内容*

2. 运行python程序在你的**连接了校园网**的设备上，然后在命令行的提示下粘贴你在第1步中所获取到的Cookies，回车即可开始刷时间

3. 也可以使用docker来运行，此时你应在config.py 里面填入你所获取的Cookies，然后再build容器并run it。建议使用`--restart=always`

**备注**：

- 你仍然需要挂满4.5小时才能获得4.5小时的统计时长

- 可以通过多次获取不同的Cookies以运行多个docker容器来刷多倍时间
