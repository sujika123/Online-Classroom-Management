from django.urls import path

from classroomapp import views, admin_views, teacher_views, student_views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginview', views.loginview, name='loginview'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),


# ****************************************************************
#                                ADMIN
# ----------------------------------------------------------------

    path('adminhome', admin_views.adminhome, name='adminhome'),
    path('teacherprf', admin_views.teacherprf, name='teacherprf'),
    path('admteacherupdate/<int:id>/', admin_views.admteacherupdate, name='admteacherupdate'),
    path('admteacherdelete/<int:user_id>/', admin_views.admteacherdelete, name='admteacherdelete'),
    path('addcourse', admin_views.addcourse, name='addcourse'),
    path('viewcourses',admin_views.viewcourses,name='viewcourses'),
    path('courseupdate/<int:id>/', admin_views.courseupdate, name='courseupdate'),
    path('coursedelete/<int:id>/', admin_views.coursedelete, name='coursedelete'),

    path('studentsprf', admin_views.studentsprf, name='studentsprf'),
    path('admstudentupdate/<int:id>/', admin_views.admstudentupdate, name='admstudentupdate'),
    path('admstudentdelete/<int:id>/', admin_views.admstudentdelete, name='admstudentdelete'),
    path('addnotification', admin_views.addnotification, name='addnotification'),
    path('viewnotification', admin_views.viewnotification, name='viewnotification'),
    path('notificationupdate/<int:id>/', admin_views.notificationupdate, name='notificationupdate'),
    path('notificationdelete/<int:id>/', admin_views.notificationdelete, name='notificationdelete'),
    path('aviewteacherleave', admin_views.aviewteacherleave, name='aviewteacherleave'),
    path('approve_tchrleave/<int:id>/', admin_views.approve_tchrleave, name='approve_tchrleave'),
    path('reject_tchrleave/<int:id>/', admin_views.reject_tchrleave, name='reject_tchrleave'),
    path('delete_tchrleave/<int:id>/', admin_views.delete_tchrleave, name='delete_tchrleave'),

    path('approve_teacher/<int:id>/', admin_views.approve_teacher, name='approve_teacher'),
    path('reject_teacher/<int:id>/', admin_views.reject_teacher, name='reject_teacher'),
    path('complaint_view', admin_views.complaint_view, name='complaint_view'),
    path('reply_complaint/<int:id>/', admin_views.reply_complaint, name='reply_complaint'),
    path('stdntcomplaint_view', admin_views.stdntcomplaint_view, name='stdntcomplaint_view'),
    path('reply_studntcomplaint/<int:id>/', admin_views.reply_studntcomplaint, name='reply_studntcomplaint'),




# **********************************************************************************
#                                  TEACHER
# ----------------------------------------------------------------------------------

    path('teacher', teacher_views.teacher, name='teacher'),
    path('teacherprofileview',teacher_views.teacherprofileview,name='teacherprofileview'),
    path('tprofileupdate/<int:id>/', teacher_views.tprofileupdate, name='tprofileupdate'),
    path('tviewstudents', teacher_views.tviewstudents, name='tviewstudents'),
    path('tviewnotification', teacher_views.tviewnotification, name='tviewnotification'),
    path('tstudentregister', teacher_views.tstudentregister, name='tstudentregister'),
    path('tcrstudentupdate/<int:id>/', teacher_views.tcrstudentupdate, name='tcrstudentupdate'),
    path('tcrstudentdelete/<int:id>/', teacher_views.tcrstudentdelete, name='tcrstudentdelete'),
    path('tviewcourses', teacher_views.tviewcourses, name='tviewcourses'),
    path('tchrleave', teacher_views.tchrleave, name='tchrleave'),
    path('tchrleavestatus', teacher_views.tchrleavestatus, name='tchrleavestatus'),
    path('tviewstudentleave', teacher_views.tviewstudentleave, name='tviewstudentleave'),
    path('approve_stdntleave/<int:id>/', teacher_views.approve_stdntleave, name='approve_stdntleave'),
    path('reject_stdntleave/<int:id>/', teacher_views.reject_stdntleave, name='reject_stdntleave'),
    path('delete_stdntleave/<int:id>/', teacher_views.delete_stdntleave, name='delete_stdntleave'),
    path('complaint_stdnt', teacher_views.complaint_stdnt, name='complaint_stdnt'),
    path('reply_stdntcomplaint/<int:id>/', teacher_views.reply_stdntcomplaint, name='reply_stdntcomplaint'),
    path('complaint_add_teacher', teacher_views.complaint_add_teacher, name='complaint_add_teacher'),
    path('complaint_tchrview', teacher_views.complaint_tchrview, name='complaint_tchrview'),
    path('taddnotes', teacher_views.taddnotes, name='taddnotes'),
    path('tviewnotes', teacher_views.tviewnotes, name='tviewnotes'),
    path('tdelete_notes/<int:id>/', teacher_views.tdelete_notes, name='tdelete_notes'),
    path('taddasnmnttopic', teacher_views.taddasnmnttopic, name='taddasnmnttopic'),
    path('tviewassignment', teacher_views.tviewassignment, name='tviewassignment'),
    path('approve_assignment/<int:id>/', teacher_views.approve_assignment, name='approve_assignment'),
    path('add_attendance', teacher_views.add_attendance, name='add_attendance'),
    path('mark_attendance/<int:id>/', teacher_views.mark_attendance, name='mark_attendance'),
    path('view_attendance', teacher_views.view_attendance, name='view_attendance'),
    path('view_day_attendence/<date>/', teacher_views.view_day_attendence, name='view_day_attendence'),
    path('add_questions', teacher_views.add_questions, name='add_questions'),
    path('question_view_techr', teacher_views.question_view_techr, name='question_view_techr'),
    path('tdelete_question/<int:id>/', teacher_views.tdelete_question, name='tdelete_question'),
    path('tupdate_question/<int:id>/', teacher_views.tupdate_question, name='tupdate_question'),
    path('tview_StdntMark', teacher_views.tview_StdntMark, name='tview_StdntMark'),




# ***************************************************************************************
#                                 STUDENT
# _______________________________________________________________________________________

    path('student', student_views.student, name='student'),
    path('sprofileview', student_views.sprofileview, name='sprofileview'),
    path('sviewteachers', student_views.sviewteachers, name='sviewteachers'),
    path('sviewnotification', student_views.sviewnotification, name='sviewnotification'),
    path('sviewcourses', student_views.sviewcourses, name='sviewcourses'),
    path('sleaveshedule', student_views.sleaveshedule, name='sleaveshedule'),
    path('sleavestatus', student_views.sleavestatus, name='sleavestatus'),
    path('complaint_add_student', student_views.complaint_add_student, name='complaint_add_student'),
    path('complaint_studentview', student_views.complaint_studentview, name='complaint_studentview'),
    path('sviewnotes', student_views.sviewnotes, name='sviewnotes'),
    path('sviewasgnmnttopic', student_views.sviewasgnmnttopic, name='sviewasgnmnttopic'),
    path('SaddAssignment', student_views.SaddAssignment, name='SaddAssignment'),
    path('sassignmentstatus', student_views.sassignmentstatus, name='sassignmentstatus'),
    path('studentview_attendance', student_views.studentview_attendance, name='studentview_attendance'),
    # path('question_view_stdnt', student_views.question_view_stdnt, name='question_view_stdnt'),
    path('take_test', student_views.take_test, name='take_test'),


]