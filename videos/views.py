from django.http import HttpResponse
from django.shortcuts import render

from .models import Video

def index(request):

    video = Video.objects.order_by('-pk')[0]
    videos = Video.objects.all()

    context = {
        "videos": videos,
        "video": video
    }

    return render(request,'index.html', context)