from django.shortcuts import render, HttpResponse
from untils import weather
# Create your views here.
def get_date(request):
    data = weather.everyday()
    note = data['note']
    content = data['content']
    dateline = data['dateline']
    picture =data['fenxiang_img']
    tts = data['tts']
    return render(request,'weather.html',{'note':note,'picture':picture,'content':content,'dateline':dateline,'tts':tts})