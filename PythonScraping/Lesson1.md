## **寻找网址所有者(WHOIS)**

------

需要安装`WHOIS`库

```markdown
pip install python-whois
```

使用该模块对域名进行查询返回核心结果

```python
import whois

prtin(whois.whois('xxxx.com'))
```





## **Urllib模块**

------

需要准备下载`Urllib`模块

```markdown
pip install urllib3
```

获取网页`HTML`信息

```python
import urllib.request

res = urllib.request.urlopen('xxxx.com')
print(res)
```

```python
from urllib import request

res = request.urlopen('xxx.com')
print(res)
```

输出`HTML`信息

```python
from urllib import request

res = request.urlopen('xxx.com')
print(res.read().decode('utf-8'))
```



### 常用方法

#### 1) urlopen()

表示向网站发起请求并获取响应对象，如下所示：

```
urllib.request.urlopen(url,timeout)
```

urlopen() 有两个参数，说明如下：

- url：表示要爬取数据的 url 地址。
- timeout：设置等待超时时间，指定时间内未得到响应则抛出超时异常。

#### 2) Request()

该方法用于创建请求对象、包装请求头，比如重构 User-Agent（即用户代理，指用户使用的浏览器）使程序更像人类的请求，而非机器。重构 User-Agent 是爬虫和反爬虫斗争的第一步。在下一节会做详细介绍。

```markdown
urllib.request.Request(url,headers)
```

参数说明如下：

- url：请求的URL地址。
- headers：重构请求头。

#### 3) html响应对象方法

```markdown
bytes = response.read() # read()返回结果为 bytes 数据类型
string = response.read().decode() # decode()将字节串转换为 string 类型
url = response.geturl() # 返回响应对象的URL地址
code = response.getcode() # 返回请求时的HTTP响应码
```

#### 4) 编码解码操作

```markdown
#字符串转换为字节码
string.encode("utf-8") 
#字节码转换为字符串
bytes.decode("utf-8") 
```





## User-Agent 用户代理

------

| 系统    | 浏览器  | User-Agent字符串                                             |
| ------- | ------- | ------------------------------------------------------------ |
| Mac     | Chrome  | Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36 |
| Mac     | Firefox | Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0 |
| Mac     | Safari  | Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15 |
| Windows | Edge    | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763 |
| Windows | IE      | Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko |
| Windows | Chrome  | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36 |
| iOS     | Chrome  | Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/31.0.1650.18 Mobile/11B554a Safari/8536.25 |
| iOS     | Safari  | Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 |
| Android | Chrome  | Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36 |
| Android | Webkit  | Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M351 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 |

#### 爬虫UA信息

```python
import urllib.request

res = urllib.request.urlopen('xxx.com')
html = res.read().decode()
print(html)
```

#### 重构UA信息

```python
from urllib import request

url = 'xxx.com'
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
print(res.read().decode('utf-8'))
```



## URL编码/解码

------

| 方法        | 说明                                          |
| ----------- | --------------------------------------------- |
| urlencode() | 该方法实现了对 url 地址的编码操作             |
| unquote()   | 该方法将编码后的 url 地址进行还原，被称为解码 |
| quote()     | 只能对字符串进行编码                          |

#### 编码

```python
from urllib import parse

print(parse.unquote('%E7%88%AC%E8%99%AB'))
```

`爬虫`

#### 解码

```python
from urllib import parse

print(parse.urlencode({'ss':'爬虫'}))
```

`ss=%E7%88%AC%E8%99%AB`

#### 案例

```python
url = 'https://www.bing.com/search?q={}'
word = input('input you want to know')
query_string = parse.quote(word)
print(url.format(query_string))
```

#### URL地址拼接方式

```python
# 1、字符串相加  
baseurl = 'http://www.baidu.com/s?'  
params='wd=%E7%88%AC%E8%99%AB'  
url = baseurl + params
# 2、字符串格式化（占位符）  
params='wd=%E7%88%AC%E8%99%AB'  
url = 'http://www.baidu.com/s?%s'% params# 
# 3、format()方法  
url = 'http://www.baidu.com/s?{}'  
params='wd=%E7%88%AC%E8%99%AB'  
url = url.format(params)
```



## 爬虫网页

------

```python
# 拼接完整URL
url = 'https://www.bing.com/search?q={}'
word = input('search you wanna know:')
encoding = parse.quote(word)
full_url = url.format(encoding)
# 向URl发送请求
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url=full_url,headers=headers)
res = request.urlopen(req)
print(res)
print(full_url)
```

#### 函数方式

```python
def get_url(word):
    url = 'https://www.bing.com/search?{}'
    params = parse.urlencode({'q':word})
    url = url.format(params)
    return url
if __name__ == '__main__':
    word = input('输入：')
    url = get_url(word)
    print(url)
```

