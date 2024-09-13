from django.contrib.auth import authenticate, login


# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from classroomapp.forms import LoginForm, userloginform, courseddform, studentloginform, notificationform, \
    stdleavesheduleform, sAssignmentddform, StdntComplaintForm
from classroomapp.models import courseadd, studentadd, notificationadd, stdleaveshedule, teacherlogin, \
    addnotes, taddAsgnmnttopic, StdntComplaint, Attendance, SaddAssignments, Question


@login_required(login_url='loginview')
def student(request):
    # image=studentadd.objects.filter(user=request.user)
    # print(image)
    return render(request, 'student/dash.html')

@login_required(login_url='loginview')
def sprofileview(request):
    u = request.user
    data = studentadd.objects.filter(user=u)
    print(data)
    return render(request, 'student/profileview.html', {'data': data})

@login_required(login_url='loginview')
def sviewteachers(request):
    # data=teacherlogin.objects.all()
    data = teacherlogin.objects.filter(status=True)
    print(data)
    return render(request,'student/sviewteachers.html',{'data':data})

@login_required(login_url='loginview')
def sviewnotification(request):
    u = request.user
    data = notificationadd.objects.all()
    return render(request,'student/sviewnotification.html',{'data':data})

@login_required(login_url='loginview')
def sviewcourses(request):
    u = request.user
    data = courseadd.objects.all()
    return render(request,'student/viewcourses.html',{'data':data})

@login_required(login_url='loginview')
def sleaveshedule(request):
    form = stdleavesheduleform()
    if request.method == 'POST':
        form = stdleavesheduleform(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.name = request.user
            # leave.title=form.get('title')
            # leave.date=form.get('date')
            # leave.content=form.get('content')
            leave.save()
            return redirect('student')

    else:
        form = stdleavesheduleform()
    return render(request, 'student/sleaveshedule.html', {'form': form})


# def sleaveshedule(request):
#     form = stdleavesheduleform()
#     u = request.user
#     if request.method == 'POST':
#         form = stdleavesheduleform(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = u
#             obj.save()
#         return redirect('sleavestatus')
#     return render(request, 'student/sleaveshedule.html', {'form': form})
#
#

@login_required(login_url='loginview')
def sleavestatus(request):
    u = request.user
    data = stdleaveshedule.objects.filter(name=u)
    print(data)

    return render(request, 'student/leavestatus.html', {'data': data})


# Complaint

@login_required(login_url='loginview')
def complaint_add_student(request):
    form = StdntComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = StdntComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('complaint_studentview')
    else:
        form = StdntComplaintForm()
    return render(request, 'student/complaintadd.html', {'form': form})


@login_required(login_url='loginview')
def complaint_studentview(request):
    n = StdntComplaint.objects.filter(user=request.user)
    return render(request, 'student/viewcomplaint.html', {'complaint': n})




# Notes
@login_required(login_url='loginview')
def sviewnotes(request):
    u = request.user
    data = addnotes.objects.all()
    return render(request,'student/sviewnotes.html',{'data':data})


# Assignment
@login_required(login_url='loginview')
def sviewasgnmnttopic(request):
    u = request.user
    data = taddAsgnmnttopic.objects.all()
    return render(request,'student/sviewassignmenttopic.html',{'data':data})



@login_required(login_url='loginview')
def SaddAssignment(request):
    form = sAssignmentddform()
    u = request.user
    if request.method == 'POST':
        form = sAssignmentddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('student')
    return render(request,'student/saddassaignment.html',{'form':form})

@login_required(login_url='loginview')
def sassignmentstatus(request):
    u = request.user
    data = SaddAssignments.objects.filter(user=u)
    print(data)

    return render(request, 'student/sviewassignmentstatus.html', {'data': data})



# Attendance

@login_required(login_url='loginview')
def studentview_attendance(request):
    u = studentadd.objects.get(user=request.user)
    attendance = Attendance.objects.filter(student=u)
    return render(request, 'student/sviewattendance.html', {'data': attendance})



# EXAM
## Student View Questions

@login_required(login_url='loginview')
def take_test(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.Ans)
            print()
            if q.Ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100

        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total

        }
        # return redirect(student)
        return render(request,'student/test_result.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'student/sview_question.html',context)

