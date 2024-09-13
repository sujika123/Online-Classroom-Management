from django.contrib.auth import authenticate, login


# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from classroomapp.forms import LoginForm, userloginform, courseddform, studentloginform, notificationform
from classroomapp.models import courseadd, studentadd, notificationadd, tchrleaveshedule, teacherlogin, \
    TchrComplaint, StdntComplaint, Login


@login_required(login_url='loginview')
def adminhome(request):
    return render(request, 'Admin/dash.html')


@login_required(login_url='loginview')
def teacherprf(request):
    data=teacherlogin.objects.all()
    print(data)
    return render(request,'Admin/viewteachers.html',{'data':data})


@login_required(login_url='loginview')
def admteacherupdate(request,id):
    user=teacherlogin.objects.get(id=id)
    form=userloginform(instance=user)
    if request.method == "POST":
        form= userloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('teacherprf')
    return render(request,'Admin/teacherupdate.html',{'form':form})

# def admteacherdelete(request,id):
#     user=teacherlogin.objects.get(id=id)
#     user.delete()
#     return redirect('teacherprf')

@login_required(login_url='loginview')
def admteacherdelete(request,user_id):
    t=teacherlogin.objects.get(user_id=user_id)
    s=Login.objects.get(teacher=t)
    if request.method=='POST':
        s.delete()
        messages.info(request, 'teacher deleted successfully')
        return redirect('teacherprf')
    else:
        return redirect('teacherprf')


# Course

@login_required(login_url='loginview')
def addcourse(request):
    form = courseddform()
    u = request.user
    if request.method=='POST':
        form = courseddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewcourses')
    return render(request,'Admin/addcourses.html',{'form':form})

@login_required(login_url='loginview')
def viewcourses(request):
    u = request.user
    data = courseadd.objects.filter(user=u)
    return render(request,'Admin/viewcourses.html',{'data':data})

@login_required(login_url='loginview')
def courseupdate(request,id):
    user = courseadd.objects.get(id=id)
    form = courseddform(instance=user)
    if request.method == "POST":
        form = courseddform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewcourses')
    return render(request, 'Admin/updatecourses.html', {'form': form})


@login_required(login_url='loginview')
def coursedelete(request,id):
    data=courseadd.objects.get(id=id)
    data.delete()
    return redirect('viewcourses')


# Student

@login_required(login_url='loginview')
def studentsprf(request):
    data=studentadd.objects.all()
    print(data)
    return render(request,'Admin/viewstudent.html',{'data':data})

@login_required(login_url='loginview')
def admstudentupdate(request,id):
    user=studentadd.objects.get(id=id)
    form=studentloginform(instance=user)
    if request.method == "POST":
        form= studentloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('studentsprf')
    return render(request,'Admin/updatestudent.html',{'form':form})

# def admstudentdelete(request,id):
#     user=studentadd.objects.get(id=id)
#     user.delete()
#     return redirect('studentsprf')

@login_required(login_url='loginview')
def admstudentdelete(request,id):
    data = studentadd.objects.get(id=id)
    print(data)
    s=Login.objects.get(student=data)
    print(s)
    if request.method=='POST':
        s.delete()
        messages.info(request, 'student deleted successfully')
        return redirect('studentsprf')
    else:
        return redirect('studentsprf')


# Notification

@login_required(login_url='loginview')
def addnotification(request):
    form = notificationform()
    u = request.user
    if request.method=='POST':
        form = notificationform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewnotification')
    return render(request,'Admin/addnotification.html',{'form':form})

@login_required(login_url='loginview')
def viewnotification(request):
    u = request.user
    data = notificationadd.objects.filter(user=u)
    return render(request,'Admin/viewnotification.html',{'data':data})

@login_required(login_url='loginview')
def notificationupdate(request,id):
    user = notificationadd.objects.get(id=id)
    form = notificationform(instance=user)
    if request.method == "POST":
        form = notificationform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewnotification')
    return render(request, 'Admin/updatenotification.html', {'form': form})

@login_required(login_url='loginview')
def notificationdelete(request,id):
    data=notificationadd.objects.get(id=id)
    data.delete()
    return redirect('viewnotification')


# Leave

@login_required(login_url='loginview')
def aviewteacherleave(request):
    u = request.user
    data = tchrleaveshedule.objects.all()

    return render(request,'Admin/viewteacherleave.html',{'data':data})

@login_required(login_url='loginview')
def approve_tchrleave(request,id):
    teacher = tchrleaveshedule.objects.get(id=id)
    teacher.status = True
    teacher.status = 1
    teacher.save()
    messages.info(request, 'accept student leave')
    return redirect('aviewteacherleave')

# Reject Teacher's leave
@login_required(login_url='loginview')
def reject_tchrleave(request, id):
    teacher = tchrleaveshedule.objects.get(id=id)
    if request.method == 'POST':
        teacher.status = 2
        teacher.save()
        messages.info(request,'rejected student leave')
    return redirect('aviewteacherleave')

@login_required(login_url='loginview')
def delete_tchrleave(request,id):
    tleave = tchrleaveshedule.objects.get(id=id)
    tleave.delete()
    return redirect('aviewteacherleave')


# Approve Teacher
@login_required(login_url='loginview')
def approve_teacher(request,id):
    teacher = teacherlogin.objects.get(id=id)
    teacher.status = True
    teacher.status = 1
    teacher.save()
    messages.info(request, 'accept teacher login')
    return redirect('teacherprf')

# Reject Teacher
@login_required(login_url='loginview')
def reject_teacher(request, id):
    teacher = teacherlogin.objects.get(id=id)
    if request.method == 'POST':
        teacher.status = 2
        teacher.save()
        messages.info(request,'rejected teacher login')
    return redirect('teacherprf')


# View Complaints
@login_required(login_url='loginview')
def complaint_view(request):

    n = TchrComplaint.objects.all()
    # m = StdntComplaint.objects.all()

    return render(request, 'admin/viewcomplaints.html', {'complaint': n})

# Reply Complaints
@login_required(login_url='loginview')
def reply_complaint(request, id):
    complaint = TchrComplaint.objects.get(id=id)
    # complaint2 = StdntComplaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('complaint_view')
    return render(request, 'admin/replycomplaints.html', {'complaint': complaint})


@login_required(login_url='loginview')
def stdntcomplaint_view(request):

    # n = TchrComplaint.objects.all()
    n = StdntComplaint.objects.all()

    return render(request, 'admin/viewstdntcomplaint.html', {'complaint': n})

# Reply Complaints
@login_required(login_url='loginview')
def reply_studntcomplaint(request, id):
    complaint = StdntComplaint.objects.get(id=id)
    # complaint2 = StdntComplaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('stdntcomplaint_view')
    return render(request, 'admin/replystdntcomplaint.html', {'complaint': complaint})






