import pyodide_http
pyodide_http.patch_all()
import requests
import pandas as pd
from datetime import datetime, timedelta

# 获取近一个月（约30*24=720根）1小时K线
url = "https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=720"
data = requests.get(url).json()["Data"]["Data"]
df = pd.DataFrame(data)

# 处理BOS信号
df['high_bos'] = df['high'] > df['high'].shift(1).rolling(window=5).max()
df['low_bos'] = df['low'] < df['low'].shift(1).rolling(window=5).min()

# 交易参数
initial_capital = 1000
capital = initial_capital
position = 0  # 当前持仓，1=多，-1=空，0=无
trade_log = []

for idx in df[(df['high_bos'] | df['low_bos'])].index:
    entry_row = df.loc[idx]
    entry_price = entry_row['close']
    entry_time = pd.to_datetime(entry_row['time'], unit='s')
    if idx + 3 >= len(df):  # 超出数据范围，不做交易
        continue
    exit_row = df.loc[idx+3]
    exit_price = exit_row['close']
    exit_time = pd.to_datetime(exit_row['time'], unit='s')
    # 多头
    if entry_row['high_bos']:
        profit = (exit_price - entry_price) / entry_price * capital
        capital += profit
        trade_log.append({
            "方向": "多头",
            "开仓时间": entry_time,
            "开仓价格": entry_price,
            "平仓时间": exit_time,
            "平仓价格": exit_price,
            "盈亏": profit,
            "资金": capital
        })
    # 空头
    elif entry_row['low_bos']:
        profit = (entry_price - exit_price) / entry_price * capital
        capital += profit
        trade_log.append({
            "方向": "空头",
            "开仓时间": entry_time,
            "开仓价格": entry_price,
            "平仓时间": exit_time,
            "平仓价格": exit_price,
            "盈亏": profit,
            "资金": capital
        })

# 输出结果
result_df = pd.DataFrame(trade_log)
print("初始资金: $%.2f" % initial_capital)
print("最终资金: $%.2f" % capital)
print("总收益: $%.2f" % (capital - initial_capital))
print("收益率: %.2f%%" % ((capital - initial_capital) / initial_capital * 100))
print(result_df[["方向", "开仓时间", "开仓价格", "平仓时间", "平仓价格", "盈亏", "资金"]])
