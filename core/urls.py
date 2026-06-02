from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Pages
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # Projects
    path('dashboard/projects/add/', views.ProjectCreateView.as_view(), name='project-add'),
    path('dashboard/projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project-edit'),
    path('dashboard/projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),

    # Skills
    path('dashboard/skills/add/', views.SkillCreateView.as_view(), name='skill-add'),
    path('dashboard/skills/<int:pk>/edit/', views.SkillUpdateView.as_view(), name='skill-edit'),
    path('dashboard/skills/<int:pk>/delete/', views.SkillDeleteView.as_view(), name='skill-delete'),

    # Contact
    path('contact/', views.ContactCreateView.as_view(), name='contact-create'),
    path('dashboard/contacts/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact-delete'),
]