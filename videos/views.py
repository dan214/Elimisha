from django.http import HttpResponse
from django.shortcuts import render

from . import models

def index(request):

    video = models.Video.objects.order_by('-pk')[0]
    video_list = models.Video.objects.all()
    courses = models.Course.objects.all()

    context = {
        "video_list": video_list,
        "video": video,
        "courses": courses,
        "user": request.user
    }

    return render(request,'index.html', context)


def detail(request, video_id):

    try:
        video = models.Video.objects.get(pk=video_id)
    except models.Video.DoesNotExist:
        raise Http404("Video does not exist")
    video_list = models.Video.objects.exclude(id=video_id).all().order_by('-id')[:5]
    context = {
        "video_list": video_list,
        "video": video,

    }
    return render(request,'detail.html',context)