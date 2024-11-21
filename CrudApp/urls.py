# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from StudentApp import views

# urlpatterns = [
#     url(r'^student$',views.studentApi),
#     url(r'^student$',views.studentApi),
#     url(r'^student/([0-9]+)$',views.studentApi),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, re_path  # Import re_path for regex-based routes
from StudentApp import views

urlpatterns = [
    path('student', views.studentApi),  # For routes without regex
    re_path(r'^student/([0-9]+)$', views.studentApi),  # For routes with regex
    path('admin/', admin.site.urls),
]
