import datetime

from django.contrib.auth import authenticate, login


# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from classroomapp.forms import LoginForm, userloginform, studentloginform, tchrleavesheduleform, notesddform, \
    taddAsgnmnttopicform, TchrComplaintForm, QuestionForm
from classroomapp.models import courseadd, studentadd, notificationadd, tchrleaveshedule, stdleaveshedule, teacherlogin, \
    addnotes, SaddAssignments, Attendance, StdntComplaint, TchrComplaint, Question, Login
from classroomapp.student_views import student


def teacher(request):
    return render(request, 'teacher/dash.html')

def teacherprofileview(request):
    u = request.user
    data = teacherlogin.objects.filter(user=u)
    print(data)

    return render(request,'teacher/profileview.html',{'data':data})

def tprofileupdate(request,id):
    profile = teacherlogin.objects.get(id=id)
    form1 = userloginform(instance=profile)
    if request.method == 'POST':
        form = LoginForm(request.POST or None,instance=profile or None)
        # form1 = userloginform(request.POST or None,request.FILES,instance=profile or None)
        form1 = userloginform(request.POST or None,request.FILES,instance=profile or None)
        if form1.is_valid():
            user = form1.save(commit=True)
            user.is_teacher = True
            user.save()
        return redirect('teacherprofileview')

    return render(request,'teacher/profileupdate.html',{'form1':form1})

