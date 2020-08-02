from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('case', views.CaseView.as_view(), name='case'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    path('recruitment', views.RecruitmentView.as_view(), name='recruitment'),
    path('recruitment/<int:pk>', views.RecruitmentDetailView.as_view(), name='recruitment-detail'),
    path('news', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('team', views.TeamView.as_view(), name='team')
]
