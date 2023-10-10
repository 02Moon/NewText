> 爬取`同花顺`网站的股票信息
>
> 在网站中股票列表是动态网页

### 请求部分

```python
url = 'http://q.10jqka.com.cn//index/index/board/all/field/zdf/order/desc/page/{}'
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0'}
html = requests.get(url = url,headers = headers).text
```

### `HTML`字符串解析

```python
soup = BeautifulSoup(html, 'html.parser')
```

> 寻找`table`
>
> 在table中寻找所有的`tr`

```python
table = soup.find('table', {'class': 'm-table m-pager-table'})
rows = table.find_all('tr')
```

> 遍历&输出数据

```python
for row in rows:
	cells = row.find_all('td')
	if len(cells) > 0:
		code = cells[1].text.strip()
         name = cells[2].text.strip()
         price = cells[3].text.strip()
         per = cells[4].text.strip()
         print('[{}]--{}--{}元--{}%'.format(code, name, price, per))
```

### 数据保存为Excel格式

> 简单的操作

```python
from openpyxl import Workbook

# 创建一个新的 Excel 文件
wb = Workbook()

# 选择默认的工作表
ws = wb.active

# 添加表头
ws.append(['姓名', '年龄', '性别'])

# 添加数据
ws.append(['张三', 20, '男'])
ws.append(['李四', 25, '女'])
ws.append(['王五', 30, '男'])

# 保存 Excel 文件
wb.save('data.xlsx')
```

```python
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment

# 创建一个新的工作簿
wb = Workbook()

# 选择默认的工作表
ws = wb.active

# 合并三个单元格
ws.merge_cells('A1:C1')

# 在合并的单元格中插入数据
ws['A1'] = '这是合并的单元格'

# 设置单元格的对齐方式
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')

# 将工作簿保存到文件
wb.save('example.xlsx')
```

### 最后完整代码

```python
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Alignment
from datetime import date

url = 'http://q.10jqka.com.cn//index/index/board/all/field/zdf/order/desc/page/{}'
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0'}
params = { 'board': 'all', 'field': 'zdf', 'page': '1', 'order': 'desc', 'ajax': '1' }
wb = Workbook()
ws = wb.active
ws.merge_cells('A1:D1')
ws['A1'] = date.today()
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
for i in range(1,10):#当前设定为1-10页，一共263页
    html = requests.get(url = url.format(i),headers = headers).text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'm-table m-pager-table'})
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            code = cells[1].text.strip()
            name = cells[2].text.strip()
            price = cells[3].text.strip()
            per = cells[4].text.strip()
            print('[{}]--{}--{}元--{}%'.format(code, name, price, per))
            ws.append([code,name,'{}元'.format(price),'{}%'.format(per)])
wb.save('{}.xlsx'.format(date.today()))
```

#### 关于操作窗口

> 窗口运行

```python
import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title('My Window')
window.geometry('200x100')

# 运行窗口
window.mainloop()

```

> 实时时间显示

```python
import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

window = tk.Tk()
window.title('实时时间')
window.geometry('200x50')

time_label = tk.Label(window, font=('Arial', 20))
time_label.pack()

update_time()

window.mainloop()
```

> 窗口表格显示

```python
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

# 创建窗口
window = tk.Tk()

# 创建表格
table = ttk.Treeview(window, columns=("column1", "column2", "column3","column4"), show="headings")
table.pack()

# 设置表格列的标题
table.heading("column1", text="列1")
table.heading("column2", text="列2")
table.heading("column3", text="列3")
table.heading("column4", text="列4")

# table.column("column1", minwidth=0, width=tkFont.Font().measure("列1"))
# table.column("column2", minwidth=0, width=tkFont.Font().measure("列2"))
# table.column("column3", minwidth=0, width=tkFont.Font().measure("列3"))


# 添加表格数据
# table.insert("", tk.END, values=("行1-列1", "行1-列2", "行1-列3"))
# table.insert("", tk.END, values=("行2-列1", "行2-列2", "行2-列3"))
table.insert("", tk.END, text="1", values=("000001", "平安银行", "10.50", "8.20"))
table.insert("", tk.END, text="2", values=("000002", "万科A", "25.60", "12.50"))
table.insert("", tk.END, text="3", values=("000003", "中国联通", "7.80", "6.80"))

# 运行窗口
window.mainloop()

```
