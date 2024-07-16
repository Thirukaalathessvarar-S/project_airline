from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.index_view,name='index'),
    path('authentication/',views.login_view,name='login')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)