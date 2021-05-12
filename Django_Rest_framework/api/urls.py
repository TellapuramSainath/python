from django.urls import path
from . import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
 	path('register/', RegisterAPI.as_view(), name='register'),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
	path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]