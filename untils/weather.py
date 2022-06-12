import requests
# http://open.iciba.com/dsapi/ 每日一句
def everyday():
    url='http://open.iciba.com/dsapi/'
    url_date = 'http://open.iciba.com/dsapi/?date=2022-01-11'
    url2='http://wthrcdn.etouch.cn/weather_mini?city=%E8%A5%BF%E5%AE%89'
    context=requests.get(url)
    return context.json()

url='http://open.iciba.com/dsapi/?date=2022-06-09'
url2='http://wthrcdn.etouch.cn/weather_mini?city=%E8%A5%BF%E5%AE%89'
context=requests.get(url)
print(context.json())