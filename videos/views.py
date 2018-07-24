from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


from . import models
from .forms import VideoForm,StudentForm, UserForm, SignUpForm

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

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = StudentForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/thanks/')

    else:
        user_form = SignUpForm(instance=request.user)
        profile_form = StudentForm(instance=request.user.userprofile)
    return render(request, 'register_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student_form.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/thanks/')
    else:
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
    return render(request, 'register_user.html', {'user_form': user_form,'student_form': student_form})


