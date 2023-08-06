from django.urls import path 
from . import views

app_name="blogapp"
urlpatterns = [
    path("" , views.index_view , name="index"),
    
    path(
        "blog-detail/<int:pk>/" ,
        views.BlogDetail.as_view(),
        name="blog_detail"
    )
]
