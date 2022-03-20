import requests

context=requests.get('https://weibo.com/ajax/statuses/hot_band')  #https://is-lq.snssdk.com/api/suggest_words/?business_id=10016 今日头条热搜接口
band_list = context.json().get('data').get('band_list')
for i in range(0,50):
    print(str(i)+':'+band_list[i].get('word'))
