### GPT4.1_API

```python
import requests
import json

url = "https://apihk.unifyllm.top/v1/chat/completions"

payload = json.dumps({
   "model": "gpt-4.1",
   "messages": [
      {
         "role": "system",
         "content": "You are a helpful assistant."
      },
      {
         "role": "user",
         "content": ""
      }
   ],
   "temperature": 0.6
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json',
   'Authorization': 'Bearer sk-rmBjcbguwOi8ZoOgMh0oAds7IkIn7PnEsi5u4PQHklczSyW7',
   'Accept': '*/*',
   'Host': 'apihk.unifyllm.top',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

Bearer 输入GptAPI

Free GPT_API Url

```url
https://github.com/sunsky89757/FreeGPTapi?tab=readme-ov-file
```

Jupyter显示所有输出
```Python
import pandas as pd
pd.set_option('display.max_rows', None)
print(df)
```

