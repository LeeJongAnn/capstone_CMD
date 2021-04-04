
from django.contrib import admin
from django.urls import path,include
from Write import views

app_name = "common"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Write.urls')),
    path('common/', include('common.urls')),
    # path('',views.index,name='index')
]
