
from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.index_view,name='index'),
    path('authentication/',views.sign_view,name='signup'),
    path('sign_in/',views.sign_in,name='sign_in')
]