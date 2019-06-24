import requests
import json

datas = {'access_token': '7541343adfe464d1c88788d5c98dd762'}
r3 = requests.get(url='https://api.sjtu.edu.cn/v1/me/profile',                headers={'Authorization': 'Bearer '+ datas["access_token"]},)
r3.encoding = 'utf-8'
mydatas = json.loads(r3.text)
print(r3)

