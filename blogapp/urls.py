from django.urls import path 
from . import views

app_name="blogapp"
urlpatterns = [
    path("" , views.index_view , name="index"),
    
    path(
    "blog-detail/<int:pk>/" ,
    views.BlogDetail.as_view(),
    name="blog_detail"
    ),
    # カテゴリ分けのルーティング
    path(
    "science-list/" ,
    views.ScienceView.as_view(),
    name="science"
    ),   
    path(
    "dailylife-list/" ,
    views.DailylifeView.as_view(),
    name="dailylife"
    ),   
    path(
    "music-list/" ,
    views.MusicView.as_view(),
    name="music"
    ),
    path('contact/' , views.ContactView.as_view() , name='contact')
]