def tstudentregister(request):
    form = LoginForm()
    form1 = studentloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = studentloginform(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            # user.is_user = True
            user.is_student = True
            user.save()
            c = form1.save(commit=False)
            c.user = user
            c.save()
            return redirect(teacher)
    return render(request, 'teacher/addstudent.html', {'form': form, 'form1': form1})


def tviewstudents(request):
    data=studentadd.objects.all()
    print(data)
    return render(request,'teacher/tviewstudent.html',{'data':data})

def tcrstudentupdate(request,id):
    user=studentadd.objects.get(id=id)
    form=studentloginform(instance=user)
    if request.method == "POST":
        form= studentloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('tviewstudents')
    return render(request,'teacher/updatestudent.html',{'form':form})

# def tcrstudentdelete(request,id):
#     user=studentadd.objects.get(id=id)
#     user.delete()
#     return redirect('tviewstudents')

def tcrstudentdelete(request,id):
    sd=studentadd.objects.get(id=id)
    s=Login.objects.get(student=sd)
    if request.method=='POST':
        s.delete()
        messages.info(request, 'student deleted successfully')
        return redirect('tviewstudents')
    else:
        return redirect('tviewstudents')

def tviewnotification(request):
    u = request.user
    data = notificationadd.objects.all()
    return render(request,'teacher/tviewnotification.html',{'data':data})

def tviewcourses(request):
    u = request.user
    data = courseadd.objects.all()
    return render(request,'teacher/tviewcourses.html',{'data':data})

# def tchrleave(request):
#     form = tchrleavesheduleform()
#     u = request.user
#     if request.method == 'POST':
#         form = tchrleavesheduleform(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = u
#             obj.save()
#         return redirect('teacher')
#     return render(request,'teacher/tleaveschedule.html', {'form': form})

def tchrleave(request):
    form = tchrleavesheduleform()
    if request.method == 'POST':
        form = tchrleavesheduleform(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.name = request.user
            # leave.title=form.get('title')
            # leave.date=form.get('date')
            # leave.content=form.get('content')
            leave.save()
            return redirect('teacher')

    else:
        form = tchrleavesheduleform()
    return render(request, 'teacher/tleaveschedule.html', {'form': form})


def tchrleavestatus(request):
    u = request.user
    data = tchrleaveshedule.objects.filter(name=u)
    print(data)
    return render(request,'teacher/tleavestatus.html', {'data': data})

def tviewstudentleave(request):
    u = request.user
    data = stdleaveshedule.objects.all()

    return render(request,'teacher/tviewstudentleave.html',{'data':data})

# Approve student's leave
def approve_stdntleave(request,id):
    student = stdleaveshedule.objects.get(id=id)
    student.status = True
    student.status = 1
    student.save()
    messages.info(request, 'accept student leave')
    return redirect('tviewstudentleave')

# Reject student's leave
def reject_stdntleave(request, id):
    student = stdleaveshedule.objects.get(id=id)
    if request.method == 'POST':
        student.status = 2
        student.save()
        messages.info(request,'rejected student leave')
    return redirect('tviewstudentleave')

def delete_stdntleave(request,id):
    sleave = stdleaveshedule.objects.get(id=id)
    sleave.delete()
    return redirect('tviewstudentleave')


# Complaint
def complaint_stdnt(request):
    n = StdntComplaint.objects.all()
    return render(request, 'teacher/tviewstdntcomplaint.html', {'complaint': n})

def reply_stdntcomplaint(request, id):
    complaint = StdntComplaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('complaint_stdnt')
    return render(request, 'teacher/replystdntcomplaint.html', {'complaint': complaint})


def complaint_add_teacher(request):
    form = TchrComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = TchrComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('complaint_tchrview')
    else:
        form = TchrComplaintForm()
    return render(request, 'teacher/registercomplaint.html', {'form': form})



def complaint_tchrview(request):
    n = TchrComplaint.objects.filter(user=request.user)
    return render(request, 'teacher/viewselfcomplaint.html', {'complaint': n})

# Notes
def taddnotes(request):
    form = notesddform()
    u = request.user
    if request.method == 'POST':
        form = notesddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('tviewnotes')
    return render(request,'teacher/addnotes.html',{'form':form})

def tviewnotes(request):
    u = request.user
    data = addnotes.objects.filter(user=u)
    return render(request,'teacher/tviewnotes.html',{'data':data})

def tdelete_notes(request,id):
    tnotes = addnotes.objects.get(id=id)
    tnotes.delete()
    return redirect('tviewnotes')

# Assignment
def taddasnmnttopic(request):
    form = taddAsgnmnttopicform()
    u = request.user
    if request.method == 'POST':
        form = taddAsgnmnttopicform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('teacher')
    return render(request,'teacher/addassignmenttopic.html',{'form':form})


def tviewassignment(request):
    u = request.user
    data = SaddAssignments.objects.all()
    return render(request,'teacher/tviewassaignment.html',{'data':data})


def approve_assignment(request,id):
    student = SaddAssignments.objects.get(id=id)
    student.status = True
    student.status = 1
    student.save()
    messages.info(request, 'accept student assignment')
    return redirect('tviewassignment')


# Attendance

def add_attendance(request):
    name = studentadd.objects.all()
    return render(request,'teacher/addattendance.html',{'name':name})

now = datetime.datetime.now()
def mark_attendance(request,id):
    user = studentadd.objects.get(id=id)
    att=Attendance.objects.filter(student=user,date=datetime.date.today())
    if att.exists():
        messages.info(request,"Today's Attendance Already marked for this Student ")
        return redirect('add_attendance')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user,date=datetime.date.today(),attendance=attndc,time=now.time()).save()
            messages.info(request,"Attendance Added Successfully")
            return redirect('add_attendance')
    return render(request,"teacher/mark_attendance.html")

def view_attendance(request):
    value_list = Attendance.objects.values_list('date',flat=True).distinct()
    attend = {}
    for value in value_list:
        attend[value] = Attendance.objects.filter(date=value)
    return render(request,'teacher/view_attendance.html',{'attend':attend})


def view_day_attendence(request,date):
    attend=Attendance.objects.filter(date=date)

    context={
        'attend': attend,
        'date': date
    }
    return render(request,'teacher/dayattendence.html',context)


# EXAM
#Teacher add Questions

# def add_questions(request):
#
#     if request.method == 'POST':
#         question_form=QuestionForm(request.POST or None)
#         if question_form.is_valid():
#             s=question_form.save(commit=False)
#             s.save()
#             messages.info(request,'successfully')
#             return redirect(add_questions)
#     return render(request,'teacher/add_question.html',{'question_form':question_form})

#Teacher add Questions

def add_questions(request):
    form = QuestionForm()
    u = request.user
    if request.method == 'POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('question_view_techr')
    return render(request,'teacher/add_question.html',{'form':form})

# Teacher View Questions

def question_view_techr(request):
    u = request.user
    data = Question.objects.all()
    return render(request, 'teacher/tviewQuestion.html', {'data': data})

def tdelete_question(request,id):
    qustn = Question.objects.get(id=id)
    qustn.delete()
    return redirect('question_view_techr')

def tupdate_question(request,id):
    user=Question.objects.get(id=id)
    form=QuestionForm(instance=user)
    if request.method == "POST":
        form= QuestionForm(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('question_view_techr')
    return render(request,'teacher/updateQuestion.html',{'form':form})

def tview_StdntMark(request):
    u = request.user
    data = Question.objects.all()
    return render(request, 'teacher/tview_StdntMark.html', {'data': data})









