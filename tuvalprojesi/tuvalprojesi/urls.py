"""
URL configuration for tuvalprojesi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# Path için

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path

# Kendi app'imizi çekiyoruz
from siteApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index , name='home'),
    path('hakkimizda', hakkimizda, name='hakkimda'),
    path('urunlerimiz', urunler, name='urun'),
    path('iletisim', iletisim, name='iletisim'),
    path('urundetay/<urunId>', urundetay, name="urundetay"),
    path('urundetay/<urunId>/yorumSil/<yorumId>', yorumSil, name="yorumsil"),
    path('login', login, name="login"),
    path('singup', singup, name="singup"),
    path('profile/<profileID>', profile , name='profile'),
    path('404', errorpage, name='404'),
    path("urundetay/<urunDetayiid>/", deleteurun, name="deleteurun"),
    path('arama', searchBar, name="search"),
    path('logout', cikis, name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
