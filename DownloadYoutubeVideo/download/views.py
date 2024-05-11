from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from pytube import *
from pytube.exceptions import RegexMatchError
# Create your views here.
def index(request):
    return render(request, 'index.html')
def getVideo(request):
    if request.method == 'POST':
        link = (request.POST.get('link')).strip()
        try:
            video = YouTube(link)
            if(video.length):
                return JsonResponse({
                    'link':link,
                    'status':200
                })
            else:
                return JsonResponse({
                'status':404,
                'message':'Không lấy được link'
                })
        except RegexMatchError:
            return JsonResponse({
                'status':404,
            'message':'Không lấy được link'
            })
    else:
        return JsonResponse({
           'status':400,
           'message':'Method sai'
        })
def Download(request):
    if request.method == 'POST':
        link = (request.POST.get('link')).strip()
        if(link):
            video = YouTube(link)
            # stream = video.streams.get_lowest_resolution()
            stream = video.streams.get_by_resolution("720p")
            stream.download()
            return JsonResponse({
                'length': video.length, #Lấy độ dài
                'title': video.title, #lấy tiêu đề
                'views': video.views, #Lấy số view
                'author': video.author, #lấy tác giả
                'link':link,
                'status':'success',
                'message':'Successfully downloaded'
            })
        else:
            return JsonResponse({
                'link': link,
                'message':'Không lấy được link khi download'
            })
    else:
        return JsonResponse({
           'status':400,
           'message':'Method sai'
        })
