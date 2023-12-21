# 引用 requests文件
import requests

# 下载地址
download_address = 'https://cdn.jsdelivr.net/gh/sun0225SUN/sun0225SUN/assets/images/mb.png'
# 把下载地址发送给requests模块
f = requests.get(download_address)
# 下载文件
with open("xx.xxx", "wb") as code:
    code.write(f.content)
