from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q



def sign_up(request):
    
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Password = request.POST['password1']
        Password2 = request.POST['password2']
        if Password == Password2:
            user=User.objects.create_user(username=Name,email=Email,password=Password)
            addst(user)
            user.save()
       
            user = auth.authenticate(request, username=Name,password=Password)
            auth.login(request,user)
            return redirect('course_list')
        else:
            return redirect("/register")
    else:
        return render(request, 'register.html')
    
def addst(user):
     Student =StudentProfile.objects.create(user=user)
     Student.save() 
        
def user_login(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Password = request.POST['password1']
        user = auth.authenticate(request, username=Name,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('course_list')
        else:
            messages.info(request,'Your username or passwword is wrong!') 
            return redirect('login')
    else:
        return render(request, 'login.html')

# logout
@login_required(login_url='/login/')
def user_logout(request):
    auth.logout(request)
    return redirect('/login')



@login_required(login_url='/login/')
def add_course(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        description = request.POST.get('description')
        instructor = request.POST.get('instructor')
        capacity = request.POST.get('capacity')
        schedule_id = request.POST.get('schedule')
        # Assuming 'schedule' is selected from a dropdown, and its value is the id of the selected schedule
        schedule = CourseSchedule.objects.get(id=schedule_id)

        course = Course.objects.create(
            code=code,
            name=name,
            description=description,
            instructor=instructor,
            capacity=capacity,
            schedule=schedule
        )
        
        return redirect('course_list')  # Redirect to home page after adding course
    else:
        # Assuming you pass the list of schedules to the template
        schedules = CourseSchedule.objects.all()
        return render(request, 'add_course.html', {'schedules': schedules})

def enroll_now(request, id):
    course = get_object_or_404(Course, id=id)
    user = User.objects.get(id=request.user.id)
    if not StudentRegistration.objects.filter(student=user, course=course).exists()  and not user.is_superuser:
        enrollment = StudentRegistration.objects.create(student=user, course=course)
        enrollment.save()
    
    return redirect('/') 

@login_required(login_url='/login/')
def course_detail(request, code):
    course = get_object_or_404(Course, code=code)
    student = request.user
    context = {
        'student': student,
        'course': course,
    }
    # if not StudentRegistration.objects.filter(student=student, course=course).exists():
    #     st = StudentRegistration.objects.create(student=student, course=course)
    #     st.save()
    return render(request, 'course_detail.html', context)

@login_required(login_url='/login/')
def course_list(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(
            Q(code__icontains=query) |
            Q(name__icontains=query) |
            Q(instructor__icontains=query)
        )
    else:
        courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


@login_required(login_url='/login/')
def student_profile(request):
    student = request.user
    registrations = StudentRegistration.objects.filter(student=student).select_related('course__schedule')
    
    context = {
        'student': student,
        'registrations': registrations,
    }
    
    return render(request, 'detail1.html', context)

@login_required(login_url='/login/')
def course_notifications(request, course_id):
    course = Course.objects.get(pk=course_id)
    notifications = course.notification_set.all()
    return render(request, 'notifications.html', {'course': course, 'notifications': notifications})
@login_required(login_url='/login/')
def show_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications.html', {'notifications': notifications})

@login_required(login_url='/login/')
def studentcourse(request, course_id):
    if request.method == 'POST':
        student = request.user
        course = get_object_or_404(Course, id=course_id)
        # Avoid creating duplicate registrations
        
        st = StudentRegistration.objects.create(student=student, course=course)
        st.save()
        return redirect('/course_list')
    else:
        # Handle the case if the request method is not POST
        return redirect('/login')