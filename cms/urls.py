"""cms URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from . import views
from complaints import views as cmsview

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('com', cmsview.index, name='complaints'),
    path('disputed', cmsview.disputed, name='disputed'),
    path('pending', cmsview.pending, name='pending'),
    path('rectified', cmsview.rectified, name='rectified'),
    path('observation', cmsview.observation, name='observation'),
    path('azadpur', cmsview.azadpur, name='azp'),
    path('shalimar', cmsview.shalimar, name='slm'),
    path('nsp', cmsview.nsp, name='nsp'),
    path('naraina', cmsview.naraina, name='nai'),
    path('bmsfault', cmsview.bms, name='bms'),
    path('electricalfault', cmsview.elect, name='elec'),
    path('ecsfault', cmsview.ecs, name='ecs'),
    path('tvsfault', cmsview.tvs, name='tvs'),
    path('linkedin', cmsview.linked, name='linkedin')
]

admin.site.site_title = "CMS Admin Portal"
admin.site.site_header = "CMS Login"
admin.site.index_title = "Welcome to Samsung CMS Portal"
