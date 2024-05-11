from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from pytube import *
# Create your views here.
def index(request):
    return render(request, 'index.html')
def Download(request):
    link =request.POST.get('link')
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
            'message':'Không lấy được link'
        })
