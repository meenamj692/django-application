from django.shortcuts import render

# Create your views here.

# Import necessary classes
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from myapp.models import Author, Book, Course,Topic, Student
from django.shortcuts import get_object_or_404, render
from myapp.forms import TopicForm, InterestForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import send_mail
from django.views import View


# Create your views here.
# def index(request):
#     #Courses
#     courselist = Course.objects.all()[:10]
#     response = HttpResponse()
#     heading1 = '<p>' + 'List of courses: ' + '</p>'
#     response.write(heading1)
#     for course in courselist:
#         para = '<p>' + str(course) + '</p>'
#         response.write(para)
#
#     #Authors
#     authorlist = Author.objects.filter().order_by('-birthdate')[:5]
#     #response = HttpResponse()
#     heading1 = '<p>' + 'List of Authors: ' + '</p>'
#     response.write(heading1)
#     response.write(str(type(authorlist)))
#     for author in authorlist:
#         para = '<p>' + str(author) + '</p>'
#         response.write(para)
#
#     return response
#
# def about(request):
#     response = HttpResponse()
#     heading = 'This is a Course Listing APP.'
#     response.write(heading)
#     return response
#
# def detail(request, course_title):
#     response = HttpResponse()
#     heading = '<strong>Course details: <br/><br/></strong>'
#     response.write(heading)
#     #Print the course details
#     #course_list = Course.objects.filter(course_no=course_num)[0]
#     course_list = get_object_or_404(Course, title=course_title)
#     response.write('Course Number: ' + str(course_list.course_no) + '<br/>Course Title: ' + str(course_list.title)
#                    + '<br/>Book Title: ' + str(course_list.textbook.title))
#     return response
def index(View):
    courselist = Course.objects.all().order_by('title')[:10]

    if 'visit' in View.COOKIES:
        visit = View.COOKIES['visit']
        visit = int(visit)
        visit += 1
        visit = str(visit)
        response = render(View, 'myapp/index.html', {'courselist': courselist })
        response.set_cookie('counter', str(visit));
        return response
    else:
        response = render(View, 'myapp/index.html', {'courselist': courselist})
        visit = visit = str(1)
        response.set_cookie('visit', visit);
        return response

def about(request):
    return render(request,'myapp/about.html')


def detail(View,course_num):
    courselist=get_object_or_404(Course,course_no=course_num)
    return render(View,'myapp/detail.html', { 'courselist': courselist })

def topics(request):
    topiclist = Topic.objects.all()[:10]
    return render(request, 'myapp/topic.html',
{'topiclist':   topiclist})

def addtopic(request):
    topiclist = Topic.objects.all()
    if request.method=='POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses=1
            topic.save()
            return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form=TopicForm()
    return render(request, 'myapp/addtopic.html', {'form':form,
'topiclist':topiclist})

def topicdetail(request, topic_id):
    topicdetails = Topic.objects.get(id = topic_id)
    if(request.method=='POST'):
        form = InterestForm(request.POST)
        if(form.is_valid()):
            if(request.POST['interested'] == '1'):
                topicdetails.num_responses += 1;
                avg_age = (topicdetails.avg_age + int(request.POST['age']))/2
                topicdetails.avg_age = avg_age
                topicdetails.save()
        return render(request, 'myapp/topicdetail.html', {'topicdetails': topicdetails, 'form':form})
    else:
        form = InterestForm()
        return render(request, 'myapp/topicdetail.html', {'topicdetails': topicdetails, 'form':form})
def register(request):
        if(request.method == 'POST'):
            form = RegistrationForm(request.POST,request.FILES)
            if(form.is_valid()):
                student=form.save(commit=False)
                student.save()
                student.set_password(student.password)
                student.save()
                return HttpResponseRedirect(reverse('myapp:register'))

        else:
            form=RegistrationForm()
            return render(request,'myapp/Register.html',{'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))  #
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

@login_required()
def user_logout(request):
    #global user
    logout(request)
    return render(request, 'myapp/logout.html')

def mycourses(request):
    mycourselist = Course.objects.filter(students__first_name__contains=request.user)
    return render(request,'myapp/mycourses.html',{'mycourselist': mycourselist})
#def mycourses(request):

def forgotpass(request):
    email = request.POST['email']
    passwords = Student.objects.get(email= email)

    send_mail('Hey how are you ? Dont worry here is your password','Hey how are you ? Dont worry here is your password{0}'.format(passwords.password),'madhuwindsor@gmail.com',email, fail_silently=False)
    return render(request, 'myapp/forgotpass.html')