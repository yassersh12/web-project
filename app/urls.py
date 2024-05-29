
from django.urls import path
from . import views
urlpatterns = [
#    path('',views.home, name="home" ),
   path('', views.course_list, name='course_list'),
   path('register/', views.sign_up, name="register"),
   path('login/', views.user_login, name="login"),
   path('logout/', views.user_logout, name='logout'),
   path('add_course/', views.add_course, name='add_course'),
   path('courses/<str:code>/', views.course_detail, name='course_detail'),
   path('student-profile/', views.student_profile, name='student_profile'),
   path('notifications/', views.show_notifications, name='show_notifications'),
   path('enroll/<int:id>/', views.enroll_now, name='enroll_now'),

]
