# Webscreenshot Api

这是一个由 selenium 驱动的 ~~高性能、高可靠、~~ 全开源的网页截图Api。  
>第一次写 Py 项目 性能和可靠性怎么样我不知道 我只知道它全开源（  

![](https://i.ibb.co/gWVg7Hq/image.png)

# 快速上手  

确保你的机子里有 Python3.7 及以上版本。  

```
    git clone git@github.com:htxzdfunny/webscreenshot-api.git
    cd webscreenshot-api
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
```

然后点击[这里](https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/#%E5%BF%AB%E9%80%9F%E5%8F%82%E8%80%83)下载你对应浏览器对应版本的驱动，把它丢进根目录下

以下示范适用Microsoft Edge ，Chrome或者其他浏览器差不多
![](https://pic1.afdiancdn.com/user/f12e34626eb511eca06352540025c377/common/faddd31e004ec323592f0f3af1280b2f_w699_h356_s9.jpg)  
![](https://pic1.afdiancdn.com/user/f12e34626eb511eca06352540025c377/common/1cc418ff5171a6a43eaf1c2a034a9dad_w361_h440_s17.jpg)  
![](https://pic1.afdiancdn.com/user/f12e34626eb511eca06352540025c377/common/1abed1e814162bde49545f012c3306ad_w842_h308_s28.jpg)  
![](https://pic1.afdiancdn.com/user/f12e34626eb511eca06352540025c377/common/4284f07be5b75f478ba12f6747c4e885_w936_h136_s15.jpg)  

 
- 启动(带命令行): `python run.py`
- 启动(不带命令行): `pythonw run.py`  

Flask将会启动在1919端口。  

> 以后再次运行记得先激活虚拟环境：`venv/Scripts/activate` 
# Api  

| 访问地址 | 功能 | 备注 |
| --- | --- | --- |
| example.com/ | 检测运行状态 | `GET`,`POST`,返回码为404
| example.com/getwebfullpic/`<url>`| 获取指定网页的截图(长截图 `headless模式`) | `GET` 可能有bug(因为这是headless模式 比如说开不了P站 下面那个非headless模式的可以)，返回为png |
| example.com/getwebpic/`<url>` | 获取屏幕截图(大小1280x720 `非headless模式`) | `GET` 没啥讲的 |

# 进阶玩法  

- 在`app.py`里你可以改服务端口和等待时间  
- 在`app.py`第22行你可以改浏览器大小  

# 最后  
特别鸣谢：[Sunset](https://github.com/chinosk114514)  
快去follow他！