from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from classroomapp.forms import LoginForm, userloginform, courseddform, studentloginform, notificationform, stdleavesheduleform
from classroomapp.models import courseadd,teacherlogin, studentadd, notificationadd, stdleaveshedule


def home(request):
    return render(request, 'index.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
             login(request, user)
             return redirect('adminhome')

        if user is not None and user.is_teacher:
            if user.teacher.status == True:

                login(request, user)
                return redirect('teacher')

        if user is not None and user.is_student:
            login(request, user)
            # print('hai')
            return redirect('student')
        else:
            messages.info(request, 'Invalid Credentials')

            # elif user.is_teacher:
            #     if user.teacher.status==True:
            #         login(request, user)
            #         return redirect('teacher')
            # elif user.is_student:
            #     login(request, user)
            #     print('hai')
            #     return redirect('student')
            #
            # else:
            #     messages.info(request, 'Invalid Credentials')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('loginview')

def register(request):
    form = LoginForm()
    form1 = userloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = userloginform(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = form1.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect(loginview)
    return render(request, 'registration.html', {'form': form, 'form1': form1})



# ************************************************************************


