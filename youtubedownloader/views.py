from django.shortcuts import render
from pytube import YouTube
import os.path
from django.contrib import messages


url = ''


def index(request):
    if request.method == 'POST':
        global url
        url = request.POST.get('url')
        youtube = YouTube(url)
        streams = youtube.streams.all()
        title = youtube.title
        thumb = youtube.thumbnail_url
        resolutions = []
        for i in streams:
            if i.resolution is not None:
                resolutions.append(i.resolution)
            else:
                resolutions.append('Audio')
        resolutions = list(dict.fromkeys(resolutions))

        return render(request, 'index.html', {'rsl': resolutions, 'thumb': thumb, 'title': title})
    else:
        return render(request, 'index.html')


def download(request, res):
    if request.method == 'POST':
        homedir = os.path.expanduser('~')
        youtube = YouTube(url)
        youtube.streams.filter(res=res).first().download(homedir + '/Downloads')
        messages.success(request, 'Video downloaded. Thanks for using our website')
        return render(request, 'index.html', {'messages': messages})
    else:
        return render(request, 'index.html')