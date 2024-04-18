"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include,re_path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("air/", include("air.urls")),
    
    path('companies/', views.all_companies, name='all_companies'),
    path('entities/', views.all_entities, name='all_entities'),

 
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('entities/<int:entity_id>/', views.entity_detail, name='entity_detail'),
    # path('push-entity-data/', views.push_entity_data, name='push_entity_data'),
    re_path('entities/entitydata',views.EntityApiView.as_view()),
    path('entities/register-entity/', views.RegisterEntity.as_view(), name='register_entity'),
    path('entities/deactivate-entity/',views.DeactivateEntity.as_view(),name='deactivate_entity')

]



