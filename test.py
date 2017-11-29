import requests
import re
# 练习requests库的使用

url = 'https://kyfw.12306.cn/otn/resources/js/framework/favorite_name.js'

data = requests.get(url,verify = False)
partten = r'([\u4e00-\u9fa5]+)\|([A-Z]+)'
output = re.findall(partten, data.text)
print(output)
print(type(output))

dict1={'zhang':'张家辉','wang':'王宝强','li':'李冰冰','zhao':'赵薇'}
print(dict1.get('zhang'))
# print (data.text)
