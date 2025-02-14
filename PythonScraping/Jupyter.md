**숫자 형식**

```python
import requests
import pandas as pd

# API 요청 URL
url = 'https://api.huobi.de.com/market/history/kline?period=1day&size=10&symbol=btcusdt'

# 데이터 요청
response = requests.get(url)
data = response.json()

# 데이터프레임으로 변환
df = pd.DataFrame(data['data'])

# 타임스탬프를 날짜로 변환
df['date'] = pd.to_datetime(df['id'], unit='s')

# 필요한 열만 선택
df = df[['date', 'open', 'close', 'low', 'high', 'vol']]

# 데이터프레임 출력
print(df)
```

**그라프 형식**

```python
# Jupyter 노트북에서 실행할 코드
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API 요청 URL
url = 'https://api.huobi.de.com/market/history/kline?period=1day&size=100&symbol=btcusdt'

# 데이터 요청
response = requests.get(url)
data = response.json()

# 데이터프레임으로 변환
df = pd.DataFrame(data['data'])

# 타임스탬프를 날짜로 변환
df['date'] = pd.to_datetime(df['id'], unit='s')

# 필요한 열만 선택
df = df[['date', 'open', 'close', 'low', 'high', 'vol']]

# 날짜를 인덱스로 설정
df.set_index('date', inplace=True)

# 가격 시각화
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Price (USDT)')
plt.title('ETH/USDT Daily Close Prices')
plt.legend()
plt.show()

```

미래 일주일가격 추측

현재 가격표 추출 및 CSV파일 형식으로 저장

```python
import requests
import pandas as pd

# API 요청 URL
url = 'https://api.huobi.de.com/market/history/kline?period=1day&size=100&symbol=ethusdt'

# 데이터 요청
response = requests.get(url)
data = response.json()

# 데이터프레임으로 변환
df = pd.DataFrame(data['data'])

# 타임스탬프를 날짜로 변환
df['date'] = pd.to_datetime(df['id'], unit='s')

# 필요한 열만 선택
df = df[['date', 'close']]

# 데이터프레임 출력
print(df)

# 데이터프레임을 CSV 파일로 저장
df.to_csv('ethusdt_prices.csv', index=False)

```

csv파일 모델로분석 및 결과추출

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
from datetime import datetime, timedelta

# 데이터 로드
df = pd.read_csv('ethusdt_prices.csv')

# 날짜를 인덱스로 설정하고 인덱스 순서를 거꾸로 설정
df.set_index('date', inplace=True)
df = df[::-1]

# 특징과 레이블 분리
X = np.arange(len(df)).reshape(-1, 1)  # 날짜를 숫자로 변환
y = df['close'].values

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 정규화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X_train_scaled, y_train)

# 모델 저장
joblib.dump(model, 'ethusdt_linear_model.pkl')

# 미래 일주일 동안의 날짜 생성
last_date = df.index[-1]
last_date = datetime.strptime(last_date, '%Y-%m-%d %H:%M:%S')
future_dates = [last_date + timedelta(days=i) for i in range(1, 8)]

# 미래 날짜를 숫자로 변환
future_X = np.arange(len(df), len(df) + 7).reshape(-1, 1)

# 미래 데이터 정규화
future_X_scaled = scaler.transform(future_X)

# 미래 가격 예측
future_predictions = model.predict(future_X_scaled)

# 결과 출력
for date, price in zip(future_dates, future_predictions):
    print(f"Date: {date.strftime('%Y-%m-%d')}, Predicted Price: {price:.2f}")

```


