from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from teamModel import views

urlpatterns = [
    path('teammembers/', views.TeamMemberList.as_view()),
    path('teammembers/<int:pk>', views.TeamMemberDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>', views.TeamDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)