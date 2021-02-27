"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
##############################18
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
# from django.urls import path
############################9
from django.urls import path, include

#new imports
############################3
# from news.views import index
############################8
from news.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ############################4
#     path('news/', index,),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ############################7
#     path('news/', index,),
#     path('test/', test,),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
############################10
    path('news/', include('news.urls')),
]

# #############################17
# if settings.DEBUG:
#     urlpatterns += static

#############################19
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
