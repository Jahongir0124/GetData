import requests
import json

x = requests.get('http://127.0.0.1:8000/serviceTime/?branchId=1&startDate=2022/07/01&endDate=2022/07/10')


print(type(x.json()))
# for i in x.json():
# 	for d in i['Datas']:
# 		print(d['Date'],d['Average_Service'],d['AverageWaitngTime'],d['Quenetity'])