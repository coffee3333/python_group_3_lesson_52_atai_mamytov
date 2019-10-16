"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webapp.views import IndexView, TaskTrackerView, TaskTrackerCreateView, TaskTrackerUpdateView, TaskTrackerDeleteView, \
    TypeView, StatusView, TypesCreateView, StatusCreateView, TypesUpdateView, StatusesUpdateView, TypeDeleteView, statuses_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('track/<int:pk>/', TaskTrackerView.as_view(), name='task_track'),
    path('track/add/', TaskTrackerCreateView.as_view(), name='task_track_add'),
    path('track/<int:pk>/edit', TaskTrackerUpdateView.as_view(), name='task_track_edit' ),
    path('track/<int:pk>/delete', TaskTrackerDeleteView.as_view(), name='task_track_delete'),
    path('types/', TypeView.as_view(), name='type_ls'),
    path('statuses/', StatusView.as_view(), name='status_ls'),
    path('types/create/', TypesCreateView.as_view(), name='type_create'),
    path('statuses/create/', StatusCreateView.as_view(), name='status_create'),
    path('types/edit/<int:pk>', TypesUpdateView.as_view(), name='type_edit'),
    path('statuses/edit/<int:pk>', StatusesUpdateView.as_view(), name='status_edit'),
    path('types/delete/<int:pk>', TypeDeleteView.as_view(), name='type_delete'),
    path('statuses/delete/<int:pk>', statuses_delete_view, name='status_delete')
]
