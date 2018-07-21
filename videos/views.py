from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from . import models
from .forms import VideoForm

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


def thanks(request):
    return render(request,'thanks.html')

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


def create_video(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VideoForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            instance = form.save(commit=False)
            instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VideoForm()

    return render(request, 'create_video.html', {'form': form})