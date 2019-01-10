# free_sms_twilio
Python免费发送短信，只能给验证通过的手机号码发短信。使用Flask启动了web服务，可以通过post接口调用发送短信。并且记录了接口调用日志到文件中。

## 1.准备工作

### a.申请twilio账号
twilio官网地址是: [Twilio](https://www.twilio.com/)，具体的注册过程贴一篇头条的教程：[账号申请](https://www.toutiao.com/i6643962078631559693/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1547010880&app=news_article&utm_source=weixin&iid=53865048831&utm_medium=toutiao_ios&group_id=6643962078631559693)，注意需要得到SID和Token，填入代码中

### b.安装依赖
需要安装的依赖是twilio和flask

`pip install twilio flask`

如果安装依赖比较慢，超时失败可以使用豆瓣的库(嗖嗖嗖的！)

`pip install twilio flask -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com`

## 2.启动服务

### a. windows下

`python myFlask.py`

### b. linux下

`nohup python myFlask.py &`

此时进程可以在后台挂起

### c.测试
访问 http://localhost:8090/send 即可调用到发送短信的接口
