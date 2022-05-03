from time import sleep
from flask import Flask, send_file, request
from selenium import webdriver
import io

driverPath="C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe" #浏览器驱动器路径 参阅README
waitTime=5 #打开网页后等几秒截图

options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-errors')
options.ignore_local_proxy_environment_variables()
options1=webdriver.EdgeOptions()#options1给长截图用
options1.add_argument('headless')
options1.add_argument('--ignore-certificate-errors')
options1.ignore_local_proxy_environment_variables()
webserver = Flask(__name__)



@webserver.route("/")
def hello_world():
    return ("<img src='https://http.cat/404'>",404)

@webserver.route("/getwebpic/<path:url>")# 普通截图
def getscreenshot(url):
    print("Request url:"+url)
    driver = webdriver.Edge(driverPath,options=options,)
    driver.set_window_size(1280,720) #改窗口大小改这里
    driver.get(url)
    sleep(waitTime)
    driver.save_screenshot("./temp.png")
    driver.quit()
    with open("./temp.png", "rb") as fi:
            return (send_file(
                io.BytesIO(fi.read()),
                mimetype='image/png'
            ), 200)
    
@webserver.route("/getwebfullpic/<path:url>")# 长截图
def getscreenshot2(url):
    print("Request url:"+url)
    driver = webdriver.Edge(driverPath,options=options1,)
    driver.set_window_size(1920,1080)
    driver.get(url)
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width,height)
    driver.set_window_size(width,height)
    sleep(waitTime)
    driver.save_screenshot("./temp.png")
    driver.quit()
    with open("./temp.png", "rb") as fi:
            return (send_file(
                io.BytesIO(fi.read()),
                mimetype='image/png'
            ), 200)